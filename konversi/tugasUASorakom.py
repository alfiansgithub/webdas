import pandas as pd

hr = "==============="

def dec2binar(num):
    binar = []
    step = [hr]
    i = 0
    if num == 0:
        binar.append(0)
        step.append(0)
    while num > 0:
        step.append("{}  ".format(num))
        if num >= 2:
            string = "2 ....... {}".format(num % 2)
            step.append(string)
        binar.append(num % 2)
        num = num // 2
        i += 1
    binar.reverse()
    strBin = ''
    for i in binar:
        strBin += str(i)
    return strBin,step

def dec2oktal(num):
    oktal = []
    step = [hr]
    if num == 0:
        oktal.append(0)
        step.append(0)
    i = 0
    while num > 0:
        step.append("{}  ".format(num))
        if num >= 8:
            string = "0 ....... {}".format(num % 8)
            step.append(string)
        oktal.append(num % 8)
        num = num // 8
        i += 1
    oktal.reverse()
    strOktal = ''
    for i in oktal:
        strOktal += str(i)
    return strOktal,step

def dec2hexa(num):
    hexa = []
    step = [hr]
    if num ==  0:
        hexa.append(0)
        step.append(0)
    i = 0
    while num > 0:
        step.append("{}  ".format(num))

        numHexa = num % 16
        if num >= 16:
            string = "16 ....... {}".format(numHexa)
            step.append(string)
        if (numHexa == 10):
            numHexa = 'A'
        elif numHexa == 11:
            numHexa = 'B'
        elif numHexa == 12:
            numHexa = 'C'
        elif numHexa == 13:
            numHexa = 'D'
        elif numHexa == 14:
            numHexa = 'E'
        elif numHexa == 15:
            numHexa = 'F'
        
        hexa.append(numHexa)
        num = num // 16
        i += 1
    hexa.reverse()
    strHexa = ''
    for i in hexa:
        strHexa += str(i)   
    return strHexa,step

def main():
    print("===============================================================")
    print("|        PROGRAM KONVERSI BILANGAN  ALFIAN CORPORATION        |")
    print("|------->>>     DESIMAL,BINER,OKTAL,HEXADESIMAL     <<<-------|")
    print("===============================================================")
    while True:
        decimal = input("inputkan angka(desimal) : ")
        if decimal == '':
            break
        
        else:
            num = int(decimal)
            binar, step_bin = dec2binar(num)
            oktal, step_okt = dec2oktal(num)
            hexa, step_hex = dec2hexa(num)

            p = max([len(step_bin), len(step_okt), len(step_hex)])
            arr_binar = ['']*p
            arr_oktal = ['']*p
            arr_hexa = ['']*p

            for i in range(len(step_bin)):
                arr_binar[i] = step_bin[i]
            for i in range(len(step_okt)):
                arr_oktal[i] = step_okt[i]
            for i in range(len(step_hex)):
                arr_hexa[i] = step_hex[i]

            arr_binar = arr_binar + [hr, binar]
            arr_oktal = arr_oktal + [hr, oktal]
            arr_hexa = arr_hexa + [hr, hexa]
            label = ['']*len(arr_binar)
            
            data = {
                'binar' : arr_binar,
                'oktal' : arr_oktal,
                'hexa' : arr_hexa
            }
            df = pd.DataFrame(data, label)

            print(df)
            print('\n')

if __name__ == "__main__":
    main()


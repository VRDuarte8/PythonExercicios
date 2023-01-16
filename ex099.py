from time import sleep


def maior(*num):
    mai = 0
    cont = 0
    for v in num:
        print(v, end=' ')
        sleep(0.3)
        if v > mai or cont == 0:
            mai = v
        cont += 1
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {mai}.")
    print('-=' * 20)


maior(1, 3, 4, 6, 2, 3)
maior(51, 62, 32, 17)
maior(1616, 215, 1652)
maior(-2, -1, -6)

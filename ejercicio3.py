def num_perfecto():
    numero = int(input("ingrese un numero : "))
    cont = 0
    for i in range(1, numero):
        if numero % i ==0:
            cont += i 
    if cont == numero:
     print("perfecto") 
    else:
     print(" no es perfecto")
    return 0


def main():
    num_perfecto()
if __name__ == "__main__":
    main()

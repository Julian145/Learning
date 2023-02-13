def read_int(prompt, min, max):
    entero = True
    num = 0
    while entero:
        try:
            num = int(input(prompt))
            if num > min and num < max:
                return num
            else:
                print("Ingresaste un valor no válido")
                continue
        except:
            print("Algo salió mal, lo sentimos mucho")
            exit()
            
v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
    
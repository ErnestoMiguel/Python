from MathPack import Mathops

print("****Calculadora****".center(50))

def getinfo(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Tipo de dato incorrecto, intentelo denuevo...")

def Menu():
        print("Opciones**")
        print("***********")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Exponente")
        print("6. Salir")

def main():
    while True:
        Menu()
        while True:
            opc = input("Introduce la opcion deseada: ")
            if opc in "123456" and opc !="":
                break
            else:
                print("La Opcion Introducida no es valida...")

        if opc == "6":
            break

        num1 = getinfo("Introduce el primer numero.")
        num2 = getinfo("Introduce el segundo numero.")

        calculadora = Mathops(num1, num2)   

        while True:
            
            if opc == "1":
                print(f'El Resultado de la Suma de {num1} y {num2} es {calculadora.suma()}')
                break
            elif opc == "2":
                print(f'El Resultado de la Resta de {num1} y {num2} es {calculadora.resta()}')
                break
            elif opc == "3":
                print(f'El Resultado de la Multiplicacion de {num1} y {num2} es {calculadora.multiplicacion()}')
                break
            elif opc == "4":
                print(f'El Resultado de la Division de {num1} y {num2} es {calculadora.division()}')
                break
            elif opc == "5":
                print(f'El Resultado de la Potenciacion de {num1} y {num2} es {calculadora.exponente()}')
                break       
        
if __name__=="__main__":
    main()
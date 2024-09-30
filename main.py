def multiplicacion(num1, num2, resultado):
        Resultado_correcto = num1 * num2
            if Resultado_correcto == resultado:
                    print("ッ El resultado es correcto")
                        else:
                                print(f"❌ El resultado es incorrecto. El resultado correcto es {Resultado_correcto}.")

                                num2= int(input("Introduce el primer número: "))
                                num1= int(input("Introduce el segundo número: "))
                                resultado = int(input("Introduce el resultado de la multiplicación: "))

                                multiplicacion(num1,num2, resultado)

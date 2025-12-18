class OperadorInvalidoError(Exception):
    pass
def calculadora(operacion):
    try:
        partes = operacion.split()
        
        if len(partes) != 3:
            raise ValueError("Formato invalido")
        numero1_str, operador, numero2_str = partes
        numero1 = float(numero1_str)
        numero2 = float(numero2_str)
        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoError("Operador invalido")
        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            if numero2 == 0:
                raise ZeroDivisionError("Division entre cero")
            resultado = numero1 / numero2
        print(f"{numero1} {operador} {numero2} = {resultado}")
    except ValueError:
        print("Error: valor invalido")
    except ZeroDivisionError:
        print("Error: division entre cero")
    except OperadorInvalidoError:
        print("Error: operador invalido")

print("CALCULADORA\n")
calculadora("10 / 2")
calculadora("10 / 0")
calculadora("abc + 5")
calculadora("10 % 2")
calculadora("7 + 3")
calculadora("5 * 4")
calculadora("15 - 8")

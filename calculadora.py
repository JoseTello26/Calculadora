import sys

def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicacion(x,y):
    return x*y
def division(x,y):
    if(y != 0):
        return x/y
    else:
        print("ERROR: El divisor no debe ser 0")
        return -1

if __name__ == '__main__':
    if  len(sys.argv)!=3:
        raise Exception("Ingrese solo 2 números como parámetro")

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(f'Suma: \t{a} + {b} = {suma(a,b)}')
    print(f'Resta: \t{a} - {b} = {resta(a,b)}')
    print(f'Mult: \t{a} * {b} = {multiplicacion(a,b)}')
    print(f'Div: \t{a} / {b} = {division(a,b):.3f}')

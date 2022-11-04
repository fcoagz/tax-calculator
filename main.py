PT = 0
IVA = 0
X = 0
R = 0
import os

def market():

    PT = float(input('Coloca el valor del producto: '))
    print('{}Bs'.format(PT))
    print('')
    IVA = float(input('Coloca el interes: '))
    print('{}%'.format(IVA))
    print('')

    X = (PT * IVA) / 100
    R = PT + X

    print('Precio inicial : {}bs'.format(PT))
    print('Interes: {}bs'.format(X))
    print('El precio total: {}bs'.format(R))
    os.system('pause')
    
if __name__ == '__main__':
    market()
PT = 0
IVA = 0
X = 0
R = 0
import os

def market():

    PT = float(input('Coloca el valor del producto: '))
    print('{}$'.format(PT))
    print('')
    IVA = float(input('Coloca el interes: '))
    print('{}%'.format(IVA))
    print('')

    X = (PT * IVA) / 100
    R = PT + X

    print('Precio inicial : {}$'.format(PT))
    print('Interes: {}% == {}$'.format(IVA, X))
    print('El precio total: {}bs'.format(R))
    os.system('pause')
    
if __name__ == '__main__':
    market()

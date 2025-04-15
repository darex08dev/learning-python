def calc_num_primo(num):
    
    cont = 0
    
    for divisores in range(1, num+1):
       if (num % divisores) == 0:
           cont += 1
    
    if cont == 2:
        print(f'{num} es un número primo')
    else:
        print(f'{num} no es un número primo')

def main():
    
    while True:
        print('Numeros primos')
        numero = int(input('Ingresa tu número: '))
        calc_num_primo(numero)
        opc = input('¿Desea continuar? (S/N): ').lower()
        
        if opc == 'n':
            break
        
if __name__ == '__main__':
    main()
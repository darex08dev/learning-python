def calc_num_primo(num):
    
    cont = 0
    
    for divisores in range(1, num+1):
        
       cont += 1 if (num % divisores) == 0 else return None
            
    return f'{num} no es un número primo' if cont != 2 else print(f'{num} es un número primo')

def main():
    
    while True:
        print('Numeros primos')
        numero = int(input('Ingresa tu número: '))
        
if __name__ == '__main__':
    main()
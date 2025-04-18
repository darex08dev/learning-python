#Probando mueva implementación:
def is_prime(number):
    
    if number <= 1:
        return False
        
    for divisor in range(2,int(number ** 0.5) + 1):
        
        if (number % divisor) == 0:
            return False
    
    return True

def main():
    
    print('-- Prime Numbers --')
    
    while True:
        
        try:
            user_number = int(input ('Enter a Number: ')
            
            if is_prime(user_number):
                print(f'{user_number} is a prime number!')
            else:
                print(f'{user_number} is not a prime number!')
                
            option = input('Press \'0\' to exit. Any key to continue: ')
            
            if option == '0':
                break
            
        except ValueError:
            print('Invalid Input!')
            
if __name__ == '__main__':
    main()
def is_prime(num):
    prime_div = [1,2,3,5,7]
    div = [2,3,4,5,6,7,8,9]
    mod_arr = []

    if (num in prime_div):
        return True
    for i in range(0,len(div)):
        mod_arr.append(num % div[i])
    if 0 in mod_arr:
        return False
    else:
        return True
        
number = int(input('Enter a number: '))

while type(number) != int:
    if is_prime(number):
        print('It\'s a prime. Roll out!')
    elif not is_prime(number):
        print('It\'s not a prime.')
    number = int(input('Enter a number: '))
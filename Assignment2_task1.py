# To check if a number is even or odd

num=int(input('Enter a number:'))

rem= num%2
print(f'{rem} is the remainder of the number')

if rem == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

try:
    age = int(input('enter age:'))
    print(10 / age)

except ZeroDivisionError:
    print('Error: division zero')

except ValueError:
    print('TypeError')

else:
    print('not error...')

finally:
    print('ALLL')
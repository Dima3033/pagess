num = input(' Enter number -> ')
counter = 0
for s in num:
    if s.isdigit():
        counter+=1
print(f'Кількість цифр {counter} кількість сімволів {len(num)}')
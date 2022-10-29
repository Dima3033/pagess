try:
    num = input(' Enter pages -> ')
    q = input("q")
    print(num.count(q))
except Exception as ex:
   print(f'Erorr information: {ex}')

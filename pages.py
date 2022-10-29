try:
    num = input(' Enter pages -> ')
    q = input("Find ")
    r= input('Change ')
    edited_num = num.replace(q,r)
    print(f'{edited_num}')
except Exception as ex:
   print(f'Erorr information: {ex}')

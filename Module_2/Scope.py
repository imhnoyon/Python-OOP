# global variable
Balance =3000

def shop(item,price):
    #  global variable use korte chaile global variable name declare kore dite hbe
     global Balance
     Balance=Balance - price
     print(Balance)

shop('xphone',2000)
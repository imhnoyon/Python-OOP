
# multiple k argument ami chaile dite parbo

def name(first,last,**kargs):
    full_name=f'{first} {last}'
    print(kargs)
    # key and value ta ber kore print kore dekhtasi
    for key,value in kargs.items(): 
        print(key,value)
    print(full_name)

name(first='Mahedi',last='Hasan',title='Student',department='CSE')

person ={'Name': 'Mahedi Hasan Noyon','Ages':22,'district': 'jamalpur'}
print(person)
print(person['Ages'])
print(person.keys())
print(person.values())
person['language']='Python'
print(person)
person['Name']='Noyon'
del person['Ages']
print(person)

for key, values in person.items():
    print(key,values)

import json

path = 'studet.json'
with open(path,'r') as file:
    filedata = json.load(file)

userdata = filedata["user"]
i=1

def status_check(k):
    if k=='True':
        return 'Selected'
    else:
        return 'Not Selected'


print('Data of students interviwed for college fest on 3/11/2023:\n')
for i,items in userdata.items():
    print(f'Application Student ID {str(i)}:')
    print(f'Name: {items["name"]}')
    print(f'SapID: {items["user-id"]}')
    print(f'EmailID: {items["email"]}')
    print(f'Department: {items["department"]}')
    print(f'MHT-CET: {items["cetscore"]}%ile')
    print(f'Birth Date: {items["user-id"]}')
    address = items["address"]
    print(f'Address: {address["street"]}, {address["taluka"]}, {address["city"]}-{address["pincode"]}')
    print(f'Status: '+ f'{status_check(items["active"])}\n')
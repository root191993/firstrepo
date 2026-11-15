
contacts = {

    'Pavan': {

      'Phone': '9880543812',
      'Email': 'Pavanreddy1001@gmail.com'

    },
    'Sree': {

       'Phone': '8861317883',
       'Email': 'Sreelureddy1001@gmail.com' 
    }
}

for contact in contacts:
    print("{}'s Contact details info:".format(contact))
    print(contacts[contact]['Phone'])
    print(contacts[contact]['Email'])
    
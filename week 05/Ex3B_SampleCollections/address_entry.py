# Address_entry

contact_info = {
    "name": "Alondra Martinez",
    "address": "123 Main St",
    "city": "Charlotte" ,
    "state": "NC",
    "zip":"28348"
}
 
 
del contact_info["name"]

print(contact_info)

full_name = {
    "first name": "Alondra",
    "last name": "Martinez"
}
print(full_name)

full_name.update({"honorific": "Mrs."})
#honorific is new key
#Mrs is the value

print(full_name)
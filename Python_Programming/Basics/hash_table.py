"""HASH MAP"""

phone_book = {}
def add(phone_book,new_contact,new_number):
    phone_book[new_contact]=new_number
    print(phone_book)
x=0
while x<2:    
    new_contact = input("enter name")
    new_number = input("add number")
    add(phone_book,new_contact,new_number)
    x+=1
print(phone_book.get("ron"),phone_book.get("lilly"))
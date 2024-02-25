contact = {}

def display_contact():
    print("Name \t \t Contact Number")
    for key in contact:
        print("{}\t \t {}".format(key,contact.get(key)))

while True:
    choice = int(input("1.Add new contact \n 2.Search contact \n 3.Display Contact\n 4.Edit Contact\n 5.Delete Contact\n 6.Exit\n Enter The No. Which Operation You Want To Perform : "))
    if choice == 1:
     name = input("Enter the contact name : ")
     phone = input("Enter the mobile number : ")
     contact[name] = phone
    elif choice == 2:
       search_name = input("Enter the contact name")
       if search_name in contact:
          print(search_name,"'s contact number is ",contact[search_name])
       else:
          print("Number is not in number list")
    elif choice == 3:
       if not contact:
          print("Empty contact book")
       else:
          display_contact()
    elif choice == 4:
       edit_contact = input("Enter the contact to be edited")
       if edit_contact in contact:
          phone = input("Enter the mobile number")
          contact[edit_contact]=phone
          print("Contact Updated")
          display_contact()
       else:
          print("Name is not found in contact book")
    elif choice == 5:
       del_contact = input("Enter the contact to be deleted ")
       if del_contact in contact:
          confirm = input("Do you want to delete this contact y/n?")
          if confirm == 'y' or confirm == 'Y':
             contact.pop(del_contact)
          display_contact()
       else:
          print("Name is not found in contact book")
    else:
       break
       
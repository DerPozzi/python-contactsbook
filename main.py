from tabulate import tabulate

class Person: 
    def __init__(self, name = " ", birthday = " ", phone = " ", email = " ", notes = " ") -> None:
        self.name = name
        self.birthday = birthday
        self.phone = phone 
        self.email = email 
        self.notes = notes 
        pass

contacts = []

def sortByName(val):
    return val.name

def addContact():
    global contacts
    print("===== ADD USER =====")
    name = input("Name: ")
    birthday = input("Birthday: ")
    phone = input("Phone: ")
    email = input("Email: ")
    notes = input("Notes: ")
    
    temp = Person(name, birthday, phone, email, notes)
    contacts.append(temp)
    contacts.sort(key = sortByName)

def editForm(c: Person):
    print(" What do you want to edit?")
    userInput = input(" (1) Name \n (2) Birthdate \n (3) Phone \n (4) Email \n (5) Notes \n (0) Quit \n >>> ")
    match int(userInput):
        case 0:
            print("Quitting... ")
            return
        case 1:
            name = input("New name: ")
            c.name = name
        case 2:
            birthdate = input("New birthdate: ")
            c.birthdate = birthdate
        case 3:
            phone = input("New phone: ")
            c.phone = phone
        case 4:
            email = input("New email: ")
            c.email = email
        case 5:
            notes = input("New notes: ")
            c.notes = notes
    userInput = input("Do you want to Edit more? (Y/N) ")
    if userInput == "Y":
        editForm(c)
    elif userInput == "N":
        return

def editContact():
    if len(contacts) == 0:
        print(" >< No Contacts added yet...")
        return
    
    name = input(" Which contact do you want to edit? \n >>> ")
    for c in contacts:
        if (c.name == name):
            editForm(c)
            return
            
    print(" Contact not found, try again...")

def displayContacts():
    global contacts
    if len(contacts) == 0:
        print(" >< No Contacts added yet...")
        return
    print(" Total contacts: " + str(len(contacts)))
    i = 1
    for c in contacts:
        print(str(i) + ".\t" + c.name)
        i += 1


def searchContact(name):
    group = []
    for contact in contacts:

        if contact.name == name:
            group.append(contact)
        
    return group if group else None

def mainMenu():
    print("===== MAIN MENU ===== \n")
    userInput = input(" (1) Add contact \n (2) Edit contact \n (3) Show contacts \n (4) Search Contact \n (0) Quit Program \n >>> ")
    match userInput:
        case "1":
            addContact()
        case "2":
            editContact()
        case "3": 
            displayContacts()
        case "4":
            name = input("Name: ")
            contact = searchContact(name)
            if contact:
                for value in contact:
                    table = [["Phone", value.phone], ["Email", value.email], ["Birthday", value.birthday], ["Notes", value.notes]]
                    print("\n" + tabulate(table, headers = ["Name", value.name]) + "\n")
            else: 
                print("No contact found...")
        case "0":
            print ("Quitting program... ")
            return False
    return True

def readContactsFile():
    file = open("contacts.txt", "r")
    data = file.read()
    if len(data) <= 10:
        return
    lines = data.split("\n")
    print (lines)
    for contact in lines:
        print(contact)
        if len(contact) == 0:
            continue
        attributes = contact.split("^")
        print(attributes)
        temp = Person(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
        contacts.append(temp)
    
    file.close()
    contacts.sort(key = sortByName)


if __name__ == "__main__":
    readContactsFile()
    while True:
        if not mainMenu():
            break
    file = open("contacts.txt","w")
    for contact in contacts:
        l = contact.name + "^" + contact.birthday + "^" + contact.phone + "^" + contact.email + "^" + contact.notes + "\n"
        file.write(l)
    file.close()

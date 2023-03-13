class Person: 
    def __init__(self, name, birthday, phone, email, notes) -> None:
        self.name = name
        self.birthday = birthday
        self.phone = phone 
        self.email = email 
        self.notes = notes 
        pass

contacts = []

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

def editContact():
    print("edit")

def displayContacts():
    global contacts
    i = 1
    for c in contacts:
        print(str(i) + ".\t" + c.name + "\t" + c.phone)
        i += 1


def mainMenu():
    print("===== MAIN MENU ===== \n")
    userInput = input(" (1) Add Contact \n (2) Edit Contact \n (3) Show Contacts \n (0) Quit Program \n >>> ")
    match userInput:
        case "1":
            addContact()
        case "2":
            editContact()
        case "3": 
            displayContacts()
        case "0":
            return False
    return True



if __name__ == "__main__":
    while True:
        if not mainMenu():
            break

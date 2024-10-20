from collections import UserDict

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Phone(Field):

    def __init__(self, value: str):
        self.value = value

    def validate_phone(self) -> bool:
        if self.value.isnumeric() and (len(self.value) == 10):
                return True
        return False

    def __str__(self):
        return str(self.value)   
    

class Record:
    
    def __init__(self, name: Name, phones: Phone):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone.validate_phone():
            self.phones.append(phone)
        else:
            print('Phone number is not valid. Must be a 10-digit number')
        
    
    def revome_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone.validate_phone():
            self.phones.remove(phone)
        else:
            print('Phone number is not valid. Must be a 10-digit number')
    
    def edit_phone(self, old_number, new_number):
        try:
            old_phone = Phone(old_number)
            new_phone = Phone(new_number)
            if old_phone.validate_phone() and new_phone.validate_phone():
                self.revome_phone(str(old_phone))
                self.add_phone(str(new_phone))
            else:
                raise ValueError
        except ValueError:
            print('One of numbers or both are not valid. Must be a 10-digit numbers')

    def find_phone(self, phone_number: str) -> Phone:
        phone = Phone(phone_number)
        if phone.validate_phone():
            for element in self.phones:
                if element == phone:
                    return element
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    record_book = {}

    def add_record(self, record: Record):
        self
    
    def find(self, name: str) -> Record:
        pass
    
    def __str__(self):
        pass
    

    
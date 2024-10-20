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
    
    def __init__(self, name: Name, phones=None):
        self.name = Name(name)
        self.phones = phones if phones else []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone.validate_phone():
            self.phones.append(phone)
        else:
            print('Phone number is not valid. Must be a 10-digit number')
        
    
    def remove_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone.validate_phone():
            for p in self.phones:
                if p.value == phone.value:
                    self.phones.remove(p)
                    return
            print(f"{phone_number} not found")
        else:
            print('Phone number is not valid. Must be a 10-digit number')
    
    def edit_phone(self, old_number, new_number):
        try:
            old_phone = Phone(old_number)
            new_phone = Phone(new_number)
            if old_phone.validate_phone() and new_phone.validate_phone():
                for index, phone in enumerate(self.phones):
                    if phone.value == old_phone.value:
                        self.phones[index] = new_phone
                        return
            else:
                raise ValueError
        except ValueError:
            print('One of numbers or both are not valid. Must be a 10-digit numbers')

    def find_phone(self, phone_number: str) -> Phone:
        phone = Phone(phone_number)
        if phone.validate_phone():
            for element in self.phones:
                if element.value == phone.value:
                    return element
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def delete_record(self, name: str):
        return self.data.pop(name, None)
    
    def find(self, name: str) -> Record:
        return self.data.get(name, None)
    
    def __str__(self):
        return '\n'.join(record.__str__() for record in self.data.values())
    

    
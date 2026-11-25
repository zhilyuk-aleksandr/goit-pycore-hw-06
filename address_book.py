from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name is required.")
        super().__init__(value.strip())


class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"[0-9]{10}", value):
            raise ValueError("Phone must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        return next((item for item in self.phones if item.value == phone), None)

    def remove_phone(self, phone):
        item = self.find_phone(phone)
        if item is None:
            raise ValueError("Phone not found.")
        self.phones.remove(item)

    def edit_phone(self, old_phone, new_phone):
        item = self.find_phone(old_phone)
        if item is None:
            raise ValueError("Phone not found.")
        self.phones[self.phones.index(item)] = Phone(new_phone)

    def __str__(self):
        phones = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]


if __name__ == "__main__":
    book = AddressBook()
    record = Record("Olena")
    record.add_phone("0501234567")
    record.add_phone("0670000000")
    book.add_record(record)
    record.edit_phone("0670000000", "0671111111")
    print(book.find("Olena"))

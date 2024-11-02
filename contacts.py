import json

class Contacts:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def add_contact(self, id, first_name, last_name):
        if id in self.data:
            return "error"
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
        return {id: [first_name, last_name]}

    def modify_contact(self, id, first_name, last_name):
        if id not in self.data:
            return "error"
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
        return {id: [first_name, last_name]}

    def delete_contact(self, id):
        if id not in self.data:
            return "error"
        deleted_contact = {id: self.data.pop(id)}
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
        return deleted_contact

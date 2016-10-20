import base64
import uuid

class User():

    id = None
    names = None
    lastnames = None
    email = None
    password = None

    def __init__(self):
        self.id = None
        self.names = None
        self.lastnames = None
        self.email = None
        self.password = None

    def set_variables_user(self, names, lastnames, email, password):
        self.id = str(uuid.uuid4())
        self.names = names
        self.lastnames = lastnames
        self.email = email
        self.password = base64.b64encode(password)

    def set_variables_db(self, dictionary):
        self.id = dictionary["id"]
        self.names = dictionary["names"]
        self.lastnames = dictionary["lastnames"]
        if "email" in dictionary:
            if dictionary["email"] is None:
                self.email = None
            else:
                self.email = dictionary["email"]
        else:
            self.email = None

        if "password" in dictionary:
            if dictionary["password"] is None:
                self.password = None
            else:
                self.password = dictionary["password"]
        else:
            self.password = None

    def to_dict(self):
        return {"id":self.id,"names":self.names , "lastnames": self.lastnames, "email": self.email, "password": self.password}

    def to_save(self):
        return {"id":self.id, "names":self.names , "lastnames": self.lastnames, "email": self.email, "password": self.password}
import base64

from ..model.User import User


#-----  AWS ------#
from ..aws.DynamoDB import DynamoDB

class UserController():

    fileSystem = None
#-----  AWS ------#
    dynamoDB = None

    def __init__(self):
    #-----  AWS ------#
        self.dynamoDB = DynamoDB()

    def add_User(self, names, lastnames, email, password):
        user = User()
        user.set_variables_user(names, lastnames, email, password)
        data = self.dynamoDB.createUser(user)

        if data is None:
            return None
        else:
            data.email = None
            data.password = None
            return data

    def login_user(self, email, password):
        data = self.dynamoDB.confirmLogin(email, base64.b64encode(password))
        user = None
        if data is not None:
            user = User()
            user.set_variables_db(data)
        return user

    def getUserFromDict(self, dictionary):
        user = User()
        user.set_variables_db(dictionary)
        return user

    def getUserContestNumber(self, user_id):
        return self.dynamoDB.getUserContestNumber(user_id)

    def getUserVideoNumber(self, user_id):
        return self.dynamoDB.getUserVideoNumber(user_id)

    def getUserId(self, user_id):
        data = self.dynamoDB.getUser(user_id)
        tmp_user = None
        if data is not None:
            tmp_user = User()
            tmp_user.set_variables_db(data)
        return tmp_user

    def getLatestUser(self):
        users = []
        for user in self.dynamoDB.getLatestUser():
            tmp_user = User()
            tmp_user.set_variables_db(user)
            users.append(tmp_user)
        return users

    def getUsers(self):
        users = []
        for user in self.dynamoDB.getUsers():
            tmp_user = User()
            tmp_user.set_variables_db(user)
            users.append(tmp_user)
        return users
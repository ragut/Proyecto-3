import unicodedata
import random
import uuid

from ..aws.DynamoDB import DynamoDB

#//----- MODELO DEL CONCURSO -----//
class Contest():

    id = None
    user_id = None
    name = None
    banner = None
    url = None
    date_ini = None
    deadline = None
    description = None
    num_video = -1

    dynamoDB = DynamoDB()

    def __init__(self):
        self.id = None
        self.user_id = None
        self.names = None
        self.banner = None
        self.url = None
        self.date_ini = None
        self.deadline = None
        self.description = None

        self.num_video = -1

#//-----    FUNCIONES CRUD MODELO CONCURSO    -----//

    def set_num_video(self, num_video):
        self.num_video = num_video

    def set_variables_contest(self, user_id, name, date_ini, deadline, description, url):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.names = name
        self.url = url
        self.generate_url()
        self.banner = self.url+".png"
        self.date_ini = date_ini
        self.deadline = deadline
        self.description = description

    def setId(self, id):
        self.id = id

    def set_variables_db(self, dictionary):
        self.id = dictionary["id"]
        self.user_id = dictionary["user_id"]
        self.names = dictionary["name"]
        self.banner = dictionary["banner"]
        self.url = dictionary["url"]
        self.date_ini = dictionary["date_ini"]
        self.deadline = dictionary["deadline"]
        self.description = dictionary["description"]


    def generate_url(self):
        if self.url is not None:
            url_aux = unicodedata.normalize('NFKD', self.url).encode('ASCII', 'ignore')
            url_aux = url_aux.lower()
            url_aux = url_aux.replace(" ","_")

            final_url = url_aux
            exist = self.dynamoDB.user_url_exist(final_url)

            while exist == True:
                final_url = url_aux + "_" + str(random.randrange(1, 101, 2))
                exist = self.dynamoDB.user_url_exist(final_url)

            self.url = final_url

    def to_dict(self):
        return {"id":self.id, "user_id":self.user_id, "name": self.names, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}

    def to_save(self):
        return {"id":self.id, "user_id":self.user_id, "name": self.names, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}
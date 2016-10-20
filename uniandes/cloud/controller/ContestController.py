from ..model.Contest import Contest
from .VideoController import VideoController
from .ImageService import ImageService
from .FileController import FileController
from ..filesystems.Filesystem import Filesystem
#-----  AWS ------#
from ..aws.DynamoDB import DynamoDB
from ..aws.S3 import S3

class ContestController():

    fileSystem = None

#-----  AWS ------#
    dynamoDB = None
    s3 = None

    def __init__(self):
        self.fileSystem = FileController()

    #-----  AWS ------#
        self.dynamoDB = DynamoDB()
        self.s3 = S3()

#//---- INSERTA CONCURSO    -----//
    def insertContest(self, user_id, names, date_ini, deadline, description, url, baner):
        contest = Contest()
        contest.set_variables_contest(user_id, names, date_ini, deadline, description, url)

    #-----  GUARDA LA IMAGEN    ------#
        img = ImageService().generate_img(baner)
        img.save(Filesystem().ulr_banner+contest.banner,"png")
        img.close()

    #-----  AWS -----#
        self.s3.save_banner(Filesystem().ulr_banner,contest.banner)
        self.dynamoDB.createContest(contest)

        return contest

#//---- OBTIENE CONCURSOS POR USUARIO   ----//
    def getUserContest(self, user_id):
        data = self.dynamoDB.getUserContest(user_id)
        contests = []
        for contest in data:
            newContest = Contest()
            newContest.set_variables_db(contest)
            contests.append(newContest)
        return contests

#//-----    OBTIENE CONCURSO ESPECIFICO ----//
    def getContest(self, contest_id):
        data = self.dynamoDB.getContest(contest_id)
        contest = Contest()
        contest.set_variables_db(data)
        return contest

    def getContestAll(self):
        data = self.dynamoDB.getContestAll()
        contest = Contest()
        contest.set_variables_db(data)
        return contest

    #//-----    OBTIENE CONCURSO ESPECIFICO ----//
    def getURLContest(self, contest_url):
        data = self.dynamoDB.getURLContest(contest_url)
        contest = Contest()
        contest.set_variables_db(data)
        return contest

#//-----    ACTUALIZA CONCURSO ESPECIFICO ----//
    def updateContest(self, id, user_id,  name, date_ini, deadline, description, url, baner):
        contest = Contest()
        contest.set_variables_contest(user_id,  name, date_ini, deadline, description, url)
        #contest.set_id(id)

    #-----  GUARDA LA IMAGEN    -----#
        img = ImageService().generate_img(baner)
        img.save(Filesystem().ulr_banner+contest.banner,"png")
        img.close()

    #-----  AWS -----#
        self.s3.save_banner(Filesystem().ulr_banner,contest.banner)

        return self.dynamoDB.updateContest(contest)

#//-----    ELIMINA CONCURSO ESPECIFICO ----//
    def deleteContest(self, id):
        VideoController().deleteContestVideo(id)
        return self.dynamoDB.deleteContest(id)


from .TemporalFileService import TemporalFileService
from .ImageService import ImageService
from .VideoController import VideoController
from ..model.Contest import Contest

#-----  AWS ------#
from ..aws.DynamoDB import DynamoDB
from ..aws.S3 import S3

class ContestController():

    fileSystem = None

#-----  AWS ------#
    dynamoDB = None
    s3 = None

    def __init__(self):

    #-----  AWS ------#
        self.dynamoDB = DynamoDB()
        self.s3 = S3()
        self.image_service = ImageService()

#//---- INSERTA CONCURSO    -----//
    def insertContest(self, user_id, names, date_ini, deadline, description, url, baner):
        contest = Contest()
        contest.set_variables_contest(user_id, names, date_ini, deadline, description, url)

    #-----  IMAGEN TEMPORAL    ------#
        img = self.image_service.generate_img(baner)
        img.save(TemporalFileService().url_banner+contest.banner,"png")

    #-----  AWS -----#
        self.s3.save_banner(TemporalFileService().url_banner,contest.banner)
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
        tmp_contest = None
        if data is not None:
            tmp_contest = Contest()
            tmp_contest.set_variables_db(data)
        return tmp_contest

#//-----    ACTUALIZA CONCURSO ESPECIFICO ----//
    def updateContest(self, id, user_id,  name, date_ini, deadline, description, url, baner):
        old_contest = self.dynamoDB.getContest(id)
        self.s3.delete_banner(old_contest["banner"])
        contest = Contest()
        contest.set_variables_contest(user_id,  name, date_ini, deadline, description, url)
        contest.setId(id)

    #-----  IMAGEN TEMPORAL    -----#
        img = ImageService().generate_img(baner)
        img.save(TemporalFileService().url_banner+contest.banner,"png")

    #-----  AWS -----#
        self.s3.save_banner(TemporalFileService().url_banner,contest.banner)
        return self.dynamoDB.updateContest(contest)

#//-----    ELIMINA CONCURSO ESPECIFICO ----//
    def deleteContest(self, id):
        VideoController().deleteContestVideo(id)
        old_contest = self.dynamoDB.getContest(id)
        self.s3.delete_banner(old_contest["banner"])
        return self.dynamoDB.deleteContest(id)


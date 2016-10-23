from ..model.ContestVideo import ContestVideo
from .TemporalFileService import TemporalFileService
import os

#-----  AWS ------#
from ..aws.DynamoDB import DynamoDB
from ..aws.SQS import SQS
from ..aws.S3 import S3

class VideoController():

    fileSystem = None

#-----  AWS ------#
    dynamoDB = None
    sqs = None
    s3 = None

    def __init__(self):
    #-----  AWS ------#
        self.dynamoDB = DynamoDB()
        self.sqs = SQS()
        self.s3 = S3()

#//----     CREA EL VIDEO   -----//
    def createVideo(self, user_id, contest_id, name_video, email, names_user, lastnames_user, videoFile, extension):
        video = ContestVideo()
        video.set_variables_video(user_id,contest_id, name_video, email, names_user, lastnames_user, "On Process", extension)

    #------ VIDEO TEMPORAL ------//
        path = os.path.join(TemporalFileService().url_original,video.video_name+"."+video.original_file)
        fileObj = open(path, 'wb')
        fileObj.write(videoFile)
        fileObj.close()
    #-----  AWS ------#
        self.s3.save_original(TemporalFileService().url_original,video.video_name+"."+video.original_file)
        self.sqs.send_message_to_process(video.id)

        return self.dynamoDB.createVideo(video)

    def getVideoById(self, video_id):
        data = self.dynamoDB.getVideoByID(video_id)
        video = ContestVideo()
        video.set_variables_db(data)
        return video

#//----  OBTIENE LOS VIDEOS PROCESADOS DEL CONCURSO   ----//
    def getContestOkVideos(self, contest_id):
        data = self.dynamoDB.getContestOkVideos(contest_id)
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----     TRAE LOS VIEDOS ----//
    def getContestVideo(self, contest_id):
        data = self.dynamoDB.getContestVideo(contest_id)
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//-----    PROCESA LOS VIDEOS  ----//
    def getProcessVideo(self):
        data = self.dynamoDB.getProcessVideo()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//---- ACTUALIZA EL ESTADO DEL VIDEO   ----//
    def updateStatusVideo(self, video_id):
        return self.dynamoDB.updateStatusVideo(video_id)

#//---- OBTIENE LOS VIDEOS PARA PROCESAR   ----//IRA EN LA SQS
    """def getVideoToProcess(self):
        video = self.database.getVideoToProcess()
        if video is not None:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            return tmp_video
        else:
            return None"""

#//----     TRAE LOS ULTIMOS 10 VIDEOS   ----//
    def getLatestVideo(self):
        data = self.dynamoDB.getLatestVideo()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----     ACTUALIZA EL ESTADO DEL VIDEO   ----//
    def getOkVideos(self):
        data = self.dynamoDB.getOkVideos()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----      ELIMINA VIDEO   ----//
    def deleteContestVideo(self, contest_id):       #//OK
        videos = self.dynamoDB.getContestVideo(contest_id)
        for video in videos:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            if(tmp_video).status is "OK":
                #Informacion
                self.dynamoDB.deleteVideo(video.id)
            else:
                #Informacion
                self.dynamoDB.deleteVideo(video.id)
            #self.dynamoDB.deleteVideo(video.id)
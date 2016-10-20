from uniandes.cloud.controller.VideoController import VideoController
from uniandes.cloud.controller.VideoService import VideoService
from uniandes.cloud.controller.MailController import MailController

#-----  AWS   -----#
from uniandes.cloud.aws.S3 import S3
from uniandes.cloud.aws.SQS import SQS

print "Init File Processing"

messages = SQS().get_message_to_process()
s3 = S3()

for message in messages:
    if message.message_attributes is not None:
        print "Retrieving Video"
        video_id = message.message_attributes.get('Video').get('StringValue')#Carga mensajes en SQS
        video = VideoController().getVideoById(video_id)
        if video is not None:
            if video.video_name is not None:
                print "Processing video with id " + video.id

                VideoService().process_video(fileSystem.get_original_url(), fileSystem.get_converted_url(), video.video_name, video.original_file)
                VideoController().updateStatusVideo(video.id)
                MailController().sendMail(video.email, video.names_user)
                message.delete() #Elimina los mensajes en SQS
            else:
                print "Video filename corrupted"
        else:
            print "All videos are processed"
    else:
        print "Message without attribute"

print "Finish Processing"
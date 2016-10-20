import boto3
from boto3.dynamodb.conditions import Attr
import os

class DynamoDB:

    dynamoDB = None

    def __init__(self):
       self.dynamoDB = boto3.resource('dynamodb', region_name="us-west-2",
                                       aws_access_key_id=os.environ["aws_access_key_id"],
                                       aws_secret_access_key=os.environ["aws_secret_access_key"])

    def createUser(self, user):
        self.dynamoDB.Table('User').put_item(Item=user.to_save())
        return user

    def getUsers(self):
        response = self.dynamoDB.Table('User').scan()
        user = response['Items']
        if len(user) == 0:
            return []
        else:
            return user

    def getUser(self, id):
        response = self.dynamoDB.Table('User').get_item(Key={"id":id})
        user = response['Item']
        return user

    def getLatestUser(self):
        response = self.dynamoDB.Table('User').scan(Limit=6)
        user = response['Items']
        if len(user) == 0:
            return []
        else:
            return user

    def getUserByEmail(self, email):
        response = self.dynamoDB.Table('User').scan(FilterExpresssion=Attr('email').eq(email))
        user = response['Items']
        if len(user) == 0:
            return []
        else:
            return user

    def confirmLogin (self, email, password):
        response = self.dynamoDB.Table('User').scan(FilterExpression=Attr('email').eq(email) & Attr('password').eq(password))
        user = response['Items']
        if len(user) == 0:
            return None
        else:
            return user[0]

    def createContest(self, contest):
        self.dynamoDB.Table('Contest').put_item(Item=contest.to_save())
        return contest

    def getUserContest(self, user_id): #Esta pendiente
        response = self.dynamoDB.Table('Contest').scan(FilterExpression=Attr('user_id').eq(user_id))
        contest = response['Items']
        if len(contest) == 0:
            return []
        else:
            return contest

    def getContest(self, id):
        response = self.dynamoDB.Table('Contest').get_item(Key={"id":id})
        contest = response['Item']
        return contest

    def getContestAll(self):
        response = self.dynamoDB.Table('Contest').scan()
        contest = response['Items']
        if len(contest) == 0:
            return []
        else:
            return contest

    def getURLContest(self, url):
        response = self.dynamoDB.Table('Contest').scan(FilterExpression=Attr('url').eq(url))
        contest = response['Items']
        if len(contest) == 0:
            return []
        else:
            return contest

    def updateContest(self, contest):
        self.dynamoDB.Table('Contest').update_item(
            Key={"id":contest.id},
            UpdateExpression= 'SET #names = :names, #baner = :banner, #date_ini = :date_ini, #deadline = :deadline, #description = :description',
            ExpressionAttributeValues={
                ':names':contest.names,
                ':banner': contest.banner,
                ':date_ini': contest.date_ini,
                ':deadline':contest.deadline,
                ':description': contest.description
            },
            ExpressionAttributeNames={
                '#names': "names",
                '#banner': "baner",
                '#date_ini': "date_ini",
                '#deadline': "deadline",
                '#description': "description"
            }
        )
        return self.getContest(contest.id)

    def deleteContest(self, id):
        self.dynamoDB.Table('Contest').delete_item(Key={"id":id})

    def getUserContestNumber(self, user_id): #Revisar
        response = self.dynamoDB.Table('Contest').scan(FilterExpression=Attr('user_id').eq(user_id))
        contest = response['Items']
        return len(contest)

    def getContestVideoNumber(self, contest_id): #Revisar
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('contest_id').eq(contest_id))
        video = response['Items']
        return len(video)

    def getUserVideoNumber(self, user_id):
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('user_id').eq(user_id))
        video = response['Items']
        return len(video)

    def createVideo(self,video): #No existe
        self.dynamoDB.Table('Video').put_item(Item=video.to_save())
        return video

    def getContestVideo(self, contest_id):
        response = self.dynamoDB.Table('Video').scan(FilterExpression = Attr('contest_id').eq(contest_id))
        video = response['Items']
        if len(video) == 0:
            return []
        else:
            return video

    def getContestVideoNum(self, contest_id):
        response = self.dynamoDB.Table('Video').scan(FilterExpression = Attr('contest_id').eq(contest_id))
        video = response['Items']
        return  len(video)

    def getVideoByID(self, id):
        response = self.dynamoDB.Table('Video').get_item(Key = {"id":id})
        video = response['Item']
        return video

    def getContestOkVideos(self, contest_id):
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('contest_id').eq(contest_id) & Attr('status').eq('OK'))
        video = response['Items']
        if len(video) == 0:
            return []
        else:
            return video

    def getOkVideos(self):
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('status').eq('OK'))
        video = response['Items']
        if len(video) == 0:
            return []
        else:
            return video
    def getLatestVideo(self):
       # response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('status').eq('OK'),Limit=6)
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('status').eq('OK'))
        video = response['Items']
        if len(video) == 0:
            return []
        else:
            return video

    def getProcessVideo(self):
        response = self.dynamoDB.Table('Video').scan(FilterExpression=Attr('status').eq('On Process'))
        video = response['Items']
        if len(video) == 0:
            return []
        else:
            return video

    def updateStatusVideo(self, id):
        self.dynamoDB.Table('Video').update_item(
            Key={"id":id},
            UpdateExpression='SET #status = :status',
            ExpressionAttributeValues={
                ':status': "OK"
            },
            ExpressionAttributeNames={
                '#status': "status"
            }
        )
        return self.getVideoByID(id)

    def deleteVideo(self, id):
        self.dynamoDB.Table('Video').delete_item(Key={"id":id})

    def user_url_exist(self, url):
        response = self.dynamoDB.Table('Contest').scan(FilterExpression=Attr('url').eq(url))
        video = response['Items']
        if len(video) == 0:
            return False
        else:
            return True
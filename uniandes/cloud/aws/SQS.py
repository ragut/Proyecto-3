import boto3
import os

class SQS:

    sqs = None

    def __init__(self):
        self.s3 = boto3.resource('sqs', region_name="us-west-2",
                                       aws_access_key_id=os.environ["aws_access_key_id"],
                                       aws_secret_access_key=os.environ["aws_secret_access_key"])

    def send_message_to_process(self, video_id):
        queue = self.sqs.get_queue_by_name(QueueName='m_videoToprocess')
        queue.send_message(MessageBody='New video to process', MessageAttributes={
            'Video': {
                'StringValue': video_id,
                'DataType': 'String'
            }
        })

    def get_message_to_process(self):
        queue = self.sqs.get_queue_by_name(QueueName='m_videoToprocess')
        return queue.receive_messages(MessageAttributeNames=['Video'])
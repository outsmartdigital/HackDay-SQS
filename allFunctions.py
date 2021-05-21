import boto3

def createQueue(name):
    sqs = boto3.resource('sqs')

    queue = sqs.create_queue(QueueName=name, Attributes={'DelaySeconds': '5'})

    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))

def useQueue(name):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName=name)

    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
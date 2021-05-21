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

def sendMessage(queueName, message, autor):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName=queueName)

    response = queue.send_message(MessageBody=message, MessageAttributes={
        'Author': {
            'StringValue': autor,
            'DataType': 'String'
        }
    })

    print('MessageId: ',response.get('MessageId'))
    print('MD5OfMessageBody: ',response.get('MD5OfMessageBody'))

def processMessage(queueName):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName=queueName)

    for message in queue.receive_messages(MessageAttributeNames=['Author']):

        author_text = ''
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            if author_name:
                author_text = ' ({0})'.format(author_name)

        print('Hello, {0}!{1}'.format(message.body, author_text))
        message.delete()
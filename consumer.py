import boto3

def processMessage(queueName):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName=queueName)
    received_messages = queue.receive_messages()

    if not received_messages:
        print('There is no message in the queue ({0})'.format(queueName))
    else:
        for message in received_messages:

            author_text = ''
            if message.message_attributes is not None:
                author_name = message.message_attributes.get('Author').get('StringValue')
                if author_name:
                    author_text = ' ({0})'.format(author_name)

            print('Hello, {0}!{1}'.format(message.body, author_text))
            message.delete()

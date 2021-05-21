import boto3

sqs = boto3.resource('sqs')

def sendMessage(queueName, message, autor):
    queue = sqs.get_queue_by_name(QueueName=queueName)

    response = queue.send_message(MessageBody=message, MessageAttributes={
        'Author': {
            'StringValue': autor,
            'DataType': 'String'
        }
    })

    print('MessageId: ',response.get('MessageId'))
    print('MD5OfMessageBody: ',response.get('MD5OfMessageBody'))

    try:
        return response.get('MessageId')
    except: 
        return 'Erro: Não foi possível inserir a mensagem na fila'
    
import boto3
from random import randint
from producer import sendMessage
from consumer import processMessage
from queueFunctions import createQueue

def createTickets(wantCreateQueue, queueName, author, quantity):

    if wantCreateQueue:
        createQueue(queueName)

    i=0
    for i in range(quantity):
        sendMessage(queueName, str(randint(quantity*2,quantity*8)), author)
    

def getTicket(queueName, quantity):

    processMessage(queueName)
    
    return 1
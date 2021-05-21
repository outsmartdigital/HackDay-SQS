from queueFunctions import createQueue
from consumer import processMessage
from producer import sendMessage
from ticket import createTickets, getTicket

createQueue('hackday_test')

sendMessage('hackday_test', 'Test Message', 'Yas e Daniel')

processMessage('hackday_test')

createTickets(1, 'tickets_queue', 'Yas e Daniel', 5)

getTicket('tickets_queue', 1)

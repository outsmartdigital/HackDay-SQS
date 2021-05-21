from consumer import processMessage
from producer import sendMessage

sendMessage('hackday_test', 'Apagar', 'Yas')

processMessage('hackday_test')
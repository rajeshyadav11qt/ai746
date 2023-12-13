import datetime
import telepot
from telepot.loop import MessageLoop
import GPIO as IO
from time import sleep

IO.setmode(IO.BCM)
IO.setwarning(False)

relay = 21
relay2 = 20

now=datetime.datetime.now()

def handle(msg):
chat_id = msg[‘chat’][‘id’]
command = msg[‘text’]

print(‘Received’)
print(command)

if command == ‘/hi’:
	telegram_bot.sendMessage(chat_id,str(“Hello”)
elif command == ‘/time’:
telegram_bot.sendMessage(chat_id,str(now.hour)+str(now,minute))
elif command == ‘/relayon’:
	telegram_bot.sendMessage(chat_id,str(“Relay1 On”)
	IO.output(relay,True)
	print(“Relay1 ON”)
elif command == ‘/relayoff’:
	telegram_bot.sendMessage(chat_id,str(“Relay1 Off”)
	IO.output(relay,False)
	print(“Relay1 OFF”)

telegram_bot = telepot.Bot('Bot Token') 
#(add your bot token here in place of ‘Bot Token’. Refer video on how to generate telegram bot token)
#Example:
# bot = telepot.Bot(‘21tewugb873t872usyf78756c36bv835h9386’)

print(“Up and running….”)

while 1:
	sleep(10)


#(DONT FORGET TO ADD TELEGRAM TOKEN)
import sys
import time
import telepot

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop

numbers={}
cntr=0
flagOfDo=0
result=1

def handle(msg):
    global flagOfLevel
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='*', callback_data='2')],[InlineKeyboardButton(text='%', callback_data='1')],[InlineKeyboardButton(text='+', callback_data='3')],[InlineKeyboardButton(text='-', callback_data='4')]
    ])
    content_type, chat_type, chat_id = telepot.glance(msg)
#    print(msg)

    global flagOfDo
    global cntr
    global result
    
    if msg['text']=='/start':
        bot.sendMessage(chat_id, 'hii ! it is a simple calculator with python.enter the first number.')
        flagOfDo=1
        cntr=0
        return
        
    numbers[cntr]=int(msg['text'])
    
    if cntr==1:
        bot.sendMessage(chat_id,'choose your function',reply_markup=keyboard)
        cntr=0
        result=0
    
    if result==1:
        if flagOfDo==1:
            bot.sendMessage(chat_id,'Send your second number ...')
            flagOfDo=0
            cntr=1
            return
  
        else:
            bot.sendMessage(chat_id,'Send first number ...')
            flagOfDo=1
            return
#     bot.sendMessage(chat_id, message)




def on_callback_query(msg):
	
    query_id, from_id, query_data=telepot.glance(msg, flavor='callback_query')    
    #    print(msg)
    global result
    global numbers

    if query_data=='0':
        bot.sendMessage(from_id,'Enter /start to start again',reply_markup=keyboard)
        numbers={}
        
    elif query_data=='1':
        bot.sendMessage(from_id,'your result: ' +  str(numbers[0]) + ' % ' + str(numbers[1]) + '=' + str(numbers[0]/numbers[1]))
        bot.sendMessage(from_id,'Enter /start to start again')
        result=1
        numbers={}
        
    elif query_data=='2':
        bot.sendMessage(from_id,'your result: ' +  str(numbers[0]) + ' * ' + str(numbers[1]) + '=' + str(numbers[0]*numbers[1]))
        bot.sendMessage(from_id,'Enter /start to start again')
        result=1
        numbers={}
        
    elif query_data=='3':
        bot.sendMessage(from_id,'your result: ' +  str(numbers[0]) + ' + ' + str(numbers[1]) + '=' + str(numbers[0]+numbers[1]))
        bot.sendMessage(from_id,'Enter /start to start again')
        result=1
        numbers={}
        
    elif query_data=='4':
        bot.sendMessage(from_id,'your result: ' +  str(numbers[0]) + ' - ' + str(numbers[1]) + '=' + str(numbers[0]-numbers[1]))
        bot.sendMessage(from_id,'Enter /start to start again')
        result=1
        numbers={}
    else:
        bot.sendMessage(from_id,'try again !!!')
        result=1
        bot.sendMessage(from_id,'Enter /start to start again')
       	   
bot = telepot.Bot('BOT-TOKEN')
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
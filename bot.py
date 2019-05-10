from pyrogram import Client, Filters








import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('firebase-adminsdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jeet-fc311.firebaseio.com/'
})

app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')




string = 'j m'


@app.on_message(Filters.chat(-1001309160459) & Filters.text & ~ Filters.regex('👇'))
def forawrd(client, message):
   if string == 'j m' :
      client.forward_messages(-1001344956857, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
      client.forward_messages(-1001356076506, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    
@app.on_message(Filters.command('cheat1') & Filters.private)
def ran(client , message ):
      string.replace('j','t')
      message.reply(string)

@app.on_message(Filters.command('nocheat') & Filters.private)
def ran(client , message ):
      string.replace('j','m')
      message.reply(string)
      users_ref = ref.child('users')
      users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})

app.run()


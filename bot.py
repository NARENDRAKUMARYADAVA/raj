from pyrogram import Client, Filters



Firebase Realtime Database using Python SDK
Posted on February 17, 2018 — 21 min read — in development






Firebase Realtime Database is a NoSQL cloud-hosted database. Data is stored as JSON and synchronized in realtime to every connected client. Using Firebase Admin SDK, we can read and write Realtime Database data with full admin privileges, or limited privileges.

In my recent project, I had the opportunity to work with Firebase Realtime Database. So, I decided to write a basic guide to using Firebase Realtime Database using Python SDK.

Download source code from Github.

Add Firebase to the App
To use the Firebase Admin SDK, we'll need a Firebase project, a service account to communicate with the Firebase service, and a configuration file with your service account's credentials. Follow Add Firebase to your app to get the configuration file, which is a JSON file.

Install Firebase Python SDK
The Firebase Admin Python SDK enables server-side (backend) Python developers to integrate Firebase into their services and applications. To install Firebase Admin Python SDK, simply execute the following command in a terminal:

pip install firebase-admin
Initialize the SDK
Initialize the SDK with this code snippet:

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-adminsdk.json')
# Initialize the app with a service account, granting admin privileges
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

app.run()


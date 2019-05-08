from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('1339685184'))
def forawrd(client, message):
    client.forward_messages('1344956857', '1339685184', [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
app.run()

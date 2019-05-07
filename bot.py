from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('icc_cricket'))
def forawrd(client, message):
    client.forward_messages('indianLine11', 'icc_cricket', [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
app.run()

from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('ferrariline1'))
def forawrd(client, message):
    client.forward_messages('-1001356076506', 'ferrariline1', [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    edit_message_text('zearn', '2344', [message] )

app.run()


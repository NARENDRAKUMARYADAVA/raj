from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('cfamovies1'))
def forawrd(client, message):
    client.forward_messages('icc_cricket', 'cfamovies1', 'as_copy(bool, True)' , [message.message_id])
app.run()

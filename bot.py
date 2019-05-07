from pyrogram import Client, Filters




app = Client('account')

@app.on_message(Filters.chat('cfamovies1'))
def forawrd(client, message):
    client.forward_messages('icc_cricket', 'cfamovies1', [message.message_id])
app.run()

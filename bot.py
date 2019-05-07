from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('https://t.me/joinchat/AAAAAENZH2KQhHhHrUvz6g'))
def forawrd(client, message):
    client.forward_messages('https://t.me/joinchat/AAAAAFAqabnU15MWqOSbig', 'https://t.me/joinchat/AAAAAENZH2KQhHhHrUvz6g', [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
app.run()

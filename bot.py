from pyrogram import Client, Filters
app = Client("845406847:AAEhd9rK83epir_9RwwFxOed8s6j0JqIwNM",869912,"a7b049e08df35464047d57e5134327e5")
u = '-1001205348094'
s = '-1001378725482'
@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
   client.send_message(int(u),message.text.replace('🎾' , '🥎'))
           

@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
   client.send_sticker(int(u),message.sticker.file_id)
        

app.run()

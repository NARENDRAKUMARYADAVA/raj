from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')


hii ='hii','dekho','winner', 'fix', '😱', '😳', 'fixer', '👆', '👇', 'match', 'pass', 'sab', 'chase', 'defend', 'hai', 'karvana', 'link',' loss', 'audio', 'varna',' pura', 'puri',' open', 'paid', 'contact',' baazigar', 'market',' load', 'whatsapp','Baazigar','https://','Https://'

@app.on_message(Filters.chat(-1001309160459) & Filters.text & ~ Filters.regex(hii))
def forawrd(client, message):
    client.forward_messages(-1001344956857, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    

app.run()


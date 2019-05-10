from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')




string = 'j m'


@app.on_message(Filters.chat(-1001309160459) & Filters.text & ~ Filters.regex('👇'))
def forawrd(client, message):
   if string == 'j m' :
      client.forward_messages(-1001344956857, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
      client.forward_messages(-1001356076506, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    
@app.on_message(Filters.command('cheat1') & Filters.private)
def ran(client , message ):
      string.replace('g','t')
      message.reply(string)

@app.on_message(Filters.command('nocheat') & Filters.private)
def ran(client , message ):
      string.replace('j','m')
      message.reply(string)

app.run()


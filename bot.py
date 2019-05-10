from pyrogram import Client, Filters


app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')




@app.on_message(Filters.chat(-1001309160459) & Filters.text & ~ Filters.regex('👇'))
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()

    for line in lines:
      if line == "started": 
          client.forward_messages(-1001344956857, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
          client.forward_messages(-1001356076506, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )

@app.on_message(Filters.command('status'))
def main(client, message) :
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()

      for line in lines:
        if line == "started":
           message.reply("Forwarding is on ! ")
        if line == "closed":
           message.reply("Forwarding is stopped ! ")
 
@app.on_message(Filters.command('offline'))
def main(client, message) :
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':

    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("Forwarding is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':

    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("Forwarding is on !")

app.run()


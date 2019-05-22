from pyrogram import Client, Filters
app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')
@app.on_message(Filters.chat(-1001378725482) & Filters.text)
def forawrd(client, message):
    client.forward_messages(-1001137104015, -1001378725482, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    client.forward_messages(-1001290422511, -1001378725482, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
       
    files = open("sure.txt" , "r")
    file = open("text.txt" , "r")
    lines = file.readlines()
    liner = files.readlines()
    file.close()
    files.close()
    
    for line in lines:
      if line == "started": 
          client.forward_messages(-1001344956857, -1001378725482, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    
@app.on_message(Filters.command('status'))
def main(client, message) :
  if message.from_user.id == 491634139:
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("Forwarding is on ! ")
        if line == "closed":
           message.reply("Forwarding is stopped ! ")
 

@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
 
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("Forwarding is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
  if message.from_user.id == 491634139:
 
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("Forwarding is on !")

@app.on_message(Filters.command('zearnon'))
def main(client, message) :
  if message.from_user.id == 491634139:
 
    files = open("sure.txt" , "w")
    files.write("started")
    files.close()
    message.reply("Forwarding is on(zearn)!")


@app.on_message(Filters.command('zearnoff'))
def main(client, message) :
  if message.from_user.id == 491634139:
 
    files = open("sure.txt" , "w")
    files.write("closed")
    files.close()
    message.reply("Forwarding is off(zearn)!")

@app.edit_message(Filters.chat(-1001378725482))
def main(client, message, edit_message):
   client.edit_message_text(message.chat.id,message.message_id,message)


app.on_message(Filters. private)
def main(client, message) :
    files = open("sue.txt" , "w")
    files.write(message)
    files.close()
    message.reply(message)


app.run()


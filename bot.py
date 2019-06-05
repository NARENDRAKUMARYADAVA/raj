from pyrogram import Client, Filters
app = Client('485505720:AAGQHhdDGWlEnzPUNcJlX8wBSdVneBjnUXc')

u = '-1001115051772'
s = '-1001378725482'
@app.on_message(Filters.chat(int(s)) & Filters.text)
def forawrd(client, message):
    print(message.text)
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if '⚫️' in message.text :
            client.send_message(int(u),message.text.replace('⚫️' , '**💘'))
        else:
          if '🔴' in message.text :
            client.send_message(int(u),message.text.replace('🔴' , '🏝'))
          else:
            if message.text == '6' :
               client.send_message(int(u),'**Six**')
            else:
              if message.text == '4' :
               
               client.send_message(int(u),'**Four**')
              else:
                if message.text == '🚹 WIDE BALL 🚹' :
                  
                  client.send_message(int(u),message.text.replace('🚹 WIDE BALL 🚹' , '🤦‍♂️ **WIDE BALL** 🤦‍♂️'))
                else:
                    if message.text == '🚾 WKT GYA WKT 🚾' :
                     
                     client.send_message(int(u),message.text.replace('🚾 WKT GYA WKT 🚾' , '🚾** Wicket Wicket Wicket** 🚾 ')) 
                    else:
                       if 'NO BALL' in message.text:
                         client.send_message(int(u),message.text.replace('NO BALL' , '🔛** NO BALL **🔛') )
                       else:
                          if 'DRINKS BREAK' in message.text:
                           
                            client.send_message(int(u), '🍻** DRINKS BREAK **🍻') 
                          else:
                            if 'DEAD BALL' in message.text:
                               
                               client.send_message(int(u), '🔁** DEAD BALL **🔄') 
                            else:
                              if message.text == 'RUKA BOWLER✔️':
                                 client.send_message(int(u), '🛑** BOWLER RUKA **🛑')
                              else:
                                if message.text == '🚾WICKET WICKET WICKET 🚾':
                                   
                                   client.send_message(int(u),message.text.replace('🚾WICKET WICKET WICKET 🚾' , '🚾** Wicket Wicket Wicket **🚾 '))
                                else:
                                   client.send_message(int(u),message.text.replace('🎾' , '🥎'))


@app.on_message(Filters.chat(int(s)) & Filters.sticker)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line == 'closed':
        if message.sticker.file_id == 'CAADBQADFAQAAlrCoBKRHyVMca5GGQI' :
            
            client.send_message(int(u),'🍾 **INNINIGS BREAK** 🍾' )

@app.on_message(Filters.command('status'))
def main(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")        
@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
app.run()

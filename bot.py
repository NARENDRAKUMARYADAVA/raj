from pyrogram import Client, Filters




app = Client('1BVtsOIIBuy2r9S8NTamRbH7qr0OLKCYciWjjGI1ldOgNpKjmMW5EDlQLZZ8fNsZuMqg4ajQPpnzGwATytBiaMhCGDC9lfWmsM_yHEkAlitMdh6Fnqxgi7ForMlTSGQ-5n7uqxZEfbrJkg6pDBS6n7qJOV6z1AXz9lO9ruQyxscBmeHrZZ8goTZw66GE9G01LNUc7ebKxf6Z9foz1mXEhpkbd3rQhyffSwoLXvWchF6Q6OwOnm4FisJUYDc4aA6AqgBC1ZVrL4zeDOeODcuPbfO5VneD8gjPKbBmPxIvmcqaEyN1Cd4UW4AqEJPydOzTMYS0v9tQ1ZkLVR6H660FXXNDfBOPDoss=')

@app.on_message(Filters.chat(-1001309160459))
def forawrd(client, message):
    client.forward_messages(-1001356076506, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    

app.run()


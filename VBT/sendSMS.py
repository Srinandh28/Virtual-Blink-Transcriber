from twilio.rest import Client

#authentication
def send(msg):
    account_sid="ACC_SID" #fill in appropriately
    auth_token="AUTH_TKN" #fill in appropriately
    client=Client(account_sid, auth_token)
    if msg:
        client.messages.create(
        to="+919791172932", #fill in appropriately
        from_="+919842903913", #fill in appropriately
        body=msg)
    else:
        client.messages.create(
        to="+919791172932", #fill in appropriately
        from_="+919842903913",#fill in appropriately
        body="Default Message")#fill in appropriately
        
    

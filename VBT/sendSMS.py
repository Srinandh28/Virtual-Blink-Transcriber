from twilio.rest import Client

#authentication
def send(msg):
    account_sid="ACC_SID" #fill in appropriately
    auth_token="AUTH_TKN" #fill in appropriately
    client=Client(account_sid, auth_token)
    if msg:
        client.messages.create(
        to="", #fill in appropriately
        from_="", #fill in appropriately
        body=msg)
    else:
        client.messages.create(
        to="", #fill in appropriately
        from_="",#fill in appropriately
        body="Default Message")#fill in appropriately
        
    

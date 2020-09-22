from fbchat import log, Client
from pushbullet.pushbullet import PushBullet
import requests
import json



apiKey = "YOUR API KEY"
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

class Checker:
    sendmes = False
    prev_auth = '0000000000000'


def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    ACCESS_TOKEN = apiKey
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id == 'YOUR AUTHOR ID' :
            #stop the bot
            if  message_object.text == 'stop':
                print('this will stop')
                Checker.sendmes = False
            

        if author_id == 'YOUR AUTHOR ID' :
            #start the bot
            if message_object.text == 'start':
                print('this will start')
                Checker.sendmes = True

        if message_object.text == "Important" or message_object.text == "important":
            print('later')
            a = 'Title'
            b = 'Notification description'
            send_notification_via_pushbullet(a,b)
            

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid :

            if Checker.sendmes and author_id != Checker.prev_auth and thread_id !='2725849170831156' and thread_id !='2008417709226395' and thread_id !='1838653722924816' and thread_id !='3761350763910072' : 
                     
             message_object.text = "YOUR REPLY"
             self.send(message_object, thread_id=thread_id, thread_type=thread_type)
             print(' \n \n \n \n \n ')
             print(author_id)
             print(thread_id)
             print('\n \n \n \n \n')
             Checker.prev_auth = author_id

            Checker.prev_auth = author_id

        
        

    sendmes = False      

def on2FACode(self):
        """Called when a 2FA code is needed to progress."""
        return input("Please enter your 2FA code --> ")


client = EchoBot('YOUR EMAIL', 'YOUR PASSWORD')
client.listen()





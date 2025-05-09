import os
import requests
from dotenv import load_dotenv
load_dotenv()
class Facturascripts:
    def __init__(self):
        self.url = os.environ["FS_API_URL"]
        self.token = os.environ["TOKEN"]


    def enviar_mensaje(self, mensaje):
        print (self.url)
        response = requests.post(
            self.url,
            headers = {
                'Content-Type': 'application/json',
                'TOKEN': self.token
            },
            json = {
                'content': mensaje
            }
        ).json()
        
        responseId = response.get('id')
        print('peru')
        print (responseId)
        print('peru2')
        resp = requests.get(
            self.url + '/' + responseId,
            headers={
                'Content-Type': 'application/json',
                'TOKEN': self.token
            }
        ).json()
        respMsg = resp['messages'][1]['content']
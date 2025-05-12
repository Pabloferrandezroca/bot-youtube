import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()
class Facturascripts:
    def __init__(self):
        self.url = os.environ["FS_API_URL"]
        self.token = os.environ["TOKEN"]


    def send_message(self, mensaje):
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
        respMsg = self.wait_response(responseId)
        return respMsg
        
    
    def wait_response(self, responseId):
        attempts = 0
        while attempts < 100:
            resp = requests.get(
                self.url + '/' + responseId,
                headers={
                    'Content-Type': 'application/json',
                    'TOKEN': self.token
                }
            ).json()
            time.sleep(1)
            resp_length = len(resp['messages'])
            if (resp_length > 1 and resp['messages'][1]['content'] != ''):
                break
            attempts += 1
            print(attempts)
        respMsg = resp['messages'][1]['content']
        return respMsg
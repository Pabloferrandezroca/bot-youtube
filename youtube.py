import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from Comments import Comments
from Facturascripts import Facturascripts
from dotenv import load_dotenv
load_dotenv()
import os

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server(port=8080)
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)



comments_list = Comments.getCommentsByVideo(youtube, os.environ["YT_CHANNEL_ID"])
commentIds = []
commentTexts = []


for comments_json in comments_list:
    
    commentId = [comment['snippet']['topLevelComment']['id'] for comment in comments_json['items']]
    commentText = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_json['items']]
    commentIds.append(commentId)
    commentTexts.append(commentText)



for i in range(len(commentIds)):
    for j in range(len(commentIds[i])): 
        parent_id = commentIds[i][j] 
        text = commentTexts[i][j] 

        facturascripts = Facturascripts()
        response_message = facturascripts.send_message(text)
        # Crear un comentario y responder
        comment = Comments(parent_id, text)
        comment.replyComments(youtube, response_message)

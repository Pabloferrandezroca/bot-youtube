from typing import Self


class Comments:

    def __init__(self, id, text):
        self.id = id
        self.text = text
        

    def getVideos(youtube, id):
        videos = youtube.search().list(
            part="snippet",
            channelId=id,
            maxResults=25,
            type="video"
        )
        responseVideos = videos.execute()

        video_ids = [item['id']['videoId'] for item in responseVideos['items']]
        return video_ids
    
    @staticmethod
    def getCommentsByVideo(youtube, id):
        video_ids = Comments.getVideos(youtube, id)
        video_comments = []
        for video_id in video_ids:
            comments = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id
            )
            responseComments = comments.execute()
            video_comments.append(responseComments)
        return video_comments


    def replyComments(self,youtube, response_message):
        request = youtube.comments().insert(
            part="snippet",
            body={
                "snippet": {
                    "parentId": self.id,
                    "textOriginal": response_message
                }
            }
        )
        request.execute()
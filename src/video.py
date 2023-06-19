import os

from googleapiclient.discovery import build
api_key: str = os.getenv('API_KEY_YOUTUBE')
youtube = build('youtube', 'v3', developerKey=api_key)

class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.url_video = f'https://youtu.be/{self.video_id}'
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title



class PLVideo(Video):
    def __init__(self, video_id, plist_id):
        super().__init__(video_id)
        self.plist_id = plist_id
        self.video_id = video_id
        self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id
                                                    ).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.url_video = f'https://youtu.be/{self.video_id}'
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']




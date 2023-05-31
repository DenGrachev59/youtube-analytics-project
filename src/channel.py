import json
import os
from googleapiclient.discovery import build
#
# import isodate

from helper.youtube_api_manual import youtube
api_key: str = os.getenv('API_KEY_YOUTUBE')
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id  # HighLoad Channel
        channel = youtube.channels() .list(id=channel_id, part='snippet,statistics').execute()

        return print(json.dumps(channel, indent=2, ensure_ascii=False))

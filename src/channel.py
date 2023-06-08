import json
import os

import self
from googleapiclient.discovery import build

#
# import isodate

# from helper.youtube_api_manual import youtube
api_key: str = os.getenv('API_KEY_YOUTUBE')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # self.dict_channel = (json.dumps(self.channel, indent=2, ensure_ascii=False))
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]['default']["url"]
        self.subscribe_count = self.channel["items"][0]["statistics"]['subscriberCount']
        self.video_count = self.channel["items"][0]["statistics"]['videoCount']
        self.view_count = self.channel["items"][0]["statistics"]['viewCount']

    def __repr__(self):
        """Метод вывода информации об экземпляре (для разработчика)"""
        return f'{self.__class__.__name__} (https://www.youtube.com/channel/{self.__channel_id})'

    def __str__(self):
        """Метод вывода информации об экземпляре (для пользователя)"""
        return f'{self.title} (https://www.youtube.com/channel/{self.__channel_id})'

    def __add__(self, other):
        """Метод сложения атрибутов экземпляра"""
        return int(self.subscribe_count) + int(other.subscribe_count)

    def __sub__(self, other):
        """Метод вычитания атрибутов экземпляра"""

        return int(self.subscribe_count) - int(other.subscribe_count)

    def __gt__(self, other):
        """Метод сравнения >"""
        return int(self.subscribe_count) > int(other.subscribe_count)

    def __ge__(self, other):
        """Метод сравнения >="""
        return int(self.subscribe_count) >= int(other.subscribe_count)

    def __lt__(self, other):
        """Метод сравнения <"""
        return int(self.subscribe_count) < int(other.subscribe_count)

    def __le__(self, other):
        """Метод сравнения <="""
        return int(self.subscribe_count) <= int(other.subscribe_count)

    def __eq__(self, other):
        """Метод сравнения =="""
        return int(self.subscribe_count) == int(other.subscribe_count)

    def print_info(self) -> str:

        """Выводит в консоль информацию о канале."""
        # channel_id = self.channel_id  # HighLoad Channel
        # channel = youtube.channels() .list(id=channel_id, part='snippet,statistics').execute()
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        dict_channel = (json.dumps(channel, indent=2, ensure_ascii=False))
        # print(dict_channel)
        return dict_channel

    @property
    def channel_id(self):
        """Геттер для доступа к данным в атрибуте"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, name):
        """Сеттер для возможности менять имя,тк self.name приватный атрибут"""
        if isinstance(name, str) and len(name) <= 10 and name.isdigit() is not True:
            self.__name = name
        else:
            print("False name or invalid")

    @classmethod
    def get_service(cls):
        """Сервис для получения данных  канала ютюб и создание объекта класса"""
        id_channel = input('Input id channel :')

        channel = youtube.channels().list(id=id_channel, part='snippet,statistics').execute()
        youtube_channel = Channel(id_channel)
        return f' Data channel:\n {channel},\n\n Созданный объект класса "Channel"\n{youtube_channel}'

    def to_json(self, file_name=None):
        with open(file_name, 'w') as f:
            json.dump(self.channel, f)

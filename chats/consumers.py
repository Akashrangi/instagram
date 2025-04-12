import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Chat


class ChatApp(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(f"mychat_app_{self.scope['user']}", self.channel_name)
    
    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None):
        text_data = json.loads(text_data)
        # print(f"==>> text_data: {text_data}")
        await self.channel_layer.group_send(
            f"mychat_app_{text_data['user']}",
            {
                'type': 'send_msg',
                'msg': text_data['msg']
            }
        )
        await self.save_chat(text_data)

    @database_sync_to_async
    def save_chat(self, text_data):
        frnd = User.objects.get(username=text_data['user'])
        mychats, created = Chat.objects.get_or_create(user = self.scope['user'], frnd=frnd)
        if created:
            mychats.chats = {}
        mychats.chats[str(datetime.datetime.now())+"1"] = {'user': 'me', 'msg': text_data['msg']}
        mychats.save()
        mychats, created = Chat.objects.get_or_create(user=frnd, frnd=self.scope['user'])
        if created:
            mychats.chats = {}
        mychats.chats[str(datetime.datetime.now())+"2"] = {'user': frnd.username, 'msg': text_data['msg']}
        mychats.save()
    async def send_videonofication(self,event):
        await  self.send(event['msg'])

    async def send_msg(self,event):
        # print(event['msg'])
        await  self.send(event['msg'])
    async def chat_message(self, event):
        # print(event['message'])
        await self.send(json.dumps("Total Online :- "+str(event['message'])))
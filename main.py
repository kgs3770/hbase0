# pip install fastapi uvicorn
from fastapi import FastAPI
import happybase
from pydantic import BaseModel
import uuid
from datetime import datetime

class Chatroom(BaseModel):
    room_name: str

class Message(BaseModel):
    room_id: str
    content: str

connection = happybase.Connection('localhost', port=9090)

app = FastAPI()

@app.get('/')   # => urls.py
def index():    # => views.py
    return {'hello': 'world'}


# 채팅방 생성
@app.post('/chatroom')
def create_chatroom(chatroom:Chatroom):
    table = connection.table('chatrooms')
    chatroom_id = str(uuid.uuid4())

    table.put(chatroom_id, {'info:room_name': chatroom.room_name})

    return {
        'chatroom_id' : chatroom_id, 
        'room_name': chatroom.room_name
        }

# 채팅방 조회
@app.get('/chatrooms')
def get_chatrooms():
    table = connection.table('chatrooms')
    rows = table.scan()

    result = []

    for k, v in rows:
        result.append(
            {
                'chatroom_id': k,
                'room_name': v[b'info:room_name'],
            }
        )
    return result       

#메세지 전송
@app.post('/messages')
def create_message(message: Message):
    table = connection.table('messages')
    
    room_id = message.room_id
    timestamp = int(datetime.now().timestamp() * 1000)
    message_id = f'{room_id}-{timestamp}'

    table.put(message_id, {'info:content':message.content, 'info:room_id': room_id})

    return {
        'message_id': message_id,
        'room_id': room_id,
        'content': message.content
    }   

#메세지 조회
@app.get('/chatrooms/{room_id}/messages')
def get_messages(room_id: str):
    table = connection.table('messages')
    prefix = room_id.encode('utf-8')

    # table.scan(row_prefix_prefix)
    rows = table.scan(row_prefix=prefix, reverse=True)

    result = []
    for k, v in rows:
        result.append({
            'message_id': k,
            'room_id': v[b'info:room_id'],
            'content': v[b'info:content'],
        })
    return result
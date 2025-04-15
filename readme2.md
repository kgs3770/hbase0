- melon setting
chrome
=wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# install
sudo apt --fix-broken install -y
sudo dpkg -i google-chrome-stable_current_amd64.deb


chrome-driver


- Selenium
pip install selenium


-css speedrun
li:nth-of-type(1) /* 형제 요소 중에서 첫 번째 <li> 요소를 선택합니다. */

p:not(.foo) /* 클래스가 'foo'가 아닌 모든 <p> 요소를 선택합니다. */

li:nth-of-type(2n+3) /* 형제 요소 중에서 3번째, 5번째, 7번째 등 (2n+3) 번째 <li> 요소들을 선택합니다. */

div > * /* <div> 요소의 직계 자식 요소들을 모두 선택합니다. */

span[data-item] /* 'data-item'이라는 속성이 있는 <span> 요소를 선택합니다. */

p ~ span /* <p> 요소 다음에 나오는 형제 <span> 요소들을 모두 선택합니다 (동등한 형제 관계). */

:enabled /* 사용 가능한 상태의 폼 요소(예: <input>, <button> 등)를 선택합니다. */

#one, #two, #five, #six, #nine /* id가 'one', 'two', 'five', 'six', 'nine'인 요소들을 모두 선택합니다. */

a + span /* <a> 요소 바로 다음에 나오는 형제 <span> 요소를 선택합니다. (인접 형제 선택자) */

div#foo > div.foo /* id가 'foo'인 <div>의 자식 중 클래스가 'foo'인 <div>를 선택합니다. */

div div span + code:not(.foo) /* 
    <div> 내부의 <div> 안에 있는 <span> 요소 바로 다음에 위치한 
    클래스가 'foo'가 아닌 <code> 요소를 선택합니다.
*/



-Hbase
테이블 생성 
=create 'students' , 'info'

테이블 조회
= list

hbase-2.5.11/bin/start-hbase.sh
hbase-2.5.11/bin/stop-hbase.sh


테이블에 데이터 넣기
put 'students', '1', 'info:name', 'hong'
put 'students', '1', 'info:age', '20'
put 'students', '2', 'info:name', 'kim'
put 'students', '2', 'info:address', 'seoul'

scan 'students' = 전체 데이터 출력

데이터 수정
 put 'students', '1', 'info:age', '30'

데이터 삭제
delete 'students', '2', 'info:address'
deleteall 'students', '1'  = .전체 데이터 삭제


# 출력 개수 제한
scan 'messages', {LIMIT => 3}

# 특정 컬럼만 조회
scan 'messages', { COLUMNS => ['info:text']}

# 범위 지정 조회
scan 'messages', { STARTROW => 'room1', STOPROW => 'room2'}

# prefix 기준 조회
scan 'messages', { FILTER => "PrefixFilter('room')" }


04/15
ubuntu@1-02:~/damf2/hbase$
fastapi
hbase-main.py에서만 다른 버전의 파이썬을 쓸거임

pyenv -v
pyenv versions =  사용가능한 파이썬 버전 목록
pyenv install 3.11.12 

사용 할 버전 변경
pyenv global 3.11.12
pyenv global 3.13.2
pyenv local 3.11.12 = 로컬로 설정

python -m venv venv
source venv/bin/activate

pip install fastapi uvicorn

damf2 > hbase > main.py 코드 작성

uvicorn main:app --reload =>  서버실행
http://localhost:8000/docs

터미널2
bin/hbase-daemon.sh start thrift

터미널1
서버종료
pip install happybase

main
<!-- from happybase

connection = happybase.Connection('localhost', port=9090) -->

uvicorn main:app --reload

# 채팅방 생성
@app.post('/chatroom')
def create_chatroom():
    pass

# 채팅방 조회
@app.get('/chatrooms')
def get_chatrooms():
    pass

#메세지 전송
@app.post('/messages')
def create_message():
    pass

#메세지 조회
@app.get('/chatrooms/{room_id}/messages')
def get_messages():

터미널2
hbase shell
list

안될때
<!-- kill
kill -9 29625 -->
or
sudo vi/etc/hosts
000.0.0.0.  1-~
. 추가

chatroom
messages 테이블 삭제

disable 'chatroom'
drop 'chatroom'
disable 'messages'
drop 'messages'
# 테이블 생성
create 'chatrooms', 'info'
create 'messages', 'info'

main.py 코드 작성
        room_name: str
        @app.post('/chatroom')
def create_chatroom():
    connection.table('chatrooms')
    table.put()

ubuntu@1-02:~/damf2/hbase$
uvicorn main:app --reload --port 9999
=http://127.0.0.1:9999/docs


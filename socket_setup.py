 import socketio

 server_address = "http://localhost:5000"
 sio = socketio.AsyncClient()

 @sio.event
 def connect():
     await sio.connect(server_adress)
     print("I'm connected!")

 @sio.event
 def connect_error(data):
     print("The connection failed!")

 @sio.event
 def disconnect():
     print("I'm disconnected!")

 # @sio.event
 # def message(data):
 #     print('I received a message!')
 #
 # @sio.on('my message')
 # def on_message(data):
 #     print('I received a message!')
 #
 # @sio.event
 # async def message(data):
 #     print('I received a message!')
 # await sio.emit('my message', {'foo': 'bar'})

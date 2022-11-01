import zmq
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

categories = ['addition', 'subtraction', 'multiplication']
msg = 0

# send 10 requests
for i in range(10):
    time.sleep(2)
    if msg > 2:
        msg = 0
    socket.send_string(categories[msg])
    message = socket.recv_json()
    print(f'Request {i + 1} received reply: {message}')
    msg += 1


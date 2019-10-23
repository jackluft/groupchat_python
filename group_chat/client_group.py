import socket
import threading
import time
s = socket.socket()
host = ''
port = 3451
# enter your host name
s.connect((host,port))
print("To send to one person enter '@' then username then ':'")
print("else enter message to send to group")
user = raw_input("Enter you user name: ")
s.send(user.encode('UTF-8'))
def s_recv():
    while True:
        data = s.recv(1024).decode('UTF-8')
        print(str(data))


def s_send():
    while True:
        mess = raw_input("Enter your message: ")
        s.send(mess.encode('UTF-8'))

threading.Thread(target=s_recv).start()
threading.Thread(target= s_send).start()


while True:
    time.sleep(1)



s.close()

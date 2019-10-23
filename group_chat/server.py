# oct 13, 2019
# group chat program
#[Done] if mess from cleint starts with @ then the cleint wants to send to one person
# To fix: when u send a private mess dosent tell who sent it
# still working on not done!!!!
# Dosen't close the connection and remove client from list
import socket
import threading
s = socket.socket()
host =''
port = 3451
s.bind((host,port))
#up to 100 cleints max
s.listen(100)
def s_recv(conn,adr):
    global clients

    while True:
        coal = True
        print("waiting.......")
        data = conn.recv(1024).decode('UTF-8')
        print("data recieved: "+str(data))
        if data.startswith("@"):

            if data.find(":") != -1:
                data2 = data.split(":")[1]
                mess2 = data.split(":")[0]
                mess3 = mess2.split("@")[1]
            else:
                conn.send("Must put [:] at end of username ".encode('UTF-8'))
                coal = False

            if coal == True:
                if clients.get(mess3) != None:
                    term = clients[mess3]
                    data3 ="From: "+ str([number for number, name in clients.items() if name == conn])+" : "+str(data2)
                    term.send(data3.encode('UTF-8'))
                else:
                    conn.send("User not found: " + str(mess3).encode('UTF-8'))
        else:
            for c in clients.values():
                if c!= conn:
                    full_data = "From server: "+str(data)
                    c.send(full_data.encode('UTF-8'))
            print("Sent to Group: "+str(data)+ " From: "+str(adr))
    conn.close()



clients = {}
while True:
    conn,adr = s.accept()
    username = conn.recv(1024).decode('UTF-8')
    print("username: "+str(username)+" For: "+str(adr))
    clients[username] = conn
    threading.Thread(target= s_recv,args=(conn,adr,)).start()
    print("Thread open!!!")

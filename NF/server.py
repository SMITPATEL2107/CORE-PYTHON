import socket
def server_program():
    # get the host name
    host=socket.gethostname()  
    port=5000 #initiate port no above 1024
   
    server_socket=socket.socket()  #get instance
    #look closely.The bind() function takes tuple as argument
    server_socket.bind((host,port))  #bind host address and port together
    print('server start')
    #configure how many client the server can lsten simultaneously
    server_socket.listen(2)

    conn,address=server_socket.accept()  #accept new connection
    print("connection from:-"+str(address))
    while True:
        #recieve data stream. it won't accept data packet greater than 1024 bytes
        data=conn.recv(1024).decode()
        if not data:
            #ifdata is not recieved break
            break
        print("from connected user:-"+str(data))
        data=input('->')
        conn.send(data.encode())  #send data to the client
    conn.close()  #close the connetion

if __name__=='__main__':
    server_program()
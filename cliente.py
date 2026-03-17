# Cliente
import socket

HOST = "127.0.0.1"
PORT = 2018

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = s.recv(1024).decode() #Aguardando jogador
    print(msg)
    while True:
        msg = s.recv(1024).decode() #Aguardando 
        jogada = input(msg)
        s.sendall(jogada.encode())
        msg = s.recv(1024).decode()
        print(msg)
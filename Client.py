import socket as socket

IP = "127.0.0.1"
PORTA = 56767

message = input("Inserisci la parola sulla quale verra' applicata la trasformata di Burrows Wheeler ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((IP, PORTA))
    print ("Connesso al server")
    client.sendall(message.encode())
    data = client.recv(1024)
    print("Dati ricevuti dal server:", data.decode())

print("Chiusura connessione")
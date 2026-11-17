import socket as socket
import AlgoritmoBWT

IP = "127.0.0.1"
PORTA = 56767

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((IP, PORTA))
    server.listen(5)

    print("Server in ascolto su " + IP + ":" + str(PORTA))

    with server.accept()[0] as client:
        print("Connessione accettata dal client: " + str(client.getsockname()))
        data = client.recv(1024)
        parola = data.decode()
        print("Dati ricevuti dal client:", parola)
        bwt_result = AlgoritmoBWT.trasformata_BWT(parola)
        client.sendall(bwt_result.encode())
        print("Dati inviati al client:", bwt_result)
        
print("Chiusura connessione")
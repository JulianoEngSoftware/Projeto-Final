import socket as sock

#aqui colocamos o IP do servidor que queremos nos conectar
HOST = '127.0.0.1'
PORTA = 9999

socket_cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

#cliente solicita conexão
socket_cliente.connect((HOST, PORTA))
print(5*"*" + "chat iniciado" +5*"*")
nome = input('informe seu nome para entrar no chat: ')
nome += "\n"

#aqui estamos enviando o nome do cliente
socket_cliente.sendall(nome.encode())

#cliente envia dados para o servidor
while True:
    try:
        mensagem = input("")
        socket_cliente.sendall(mensagem.encode())
    except:
        print("Erro no envio...")
        socket_cliente()
        break #Ao contrário do continue, ele não retorna para o inicio e tenta novamente, ele encerra o loop

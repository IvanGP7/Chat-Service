# 1. preguntar usuario
# 2. Al acceder te muestra las siguientes opciones: 
#       a) Connect chat:
#           Te conecta a otro chat privado, especificando el id.
#           La conexión se debe abrir una UI dedicada con el chat.
#           Una vez concectado el cliente debe escuchar y poder enviar mensajes.
#       b) Subscribe to group chat
#           Empieza escuchando los mensajes de una chat grupal, por especificar su id.
#           Si el chat no existe el servidor lo crea.
#       c) Discover chats
#           Pregutnta al servidor una lista de chats activos.
#           Los chats activos son los chats grupales y privados que estan actualmente activos.
#       d) Access insult channel
#           El canal insult es usado para enviar mesajes a un cliente indefinido que te pide una petición.
# 
import grpc
import NameServer_pb2_grpc, NameServer_pb2
#import MessageBroker_pb2_grpc, MessageBroker_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = NameServer_pb2_grpc.NameServerServiceStub(channel)
response = stub.test
print(response.sentence)

username = input("Introduce your username: ")

#pedir al servidor los ids respecto al usuario
print("Choose one option between 1 and 5:")
option = 0
count = 0
while (option > 1 or option < 5):
    if count > 0:
        print("ERROR VALUE '{option}': TRY AGAIN!")
    print("Choose one option 1-4:")
    print("     1. Connect chat")
    print("     2. Subscribe to group chat")
    print("     3. Discover chats")
    print("     4. Access insult channel")
    option = int(input())

match option:
  case 1:
    print(option)
  case 2:
    print(option)
  case 3:
    print(option)
  case 4:
    print(option)



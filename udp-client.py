import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

address = '/tmp/udp_client_socket_file'

fake = Faker()
fake_name = fake.name()
fake_address = fake.address()

print('ターミナルからの入力をfakerにやってもらいます。')
print(f"生成された名前：{fake_name}")
print(f"生成されたアドレス：{fake_address}")

message = f"名前：{fake_name}, アドレス：{fake_address}"

try:
    os.unlink(address)
except FileNotFoundError:
    pass
sock.bind(address)

try:
    print('{!r}を送ります。'.format(message))
    sent = sock.sendto(message.encode(), server_address)

    print('応答を待っています。')

    data, server = sock.recvfrom(4096)

    print('{!r}を受け取りました。'.format(message))

finally:
    print('ソケットを閉じます。')
    sock.close()
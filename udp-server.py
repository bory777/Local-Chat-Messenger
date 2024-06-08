import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/udp_socket_file'

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print('{}を起動します。'.format(server_address))
sock.bind(server_address)

while True:
    print('\nメッセージを待っています。')

    data, address = sock.recvfrom(4096)

    print('{}から{}バイト受け取りました。'.format(address, len(data)))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('{}から{}バイト送り返しました。'.format(address, sent))
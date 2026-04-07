import ssl

def execute():
    # rule_key: quantum.arq-q-0245-python
    ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1)

if __name__ == '__main__':
    execute()

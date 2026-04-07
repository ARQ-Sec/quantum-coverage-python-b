import ssl

def execute():
    # rule_key: quantum.arq-q-0270-python
    ssl.SSLContext(ssl.PROTOCOL_TLSv1)

if __name__ == '__main__':
    execute()

from Crypto.Cipher import AES

def execute():
    # rule_key: quantum.arq-q-0252-python
    AES.new(b"0123456789ABCDEF", AES.MODE_ECB)

if __name__ == '__main__':
    execute()

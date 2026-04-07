import ssl

def execute():
    # rule_key: quantum.arq-q-0247-python
    ssl._create_unverified_context()

if __name__ == '__main__':
    execute()

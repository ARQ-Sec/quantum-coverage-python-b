import ssl
import httpx
import aiohttp

def execute():
    # rule_key: quantum.arq-q-0304-python
    client = httpx.Client(verify=False)
    connector = aiohttp.TCPConnector(ssl=False)

if __name__ == '__main__':
    execute()

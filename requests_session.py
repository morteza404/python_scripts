import time
import requests

"""
    The Session object allows you to persist certain parameters across requests. 
    It also persists cookies across all requests made from the Session instance, 
    and will use urllib3‘s connection pooling. 
    So if you’re making several requests to the same host, 
    the underlying TCP connection will be reused, which can result in a significant performance increase
"""

def download(url):
    resp = requests.get(url, timeout=10)
    print(f"len content for {url} is: {len(resp.content)}")

def download_session(url):
    with requests.Session() as session:
        resp = session.get(url, timeout=10)
        print(f"len content for {url} is: {len(resp.content)}")

if __name__ == "__main__":

    start = time.time()
    download("http://burna.ir")
    # download_session("http://olympus.realpython.org/dice")
    end = time.time()
    print(f"duration is : {end-start}")
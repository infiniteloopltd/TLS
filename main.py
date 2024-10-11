import tls_client
import requests
import urllib3

def run():
    session = tls_client.Session(
        client_identifier="chrome_120",
        random_tls_extension_order=True
    )
    page_url = "https://tls.peet.ws/api/all"
    res = session.get(
        page_url
    )
    print(res.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

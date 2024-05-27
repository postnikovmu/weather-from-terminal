import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    api_url_template = 'https://api.vk.ru/method/utils.getShortLink'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'v': '5.236',
        'url': url,
        'private': 0
    }
    api_url = api_url_template
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()

    print(response)
    print(response.text)
    print(response.json())
    short_url = ''
    if response.ok:
        short_url = response.json().get("response").get("short_url")
    return short_url


def main():
    load_dotenv()
    VK_SERVICE_TOKEN = os.environ.get('VK_SERVICE_TOKEN')

    url = 'dvmn.org/modules'

    short_url = shorten_link(VK_SERVICE_TOKEN, url)
    print("short_url:", short_url)


if __name__ == '__main__':
    main()

import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    VK_SERVICE_TOKEN = os.environ.get('VK_SERVICE_TOKEN')
    url_template = 'https://api.vk.ru/method/utils.getServerTime'
    headers = {'Authorization': f'Bearer {VK_SERVICE_TOKEN}'}
    params = {
        'v': '5.236'
    }
    url = url_template
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    print(response)
    print(response.text)

    pass


if __name__ == '__main__':
    main()

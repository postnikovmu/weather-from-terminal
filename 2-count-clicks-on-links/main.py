import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.environ.get('VK_SERVICE_TOKEN'))
    pass


if __name__ == '__main__':
    main()

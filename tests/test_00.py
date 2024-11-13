import requests

from Hillel_AQA_github.configuration import SERVICE_URL


def test_getting_posts():
    response = requests.get(url = SERVICE_URL)
    print(response.json())




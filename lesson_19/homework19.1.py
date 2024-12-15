"""
Є вiдкритий API NASA.

Він дозволяє за певними параметрами отримати данi у виглядi
JSON про фото зробленi ровером “Curiosity” на Марсi. Серед
цих даних є посилання на фото якi потрiбно розпарсити i потiм
за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi
файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно
зробити використовуючи модуль requests
"""


import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params, timeout=10)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    for num, photo in enumerate(photos[:2], start=1):
        image_url = photo['img_src']
        image_response = requests.get(image_url, timeout=10)

        with open(f'mars_photo{num}.jpg', 'wb') as file:
            file.write(image_response.content)

    print('Photos successfully uploaded!')
else:
    print(f'Error: {response.status_code}')

import requests

upload_url = 'http://127.0.0.1:8080/upload'
file_path = 'blacksun.jpg'

with open(file_path, 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(upload_url, files=files, timeout=10)

if response.status_code == 201:
    print('File successfully uploaded!')
    image_url = response.json().get('image_url')
    print(f'Uploaded image URL: {image_url}')
else:
    print(f'Error while uploading file: {response.status_code}')
    exit()

get_url = image_url
headers = {'Content-Type': 'text'}

response = requests.get(get_url, headers=headers, timeout=10)

if response.status_code == 200:
    print(f"File URL: {response.json().get('image_url')}")
else:
    print(f'Error retrieving file: {response.status_code}')
    exit()

delete_url = image_url.replace('uploads/', 'delete/')

response = requests.delete(delete_url, timeout=10)

if response.status_code == 200:
    print('File deleted successfully!')
else:
    print(f'Error deleting file: {response.status_code}')

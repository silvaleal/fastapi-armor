import requests

headers = {
    "Authorization": 'Bearer example_token'
}

try:
    response = requests.post('http://localhost:1500/', headers=headers)

    print(f"Status Code: {response.status_code}")

    print('Response:')

    print(response.json())
except Exception as e:
    print(f"Error: {e}")
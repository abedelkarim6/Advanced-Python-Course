import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(api_url)

print(response.status_code)
print(response.json())

if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")

else:
    print(f"API Call Failed with status code: {response.status_code}")
    print("Response Content:")
    print(response.text)

import httpx

base_url = "https://dummyjson.com/"

content = "products/1"
url = base_url + content
response = httpx.get(url)

print(response.status_code)
content = response.json()
print(content)

content2 = "products?limit=0"
required = "apple"
url2 = base_url + content2
response = httpx.get(url2)
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    products = data.get("products", [])
    
    no_apple = 0
    for product in products:
        if required in str(product):
            no_apple += 1
            print(f"{product['id']}: {product['title']}")
            
print(f"Total matches: {no_apple}")





content3 = "posts/5"
url3 = base_url + content3
response3 = httpx.get(url3)
print(response3.status_code)

if response3.status_code == 200:
    post_data = response3.json()
    likes = post_data["reactions"]["likes"]
    print(f"Post 5 likes: {likes}")



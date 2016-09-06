from urllib.parse import urlparse

url_str="http://images.broadwayworld.com/columnpic/bare181.jpg"
url=urlparse(url_str)
path=url[2]
image_name=path.split("/")[-1]
print(image_name)

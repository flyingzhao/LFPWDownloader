from urllib.parse import urlparse

def get_image_name(url_str):
    url=urlparse(url_str)
    path=url[2]
    image_name=path.split("/")[-1]
    return image_name

if __name__=="__main__":
    image_name=get_image_name("http://images.broadwayworld.com/columnpic/bare181.jpg")
    print(image_name)
from urllib import request 

image_url="http://images.broadwayworld.com/columnpic/bare181.jpg"
path="./images"

req=request.Request(image_url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")
conn=request.urlopen(req)

with open("./images/1.jpg","wb") as f:
    f.write(conn.read())
    f.close()

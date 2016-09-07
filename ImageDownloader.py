from urllib import request 

def image_download(image_url,save_image_name):

    save_path="./images"

    req=request.Request(image_url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")
    
    try:
        conn=request.urlopen(req)
        save_image(save_image_name,conn.read())
        print(image_url+" success ")
    except Exception as e:
        print(image_url+" failure "+str(e))
    
def save_image(save_image_name,content):
    with open("./images/"+save_image_name,"wb") as f:
        f.write(content)

if __name__=="__main__":
    image_download("http://images.broadwayworld.com/columnpic/bare181.jpg","1.jpg")
    image_download("http://www.absolutely.net/wenn/handy_manny_05_wenn5360250.jpg","2.jpg")
    image_download("http://images.broadwayworld.com/columnpic/bare181.jpg","3.jpg")
    image_download("http://www.absolutely.net/wenn/handy_manny_05_wenn5360250.jpg","4.jpg")

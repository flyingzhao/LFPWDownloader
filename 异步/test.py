import asyncio
import sys
import aiohttp


async def image_download(image_url,save_image_full_path):
    with aiohttp.Timeout(10):
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                await save_image(save_image_full_path,await resp.read())

    
async def save_image(save_image_full_path,content):
    with open(save_image_full_path,"wb") as f:
        f.write(content)

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    tasks = [image_download("http://images.broadwayworld.com/columnpic/bare181.jpg","./images/train/1.jpg"),
        image_download("http://www.absolutely.net/wenn/handy_manny_05_wenn5360250.jpg","./images/train/2.jpg"),
        image_download("http://images.broadwayworld.com/columnpic/bare181.jpg","./images/train/3.jpg"),
        image_download("http://www.absolutely.net/wenn/handy_manny_05_wenn5360250.jpg","./images/train/4.jpg")]
        
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


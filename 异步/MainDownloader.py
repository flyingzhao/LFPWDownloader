from urllib.parse import urlparse
import time
import sys
import csv
from multiprocessing import Pool
import aiohttp
import asyncio


class LbfwDownloader:
    def __init__(self,loop,csv_path,save_image_path):
        self.loop=loop
        self.csv_path=csv_path
        self.save_image_path=save_image_path
    
    def __del__(self):
        pass

    def read_csv(self,csv_path):
        url_collection=[]
        with open(csv_path,"r") as csvfile:
            lines=csv.reader(csvfile,delimiter="\t")
            for line in lines:
                url_collection.append(line[0])
        return set(url_collection[2:])

    async def download_and_save(self,image_url):
        image_name=self.get_image_name(image_url)
        await self.image_download(image_url,self.save_image_path+image_name)
        print(image_name+" is done")
        sys.stdout.flush()

    def get_image_name(self,url_str):
        url=urlparse(url_str)
        path=url[2]
        image_name=path.split("/")[-1]
        return image_name

    async def image_download(self,image_url,save_image_full_path):

        header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}

        async with aiohttp.ClientSession() as session:
            async with session.get(image_url,headers=header) as resp:
                try:
                    assert resp.status == 200,"Failure "+str(resp.status)
                    await self.save_image(save_image_full_path,await resp.read())
                    print("success")
                except Exception as e:
                    print(e)
            
    async def save_image(self,save_image_full_path,content):
        with open(save_image_full_path,"wb") as f:
            f.write(content)

    def start_download(self):
        url_list=self.read_csv(self.csv_path)
    
        tasks = [self.download_and_save(u) for u in url_list]
            
        loop.run_until_complete(asyncio.wait(tasks))

        print("Everything is OK")


if __name__=="__main__":
    
    t=time.time()
    loop = asyncio.get_event_loop()

    train=LbfwDownloader(loop,"./url/kbvt_lfpw_v1_train.csv","./images/train/")
    train.start_download()
    print("time: "+str(time.time()-t))
    
    t=time.time()
    test=LbfwDownloader(loop,"./url/kbvt_lfpw_v1_test.csv","./images/test/")
    test.start_download()
    print("time: "+str(time.time()-t))

    loop.close()


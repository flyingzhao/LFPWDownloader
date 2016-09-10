from ReadCSV import readcsv
from URLParser import get_image_name
from ImageDownloader import image_download
import time
import sys
from multiprocessing import Pool

import asyncio

def main_downloader(loop,csv_path,save_image_path):
    url_list=readcsv(csv_path)
    
    
    tasks = [download_and_save(u,save_image_path) for u in url_list]
        
    loop.run_until_complete(asyncio.wait(tasks))

    print("Everything is OK")


def download_one_url(image_url,save_image_path):
    print("start download "+image_url)
    download_and_save(image_url,save_image_path)
    sys.stdout.flush()
        
async def download_and_save(image_url,save_image_path):
    image_name=get_image_name(image_url)
    await image_download(image_url,save_image_path+image_name)
    print(image_name+" is done")
    sys.stdout.flush()

if __name__=="__main__":
    
    # t=time.time()
    loop = asyncio.get_event_loop()
    # main_downloader(loop,"./url/kbvt_lfpw_v1_train.csv","./images/train/")
    # print("time: "+str(time.time()-t))
    
    t=time.time()
    main_downloader(loop,"./url/kbvt_lfpw_v1_test.csv","./images/test/")
    print("time: "+str(time.time()-t))

    loop.close()


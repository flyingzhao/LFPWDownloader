from ReadCSV import readcsv
from URLParser import get_image_name
from ImageDownloader import image_download
import time
import sys
from multiprocessing import Pool

def main_downloader(csv_path,save_image_path):
    url_list=readcsv(csv_path)

    progress_count=1
    image_number=len(url_list)

    p=Pool(8)

    for image_url in url_list:
        p.apply_async(download_one_url,args=(image_url,save_image_path))
        # download_one_url(image_url,save_image_path)
    p.close()
    p.join()
    print("Everything is OK")


def download_one_url(image_url,save_image_path):
    print("start download "+image_url)
    download_and_save(image_url,save_image_path)
    # progress=progress_count/image_number
    # print("Current count is {} progress is {:.2f}%".format(progress_count,progress*100))
    # progress_count+=1
    sys.stdout.flush()

        
def download_and_save(image_url,save_image_path):
    image_name=get_image_name(image_url)
    image_download(image_url,save_image_path+image_name)
    print(image_name+" is done")

if __name__=="__main__":
    t=time.time()
    main_downloader("./url/kbvt_lfpw_v1_train.csv","./images/train/")
    print("time: "+str(time.time()-t))
    sys.stdout.flush()
    
    t=time.time()
    main_downloader("./url/kbvt_lfpw_v1_test.csv","./images/test/")
    print("time: "+str(time.time()-t))
    sys.stdout.flush()


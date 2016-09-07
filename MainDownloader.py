from ReadCSV import readcsv
from URLParser import get_image_name
from ImageDownloader import image_download
import time

def main_downloader():
    url_list=readcsv("./url/kbvt_lfpw_v1_train.csv")
    for image_url in url_list:
        print("start download "+image_url)
        t=time.time()
        download_and_save(image_url)
        print("time: "+str(time.time()-t))
        
def download_and_save(image_url):
    image_name=get_image_name(image_url)
    image_download(image_url,image_name)
    print(image_name+"is done")

if __name__=="__main__":
    main_downloader()


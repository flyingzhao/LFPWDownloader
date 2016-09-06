from ReadCSV import readcsv
from URLParser import get_image_name
from ImageDownloader import image_download

url_list=readcsv("./url/kbvt_lfpw_v1_train.csv")
for image_url in url_list:
    print(image_url)
    image_name=get_image_name(image_url)
    image_download(image_url,image_name)
    print(image_name+"is done")


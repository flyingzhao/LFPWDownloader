import csv

def readcsv(csv_path):
    url_collection=[]
    with open(csv_path,"r") as csvfile:
        lines=csv.reader(csvfile,delimiter="\t")
        for line in lines:
            url_collection.append(line[0])

    return url_collection[2:]

if __name__=="__main__":
    col=readcsv("./url/kbvt_lfpw_v1_train.csv")
    print(len(col))
    
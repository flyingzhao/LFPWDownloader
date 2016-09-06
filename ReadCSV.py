import csv

url_collection=[]
with open("./url/kbvt_lfpw_v1_train.csv","r") as csvfile:
    lines=csv.reader(csvfile,delimiter="\t")
    for line in lines:
        url_collection.append(line[0])

print(url_collection[2:])

    
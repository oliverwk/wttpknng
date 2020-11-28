import requests, re
i = 0
list = ["/globalassets/nakd_cut_out_lace_bodysuit_1013-000492-0002_01j.jpg?ref=5C428B61E1","/globalassets/nakd_cut_out_lace_bodysuit_1013-000492-0002_02k.jpg?ref=ED7413B9D5","/globalassets/nakd_cut_out_lace_bodysuit_1013-000492-0002_03a.jpg?ref=7B8B7361C2","/globalassets/nakd_cut_out_lace_bodysuit_1013-000492-0002_04c.jpg?ref=F115483C22"]
for item in list:
    print(item)
    fiel = requests.get("https://www.na-kd.com/resize"+item.split("?")[0])
    name = re.sub(r'[0-9]+', '',item.split("/")[2].split("-")[0].replace("_","-")).strip("nakd-")+"-"
    id = str(i)
    id = item.split(".jpg")[0].split("_")[len(item.split(".jpg")[0].split("_"))-1]
    print("Name: "+name+id)
    file = open("/Users/MWK/Desktop/nkd/tmp/"+name+id+".png","wb")
    file.write(fiel.content)
    file.close()
    i += 1

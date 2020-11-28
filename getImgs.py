import requests, json, wget, os
print(os.listdir())
file = open("Lingerie.json","r")
inhoud = file.read()
file.close()
jsons = json.loads(inhoud)
si = 0
error = 0
for i in jsons:
    error = 0
    img_url = i["img_url_sec"]
    print(img_url)
    response = requests.get(img_url)
    if response.status_code != 200:
            print("Didn't found it with status code: "+str(response.status_code))
            if error==0:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02i"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","02i")

            if error==1:
                print("Didn't find the image the: "+str(error)+" time.")
                if "_4_" in img_url:
                  response = requests.get(img_url.replace("_4_","_3_"))
                  if response.status_code != 200:
                      error += 1
                  else:
                      jsons[si]["img_url_sec"] = img_url.replace("_4_","_2_")

                elif "_1__1" in img_url:
                    response = requests.get(img_url.replace("_1__1","_4_"))
                    if response.status_code != 200:
                        error += 1
                    else:
                        jsons[si]["img_url_sec"] = img_url.replace("_1__1","_4_")

                else:
                    response = requests.get(img_url.replace("_4_","_2_"))
                    if response.status_code != 200:
                        error += 1
                    else:
                        jsons[si]["img_url_sec"] = img_url.replace("_4_","_2_")


            if error==2:
                print("Didn't find the image the: "+str(error)+" time.")
                if "-1" in img_url:
                    print("Er zit een -1 in dat beteknd waarschijnlijk dat het dubbel is dus kan je dat weg laten zo als je hier kan zien: "+img_url.replace("-1",""))
                    response = requests.get(img_url.replace("-1",""))
                    if response.status_code != 200:
                        error += 1
                    else:
                        jsons[si]["img_url_sec"] = img_url.replace("-1", "")

            else:
                response = requests.get(img_url.replace("04k","03h"))
                if response.status_code != 200:
                    error += 1
                else:
                   jsons[si]["img_url_sec"] = img_url.replace("04k","03h")


            if error==3:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02b"))
                if response.status_code != 200:
                     error += 1
                else:
                     jsons[si]["img_url_sec"] = img_url.replace("04k","02b")

            if error==4:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","05g"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","05g")

            if error==5:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","03k"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","03k")

            if error==6:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02k"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","02k")

            if error==7:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02m"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","02m")

            if error==8:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02b"))
                if response.status_code != 200:
                   error += 1
                else:
                   jsons[si]["img_url_sec"] = img_url.replace("04k","02b")

            if error==9:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","02k_r1"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","02k_r1")

            if error==10:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","04b"))
                if response.status_code != 200:
                     error += 1
                else:
                     jsons[si]["img_url_sec"] = img_url.replace("04k","04b")

            if error==11:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","04k_r1"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","04k_r1")

            if error==12:
                print("Didn't find the image the: "+str(error)+" time.")
                response = requests.get(img_url.replace("04k","01j"))
                if response.status_code != 200:
                    error += 1
                else:
                    jsons[si]["img_url_sec"] = img_url.replace("04k","01j")

    else:
        print("Found it with status code: "+str(response.status_code))

    si += 1

files = open("Lingerie.json","w")
print(json.dumps(jsons, indent=4))
files.writelines(json.dumps(jsons, indent=4))
files.close()

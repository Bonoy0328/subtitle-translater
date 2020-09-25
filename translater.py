# 翻译当前目录下所有srt文件，并在当前目录新建文件夹subtile_Translaed,保存所有翻译过的字幕文件，支持百度API和搜狗API
import http.client
import hashlib
import urllib
import random
import json
import time
import os

appid = '***************'  # 填写你的appid
secretKey = '****************'  # 填写你的密钥
# QPS = 1 #填写你的QPS

#打开当前目录下所有srt文件
srtFile = []
for i in range(len(os.listdir("."))):
    if (os.listdir(".")[i][-3:] == "srt"):
        srtFile.append(os.listdir(".")[i])
fileCount = len(srtFile)
for j in range(fileCount):
    #读取字幕文件，并提取其中的英语句子，保存到subtitleContent列表中
    with open(srtFile[j],encoding="utf-8") as file:
        srt = file.read()
    subtitle = srt.split("\n")
    subtitleContent = []
    for i in range(int(len(subtitle)/4)):
        subtitleContent.append(subtitle[2+i*4])
    ##############################################
    trsCount = len(subtitleContent)
    #调用百度翻译API
    trsResult = []
    for i in range(trsCount):
        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'en'   #原文语种
        toLang = 'zh'   #译文语种
        salt = random.randint(32768, 65536)
        q= subtitleContent[i]
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
        while True:
            try:
                httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
                httpClient.request('GET', myurl)

                # response是HTTPResponse对象
                response = httpClient.getresponse()
                result_all = response.read().decode("utf-8")
                result = json.loads(result_all)

                # print(q)
                # print (result["trans_result"][0]["dst"].replace("搅拌机","Blender"))
                if (len(result)==3):
                    trsResult.append(result["trans_result"][0]["dst"].replace("搅拌机","Blender"))
                    break
            except Exception as e:
                if (len(result)==3):
                    break
                print (e)
            finally:
                if (len(result)==3):
                    break
                if httpClient:
                    httpClient.close()
            time.sleep(0.1)
        tipStr = "正在翻译第" + str(j+1) + "/" + str(fileCount+1) + "个文件的第" + str(i+1) + "/" + str(trsCount + 1) + "句话"
        os.system("cls")
        print(tipStr)
    ###########################################################
    #拼接翻译结果，并保存为新的SRT文件
    finalResult = ""
    for i in range(len(subtitle)):
        
        if(subtitle[i] == ""):
            finalResult += "\n\n"
        else:
            finalResult += subtitle[i] + "\n"
        if (i - 2)%4 == 0:
            finalResult += trsResult[int((i - 2)/4)]
    # for i in range(len(subtitleContent)):
    #     print(subtitleContent[i])
    #     print(trsResult[i])
    if not os.path.exists(".\subtile_Translaed"):
        os.makedirs(".\subtile_Translaed")
    with open(".\subtile_Translaed\\" + srtFile[j],"w",encoding="utf-8") as f:
        f.write(finalResult)
    file.close()
    f.close()
    ##########################################

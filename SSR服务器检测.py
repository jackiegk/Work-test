#encoding=utf-8

import simplejson
import urllib.request
import requests
import time
def main():
    ## 补全ssrstatus的json地址····
    url = ''

    ## 获得当前时间
    time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time1)

    total_message = ""
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = response.read()

    json_info = simplejson.loads(result)
    length = len(json_info["servers"])

    for item in range(0, length):
        status1 = json_info["servers"][item]["status"]
        if status1 == False :
            name_value =  json_info["servers"][item]["name"]
            time_value = json_info["servers"][item]["time"]
            status_value = json_info["servers"][item]["status"]
            total_message = total_message + \
                            "\n* 名称: " + name_value + \
                            "\n* 状态: " + str(status_value) + \
                            "\n* time: " + time_value + \
                            "\n "
        else:
            continue  # continue跳出本次循环，break跳出整个for循环
    if total_message :
        print("服务器有错误，马上报告主人")
        payload = {'text': "SSR服务器故障", 'desp': "\n* 服务器时间" + time1 + "\n" + total_message}
        requests.get('http://sc.ftqq.com/[此处填自己的Key].send', params=payload)
    else:
        print("服务器正常，不需要发消息")

if __name__ == "__main__":
    main()

import datetime
import requests
import json
def weixintuisong(yonghu,tuisongwenben):
    corpid = ''
    corpsecret = ''
    res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+corpid+'&corpsecret='+corpsecret)  # get提交
    return1 = json.loads(res.text)  # json解析返回值
    wxtoken = return1['access_token']
    wx_data = {"touser": yonghu,
    "msgtype": "text",
    "agentid": "1000002",
    "text": {
        "content": '【奕辅导】\n'+tuisongwenben}}
    res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+wxtoken,data=json.dumps(wx_data))  # get提交

#自己token
accessToken = ''

#现行时间
t = datetime.datetime.now()
t = '【'+ str(t) +'】'
#获取打卡id开始(id里面有时间戳)GET访问
url = 'https://yfd.ly-sky.com/ly-pd-mb/form/api/healthCheckIn/client/stu/index'
header = {
    "accessToken": accessToken,
    "userAuthType": "MS"
}
res = requests.get(url,headers=header)#get提交
print(t + res.text)#返回文本型返回值
return1 = json.loads(res.text)#json解析返回值
if return1['code'] == 200:#json解析出code=200判断是否打卡
    dakaxinxi = dict.get(return1, "data")
    dakaid = dict.get(dakaxinxi, "questionnairePublishEntityId")
    print(t + '获取成功|'+ dakaid)
else:
    print(t + '获取失败|'+ return1['message'])
    weixintuisong('crush', '获取失败|'+ return1['message'])
#获取打卡id结束
#开始提交数据 POST提交表单
url = 'https://yfd.ly-sky.com/ly-pd-mb/form/api/answerSheet/saveNormal'
data = {
    "questionnairePublishEntityId": dakaid,
    "answerInfoList": [{
        "subjectId": "1001640315554537000980000000001",
        "subjectType": "multiSelect",
        "multiSelect": {
            "optionAnswerList": [{
                "beSelectValue": "NotThing",
                "fillContent": ""
            }]
        }
    }, {
        #重要部分，经纬度/地名
        "subjectId": "1001640315554577000980000000001",
        "subjectType": "location",
        "location": {
            "deviationDistance": 10045,
            "locationRangeId": "1001640054768198000150000000001",
            "address": "广东省佛山市三水区云东海街道学海中路1号",
            "city": "佛山市",
            "province": "广东省",
            "area": "三水区",
            "latitude": 23.212008,
            "longitude": 112.862628
        }
    }, {
        "subjectId": "1001640743741123000960000000001",
        "subjectType": "signleSelect",
        "signleSelect": {
            "beSelectValue": "flag1640743720931",
            "fillContent": ""
        }
    }, {
        "subjectId": "1001640743758116001000000000001",
        "subjectType": "signleSelect",
        "signleSelect": {
            "beSelectValue": "2",
            "fillContent": ""
        }
    }, {
        "subjectId": "1001640743801628001000000000001",
        "subjectType": "simpleFill",
        "simpleFill": {
            "inputContent": "无",
            "imgList": []
        }
    }, {
        "subjectId": "1001640743816621000960000000001",
        "subjectType": "simpleFill",
        "simpleFill": {
            "inputContent": "无",
            "imgList": []
        }
    }, {
        "subjectId": "1001640743859737000980000000001",
        "subjectType": "signleSelect",
        "signleSelect": {
            "beSelectValue": "1",
            "fillContent": ""
        }
    }, {
        "subjectId": "1001640956029680001500000000001",
        "subjectType": "signleSelect",
        "signleSelect": {
            "beSelectValue": "flag1640955958618",
            "fillContent": ""
        }
    }]
}
data = json.dumps(data)#提交数据是json格式
header = {
    "Host": "yfd.ly-sky.com",
    "Connection": "keep-alive",
    "Content-Length": "1373",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "accessToken": accessToken,
    "content-type": "application/json",
    "userAuthType": "MS",
    "Referer": "https://servicewechat.com/wx217628c7eb8ec43c/20/page-frame.html"
}
res = requests.post(url,data,headers=header)#post提交
res.encoding = 'utf-8'#utf—8编码
print(t + res.text)#返回文本型返回值
return1 = json.loads(res.text)#json解析返回值
xinxi = return1['message']
if return1['code'] == 200:#json解析出code=200判断是否打卡
    print(t + '打卡成功')
    weixintuisong('crush', '打卡成功')
else:
    print(t + '打卡失败|'+xinxi)
    weixintuisong('crush', '打卡失败|'+xinxi)
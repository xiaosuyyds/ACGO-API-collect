# encoding=utf8
import json,random
import requests,time,os

def get_inform(url):
    url = url
    req = requests.get(url)
    return json.loads(req.text)

def try_uid(uid):
    url = 'https://gateway.acgo.cn/acgoAccount/openapi/user/detail?uid=%d'%(uid)
    req=get_inform(url)
    if req["code"]==200:
        return [True,req["data"]]
    else:
        return [False,req["data"]]

try:
    driect_file_path = os.path.abspath(__file__)
    foward_file_path = os.path.dirname(driect_file_path)
    work_path=os.path.join(foward_file_path,"uid.txt")
    f=open(work_path,"r",encoding='utf-8')
    tryuids=eval(f.read())
    f.close()
except:
    tryuids=[]
try:
    driect_file_path = os.path.abspath(__file__)
    foward_file_path = os.path.dirname(driect_file_path)
    work_path=os.path.join(foward_file_path,"max_try_uids.txt")
    f=open(work_path,"r",encoding='utf-8')
    uid=int(f.read())
    f.close()
except:
    uid=0

while True:
    uid+=1
    driect_file_path = os.path.abspath(__file__)
    foward_file_path = os.path.dirname(driect_file_path)
    work_path=os.path.join(foward_file_path,"max_try_uids.txt")
    req=try_uid(uid)
    f=open(work_path,"w",encoding='utf-8')
    f.write(str(uid))
    f.close()
    
    if req[0]:
        print("爬取成功！")
        print("用户名:",req[1]["nickName"])
        print("UID:",req[1]["uid"])
        if(req[1]["autograph"]!="love acgo"):
            print("个性签名:",req[1]["autograph"])
        if(req[1]["avatar"]!="https://attach.acgo.cn/picture/default.png"):
            print("头像:",req[1]["avatar"])
        print("关注人数:",req[1]["followNumber"])
        print("粉丝人数:",req[1]["fanNumber"])
        print("注册时间:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(req[1]["registerTime"])))
        if(req[1]["sex"]==1):
            print("性别: 男")
        elif(req[1]["sex"]==2):
            print("性别: 女")
        if(req[1]["birthday"]!=0):
            print("生日:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(req[1]["birthday"])))
        if(req[1]["school"]!=None):
            print("学校:",req[1]["school"])
        if(req[1]["city"]!=None):
            print("城市:",req[1]["city"])
        print("用户排名分数:",req[1]["userRankScore"])
        print("是否创建团队:",req[1]["isCreateTeam"])
        print("\n无用/不明作用の信息：")
        print("荣誉:",req[1]["honorary"])
        print("关注状态:",req[1]["followStatus"])
        print("blockStatus:",req[1]["blockStatus"])
        print("排名编号:",req[1]["rankId"])
        
        print()
        print()
        print()
        tryuids.append(req)
        driect_file_path = os.path.abspath(__file__)
        foward_file_path = os.path.dirname(driect_file_path)
        work_path=os.path.join(foward_file_path,"uid.txt")
        f=open(work_path,"w",encoding='utf-8')
        f.write(str(tryuids))
        f.close()
        # time.sleep(1)
    # else:
    #     print("爬取失败！")/
    #     if(req[1]==None):
    #         print(uid,"用户不存在！")
    #     else:
    #         print("未知错误，错误信息：",req[1])
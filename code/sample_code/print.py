import time

user_list=[]
file="C:\\Users\\DN\\Desktop\\Program\\Project\\ACGO_API_collect\\ACGO-API-collect\\code\\sample_code\\uid.txt"
f=open(file, "r", encoding="utf-8", errors='ignore')
user_list=eval(f.read())
f.close()
print("截至2023-9-13 ACGO共有",len(user_list),"名用户")

man=[]
woman=[]
no_sex=[]
birthday=[]
no_birthday=[]

for i in range(len(user_list)):
    user=user_list[i]
#     print("用户名:",user[1]["nickName"])
#     print("UID:",user[1]["uid"])
#     if(user[1]["autograph"]!="love acgo"):
#         print("个性签名:",user[1]["autograph"])
#     if(user[1]["avatar"]!="https://attach.acgo.cn/picture/default.png"):
#         print("头像:",user[1]["avatar"])
#     print("关注人数:",user[1]["followNumber"])
#     print("粉丝人数:",user[1]["fanNumber"])
#     print("注册时间:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user[1]["registerTime"])))
#     if(user[1]["sex"]==1):
#         print("性别: 男")
#     elif(user[1]["sex"]==2):
#         print("性别: 女")
#     if(user[1]["birthday"]!=0):
#         print("生日:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user[1]["birthday"])))
#     if(user[1]["school"]!=None):
#         print("学校:",user[1]["school"])
#     if(user[1]["city"]!=None):
#         print("城市:",user[1]["city"])
#     print("用户排名分数:",user[1]["userRankScore"])
#     print("是否创建团队:",user[1]["isCreateTeam"])
#     print("\n无用/不明作用の信息：")
#     print("荣誉:",user[1]["honorary"])
#     print("关注状态:",user[1]["followStatus"])
#     print("blockStatus:",user[1]["blockStatus"])
#     print("排名编号:",user[1]["rankId"])
#     print("-------\n")
    # print("\n"*33)

    
    if(user[1]["sex"]!=0):
        if(user[1]["sex"]==1):
            man.append(user)
        elif(user[1]["sex"]==2):
            woman.append(user)
    else:
        no_sex.append(user)

    if(user[1]["birthday"]!=0):
        birthday.append(user)
    else:
        no_birthday.append(user)

    if("知予" in user[1]["nickName"]):
        print("用户名:",user[1]["nickName"])
        print("UID:",user[1]["uid"])
        if(user[1]["autograph"]!="love acgo"):
            print("个性签名:",user[1]["autograph"])
        if(user[1]["avatar"]!="https://attach.acgo.cn/picture/default.png"):
            print("头像:",user[1]["avatar"])
        print("关注人数:",user[1]["followNumber"])
        print("粉丝人数:",user[1]["fanNumber"])
        print("注册时间:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user[1]["registerTime"])))
        if(user[1]["sex"]==1):
            print("性别: 男")
        elif(user[1]["sex"]==2):
            print("性别: 女")
        if(user[1]["birthday"]!=0):
            print("生日:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user[1]["birthday"])))
        if(user[1]["school"]!=None):
            print("学校:",user[1]["school"])
        if(user[1]["city"]!=None):
            print("城市:",user[1]["city"])
        print("用户排名分数:",user[1]["userRankScore"])
        print("是否创建团队:",user[1]["isCreateTeam"])
        print("\n无用/不明作用の信息：")
        print("荣誉:",user[1]["honorary"])
        print("关注状态:",user[1]["followStatus"])
        print("blockStatus:",user[1]["blockStatus"])
        print("排名编号:",user[1]["rankId"])
        print("-------")

print("男（仅已被记录）:",len(man))
print("女（仅已被记录）:",len(woman))
print("未记录:",len(no_sex))
print()
print("男生占所有用户的比例:",len(man)/len(user_list)*100,"%")
print("女比占所有用户的比例:",len(woman)/len(user_list)*100,"%")
print()
print("男生占所有已记录用户的比例:",len(man)/(len(man)+len(woman))*100,"%")
print("女比占所有已记录用户的比例:",len(woman)/(len(man)+len(woman))*100,"%")
print()
print("有生日记录的是:",len(birthday))
print("无生日记录的是:",len(no_birthday))
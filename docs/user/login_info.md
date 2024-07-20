# 获取当前登录账号信息

> <https://gateway.acgo.cn/acgoAccount/openapi/user/info>

*请求方式：GET*

*鉴权方式：Access-Token*

*认证方式：Cookie(user-token)*

**Http请求头：**

| 参数名          | 类型  | 内容                 | 必要性 | 备注                                   |
|--------------|-----|--------------------|-----|--------------------------------------|
| Access-Token | str | Access-Token       | 必要  | 详情见[登陆账号](../user/login_password.md) |

**返回值：**

根对象：

| 字段        | 类型  | 内容         | 备注     |
|-----------|-----|------------|--------|
| code      | num | 返回值        | 200：成功 |
| message   | str | 错误信息       | ok     |
| data      | obj | 信息本体       |        |
| timestamp | num | 当前的Unix时间戳 |        |

data对象：

| uid          | num  | 用户ID    |                                       |
|--------------|------|---------|---------------------------------------|
| blockStatus  | num  | 封号状态    | 未封号为1                                 |
| nickName     | str  | 用户昵称    |                                       |
| avatar       | str  | 用户头像URL |                                       |
| sex          | num  | 用户性别    | 0：未知 1：男 2：女                          |
| birthday     | num  | 用户生日    | Unix时间戳，0为未知                          |
| registerTime | num  | 注册时间    | Unix时间戳                               |
| school       | 未知   | 学校（?）   | null：未知<br />暂未发现有`school`字段的用户       |
| city         | 未知   | 城市（?）   | null：未知<br />暂未发现有`city`字段的用户         |
| autograph    | str  | 个性签名    |                                       |
| followNumber | num  | 关注人数    |                                       |
| fanNumber    | num  | 粉丝人数    |                                       |
| honorary     | 未知   | 荣誉（？）   | 未知                                    |
| rankRing     | 未知   | 未知      | 未知                                    |
| rankId       | 未知   | 未知      | 未知                                    |
| userRankVo   | obj  | 排名信息    |                                       |
| isCreateTeam | bool | 是否创建团队  | true：已创建<br />false：未创建<br />默认为false |

`data`中的`userRankVo`对象：

| 字段            | 类型  | 内容    | 备注               |
|---------------|-----|-------|------------------|
| userRankScore | num | 用户排位分 | 可通过排位赛获得         |
| honorary      | str | 荣誉    |                  |
| rankRing      | num | 用户排名  | 用户排名，若为200则不计入排名 |
| rankId        | num | 排名id  | 默认为1             |

<details>
<summary>查看响应示例：</summary>
  
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "uid": 3131901,
        "blockStatus": 1,
        "nickName": "米哈游miHoYo",
        "avatar": "https://attach.acgo.cn/picture/d5668eb7784b4debb441e396d555d383.png",
        "sex": 0,
        "birthday": 0,
        "registerTime": 1688036953,
        "school": null,
        "city": null,
        "autograph": "技术宅拯救世界",
        "followNumber": 31,
        "fanNumber": 94,
        "followStatus": null,
        "userRankScore": 12,
        "honorary": null,
        "rankRing": null,
        "rankId": null,
        "userRankVo": {
            "userRankScore": 12,
            "honorary": "倔强青铜",
            "rankRing": null,
            "rankId": 1
        },
        "isCreateTeam": true,
        "remainCreateTeamNum": 0
    },
    "timestamp": 1721504230
}
```
# 用户登陆

> <https://gateway.acgo.cn/acgoAccount/openapi/oauth/loginByPassword>
---
> Csrf-Token暂未逆向，建议尝试[这个方法](../../docs/sgin/access-token.md)

*请求方式：POST*
*鉴权方式：Csrf-Token、`__request_client_time__`*

**POST请求体：**

| 参数名                       | 类型  | 内容       | 必要性   | 备注                 |
|---------------------------|-----|----------|-------|--------------------|
| appid                     | str | appID(?) | 必要    | 默认为xmw537127780164 |
| mobile                    | str | 用户绑定手机号  | 必要    |                    |
| password                  | str | 用户密码     | 必要    | 被加密，加密方法暂未知        |
| timestamp                 | int | 时间戳      | 必要    | 请求Unix时间戳（整数）      |
| `__request_client_time__` | int | (?)      | 必要(?) | 未知字段               |


**Http请求头：**

| 参数名          | 类型  | 内容           | 必要性 | 备注                 |
|--------------|-----|--------------|-----|--------------------|
| Csrf-Token   | str | Csrf-Token   | 必要  | 未知的鉴权方式，待逆向        |
| Content-Type | str | Content-Type | 必要  | "application/json" |
| Fp2          | str | (?)          | 必要? | (?)                |


**json回复：**

| 字段        | 类型  | 内容      | 备注                                |
|-----------|-----|---------|-----------------------------------|
| code      | num | 返回值     | 0：成功<br />500：参数或登陆密码/账号错误（如注销账号） |
| message   | str | 错误信息    | 默认为success                        |
| data      | obj | 信息本体    |                                   |
| timestamp | num | Unix时间戳 | 当前的Unix时间戳                        |

`data`对象：

| 字段           | 类型   | 内容           | 备注                        |
|--------------|------|--------------|---------------------------|
| accessToken  | str  | Access-Token | Access-Token              |
| areaCode     | str  | 地区码(?)       | 默认为"0"                    |
| avatarImg    | str  | 头像图片链接       | 图片链接                      |
| birthday     | str  | 生日           | 生日                        |
| citycode     | str  | 城市码(?)       | 默认为"0"                    |
| expiresIn    | int  | 过期时间(?)      | 单位为秒，Access-Token的过期时间(?) |
| nickname     | str  | 昵称           | 昵称                        |
| phone        | str  | 手机号          | 用户绑定手机号                   |
| provinceCode | str  | 省份码(?)       | 默认为"0"                    |
| pwdSet       | bool | 是否设置密码       | 是否设置密码                    |
| schoolId     | str  | 学校ID(?)      | 用户所在学校ID(?)，默认为"0"        |
| userId       | int  | 用户ID         | 用户ID                      |
| xmschoolId   | int  | (?)          | (?)                       |


**本API暂无示例，因为涉及到过多隐私信息！**
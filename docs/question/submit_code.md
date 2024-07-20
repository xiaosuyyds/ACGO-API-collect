# 提交代码

> <https://gateway.acgo.cn/acgoPms/question-answer-record/submit>

*请求方式：POST*

*鉴权方式：Access-Token*

*认证方式：Cookie(user-token)*

*请求同步性：同步异步均可，建议使用同步提交*


**POST请求体：**

| 参数名                  | 类型  | 内容                        | 必要性 | 备注                           |
|----------------------|-----|---------------------------|-----|------------------------------|
| answer               | obj | 数组索引为0需要为一个字符串，代表用户提交的代码。 | 必要  | 其他索引请务必不要填写任何东西。             |
| pmsQuestionVersionId | str | 题目版本编号                    | 必要  | 可以是任何的值，参考1020788。目前不确定有什么用处 |
| questionId           | str | 要提交的题目编号                  | 必要  | 参考："1"                       |
| language             | num | 提交的代码语言编号                 | 必要  | c++:2，python:4               |

**Http请求头：**

| 参数名          | 类型  | 内容                 | 必要性 | 备注                                   |
|--------------|-----|--------------------|-----|--------------------------------------|
| Access-Token | str | Access-Token       | 必要  | 详情见[登陆账号](../user/login_password.md) |
| Content-Type | str | "application/json" | 必要  | 按照内容直接填写即可，不需要做出任何改变。                |

**json响应：**

根对象：

| 字段        | 类型  | 内容         | 备注     |
|-----------|-----|------------|--------|
| code      | num | 返回值        | 200：成功 |
| message   | str | 错误信息       | ok     |
| data      | obj | 信息本体       |        |
| timestamp | num | 当前的Unix时间戳 |        |

`data`对象：

| 字段             | 类型  | 内容           | 备注                        |
|----------------|-----|--------------|---------------------------|
| compileError   | str | 编译失败报错信息     |                           |
| id             | num | 提交用户的个人id    |                           |
| initialCode    | (?) | (?)          |                           |
| judgeMode      | (?) | (?)          | 也许后面会推出special judge和交互式。 |
| list           | (?) | (?)          |                           |
| ojSubmissionId | num | 提交记录编号       | 可以通过提交记录来获得每一个测试点的具体信息    |
| status         | (?) | (?)          |                           |
| language       | num | 提交的代码语言编号(?) | 此字典似乎一直是null              |
| name           | (?) | (?)          | 此字典似乎一直是null              |
| createdAt      | (?) | (?)          | 此字典似乎一直是null              |
| maxCpuTime     | (?) | (?)          | 此字典似乎一直是null              | 
| maxUsedMemory  | (?) | (?)          | 此字典似乎一直是null              |

**示例：**
提交题目`questionID=1`的详细信息
```python
import requests

def submit_code():
    url = "https://gateway.acgo.cn/acgoPms/question-answer-record/submit"
    access_token = "参考登陆api。"
    headers = {
        "Access-Token": access_token,
        "Content-Type": "application/json"
    }
    data = {
        "answer": ["""// A+B

#include <iostream>
nusing namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    long sum = a+b;
    cout << sum << endl;
    return 0;
}"""],
        "pmsQuestionVersionId": "1020789",
        "questionId": "1",
        "language": 2
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)

submit_code()
```

<details>
<summary>查看响应示例：</summary>
  
```json
{
    "code": 200,
    "message": "ok",
    "data": {
        "id": 923404,
        "initialCode": null,
        "list": null,
        "compileError": null,
        "judgeMode": null,
        "status": null,
        "ojSubmissionId": "4988105085857824865",
        "language": null,
        "name": null,
        "createdAt": null,
        "maxCpuTime": null,
        "maxUsedMemory": null
    },
    "timestamp": 1721505524
}
```

</details>

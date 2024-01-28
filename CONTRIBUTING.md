# ACGO-API-coliect贡献指南

欢迎来到 ACGO-API-coliect 社区贡献指南，本文主要面向需要进行提交贡献文档内容的用户。

## 总则

[ACGO-API-coliect](https://github.com/xiaosuyyds/ACGO-API-collect/ACGO-API-coliect) 项目是一个仅用于学习研究、社区开源、公益性质的 [ACGO](https://www.acgo.cn/) API（应用程序接口） 文档，使用 [CC-BY-NC 4.0 协议](https://github.com/xiaosuyyds/ACGO-API-coliect/blob/master/LICENSE) 开源，它将无差别收集整理相关的**主站业务接口**。

该项目使用 [MarkDown](https://zh.wikipedia.org/zh-cn/Markdown) 语法进行文档书写，按照业务类型及功能以 **路径** + **文件** 形式索引，任何用户都可通过 Pull Request 提供自己分析出的接口地址与使用说明。

本项目收集的接口类型包括但不限于 REST API、gRPC、WebSocket，文档内统一优先使用安全套接字协议，如`https`、`securityRpc`、`wss`。

## 目录与路径结构

### 目录

文档目录以 **Markdown无序列表** 语法写在 [README.md](README.md) 中，使用缩进标识文档的层级，如`用户`下存在`基本信息`、`当前登陆账号的信息`、`登陆账号`等子分类，使用 **Markdown 复选框** 语法该标注文档是否编写完成

```markdown
- [x] 用户
  - [x] 用户信息
  - [ ] 当前登陆账号的信息
  - [ ] 登陆账号
```

### 路径

路径层级应当与文档目录一致，以文件夹的形式存放在项目中的`/docs`路径下，命名统一使用英文，如`video`、`danmaku`、`comment`

二级、三级路径应当存在二级三级目录，以`README.md`的形式

## Markdown文档内容格式

注：文档范式可根据**实际情况**进行调整

### 接口说明

文档中可存在多个接口说明，应当遵守同一范式，依次排列在文档中

接口说明分为`标题`、`地址`、`说明`、`请求参数`、`响应正文`、`示例`这些部分

接口标题为 **二级以下** 的标签，接口地址使用 **引用** 语法，地址只保留 REST API 路径，不应携带 query 等内容

接口地址下方需要注明接口的请求方式，如`GET`、`POST`、`PUT`等，使用 **斜体** 语法

若接口存在认证或鉴权，需要在说明中注明，如`Cookie`（认证是针对用户的，鉴权是针对接口使用的

其他使用说明也可写在这里，如`限制游客访问的信息需要登录`

请求参数应当使用 **表格** 语法，第一列为参数名，第二列为参数类型，第三列为参数说明，第四列为是否必选，第五列为默认值

响应正文应当使用 **表格** 语法，第一列为参数名，第二列为参数类型，第三列为参数说明

示例应当使用 **代码块** 语法，使用`json`语法格式化输出

### 枚举值与属性位

接口返回或请求中若存在一些 enum 类型或二进制属性位，应当单独进行探讨。

这些值及其说明使用 **表格** 进行整理，表头统一为`位` / `代码` / `值`、`含义`、`备注`

这些枚举值或属性位的用法应附加文字说明

## 文档提交

TODO

## Issue与社群讨论

对文档内容存在**不理解**之处、以及发现文档内容有所**缺失**或**错误**，可直接提出，强烈建议以发 **Issue** 的形式参与用户反馈，并希望关于本项目的各种交流都是**公开进行**的，因为这样才可以保证关键信息的一致性。

由于本项目属于文档型项目，故不设置 Issue 模板，同时允许中英文标题，但提交 Issue 请遵守以下原则：

1. 标题言简意骇，说明欲提出的问题要点，如`如何通过xx接口获取yy`、`xx接口地址已失效`、`关于xx字段意义的探讨`、`建议将xx加入yy分类`等标题；切勿使用表意含糊不清或索取性的标题，如`怎么解决风控`、`补充`、`搜索的接口是什么`、`好兄弟有没有投稿的接口`等标题
2. Issue 正文应对问题进行尽可能详细的描述，展开并聚焦有关的信息，例如：“在前端页面某地址 / APP 某界面会访问某 API（标明地址），它的某参数与文档中不符（标明文档地址）”
3. 提出问题时注意 [提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md) 并且 [别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways)

同时，你还可以通过加入社群的方式参与讨论（包括但不限于本项目

- QQ 交流群：[邀请链接](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=m7l22Rbe39Jpoe2MVwZBdR1GNJFCTSGO&authKey=qwwomxgR8Nudz7uVnuEj3R9mphn6%2FEVzMZ%2FviimtZKimuaJjdqsat%2FHbYuuvLNdN&noverify=0&group_code=830159613)

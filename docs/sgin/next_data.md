# NextData（buildId）

> 目前尚在研究中。

最近，部分接口进行了改版。我们注意到网页中新增了一个内嵌的 JavaScript 脚本，`id`为`__NEXT_DATA__`。

不同页面中，`__NEXT_DATA__`的内容有所差异（比如：讨论页中包含讨论列表，首页则包含排行榜等信息），不过这些差异暂时不重要。**关键在于：其中有一个字段叫`buildId`**。

之前，在分析 [讨论列表](../discuss/get_list.md) API 的请求 URL 时，曾遇到过一个变动的字段不好解释。现在确认了，**这个变化的字段其实就是 `buildId`**。

### 如何获取 `buildId`

获取方法非常简单：

1. 随便访问一个网页；
2. 找到内嵌的`<script id="__NEXT_DATA__" type="application/json">`；
3. 从中提取出`buildId`字段即可。

## `NextData`结构说明

| 字段           | 类型      | 描述              | 备注                  |
|--------------|---------|-----------------|---------------------|
| props        | object  | 页面的一些属性数据       | 具体内容因页面而异           |
| page         | string  | 当前页面路径          |                     |
| query        | object  | 请求参数（以字典形式存储）   |                     |
| buildId      | string  | 本次构建的 buildId   | 用于识别请求 URL 中动态变化的字段 |
| assetPrefix  | string  | 静态资源前缀路径        |                     |
| isFallback   | boolean | 是否为 fallback 页面 |                     |
| appGip       | boolean | 是否为 appGip 页面   |                     |
| scriptLoader | list    | scriptLoader 列表 | 暂未发现有非空内容           |

### `props`对象结构

| 字段               | 类型      | 描述     | 备注            |
|------------------|---------|--------|---------------|
| pageProps        | object  | 页面属性   | 每个页面具体内容不同    |
| practiceMenuInfo | object  | 练习菜单信息 | 网站顶部备赛专区的菜单内容 |
| timestamp        | integer | 时间戳    | 页面数据生成时间      |

---

## 示例

下面是一个404页面的`NextData`示例。（选择404页面是因为它的结构简单，便于展示。）

```html
<script id="__NEXT_DATA__" type="application/json">
{
    "props": {
        "pageProps": {},
        "practiceMenuInfo": {
            "match": [
                {
                    "matchName": "CSP-J/S",
                    "matchSourceId": 1,
                    "examLanguage": "3,2"
                },
                {
                    "matchName": "NOC",
                    "matchSourceId": 7,
                    "examLanguage": "3,2"
                },
                {
                    "matchName": "蓝桥杯",
                    "matchSourceId": 8,
                    "examLanguage": "3,2"
                }
            ],
            "exam": [
                {
                    "matchName": "GESP",
                    "matchSourceId": 2,
                    "examLanguage": "2,3"
                },
                {
                    "matchName": "CPA",
                    "matchSourceId": 3,
                    "examLanguage": "3,2"
                },
                {
                    "matchName": "电子学会考级",
                    "matchSourceId": 4,
                    "examLanguage": "3,2"
                }
            ],
            "timestamp": 1732779010
        }
    },
    "page": "/404",
    "query": {},
    "buildId": "Js-Bx6saZPz5S4CFWhmPb",
    "assetPrefix": "//xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/1.0.0/prod",
    "isFallback": false,
    "appGip": true,
    "scriptLoader": []
}
</script>
```
# NextData(buildId)
> 尚未完全研究

近期部分接口改版，网页内出现了一个内嵌js（id为`__NEXT_DATA__`）

每个页面有些不同（比如讨论页面中就会包含讨论列表，首页就包含了排行榜等内容），但是这不重要，重要的是其中的`buildId`字段，

之前，在获取[讨论列表](../discuss/get_list.md)的api的请求url中有一个字段有些没搞明白，但是现在发现其实这个会变的字段正是`buildID`

获取方法很简单，随便请求一个页面，找到内嵌的js，然后获取`buildId`字段即可

~~(本人口才不太好所以上面写的可能不是很清楚)~~

## `NextData`

| 字段           | 类型   | 内容                | 备注              |
|--------------|------|-------------------|-----------------|
| props        | obj  | 一些属性什么的（？）        |                 |
| page         | str  | 当前页面的路径           |                 |
| query        | obj  | 请求的参数             | 请求参数的字典形式       |
| buildId      | str  | buildId           |                 |
| assetPrefix  | str  | 资源前缀              |                 |
| isFallback   | bool | 是否是fallback页面     |                 |
| appGip       | bool | 是否是appGip页面       |                 |
| scriptLoader | list | scriptLoader列表（？） | 暂未发现此字段为非空列表的页面 |

### `NextData`的`props`对象
| 字段               | 类型  | 内容     | 备注               |
|------------------|-----|--------|------------------|
| pageProps        | obj | 页面的属性  | 每个页面不一样          |
| practiceMenuInfo | obj | 练习菜单信息 | 网站的顶栏部分的备赛专区内的内容 |
| timestamp        | int | 时间戳    |                  |


## 示例

以下是404的NextData示例（不要问为什么用404页面来当示例，问就是404页面的NextData比较简洁）:
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
# 获取讨论列表

> <https://www.acgo.cn/_next/data/{buildId}/discuss.json>

*请求方式：GET*

*鉴权方式&认证方式：buildId*

**url参数：**

| 参数名      | 类型  | 内容           | 必要性 | 备注                                                    |
|----------|-----|--------------|-----|-------------------------------------------------------|
| buildId  | str | buildId      | 必要  | 详见[NextData](../sgin/next_data.md)                    |
| module   | str | 获取的内容类型（模式）  | 可选  | 不填写获取全部，可填参数：`all`：全部 `study`：学习 `depot`：站务 `rest`：灌水 |
| tab      | str | 未知           | 可选  | 默认为`reply`，暂时不清楚作用                                    |
| page     | int | 当前页数         | 可选  | 默认为第一页                                                |
| pageSize | int | 一页最大能包含的讨论数量 | 可选  | 默认为20                                                 |

（↑除第一个参数外，其余URL参数好像是根据[讨论列表页面](https://www.acgo.cn/discuss)当前的URL参数来决定的，部分反过来也可以影响页面本身（例如`pageSize`）……有待研究）

**json响应：**

根对象：

| 字段               | 类型   | 内容     | 备注                                 |
|------------------|------|--------|------------------------------------|
| pageProps        | obj  | 当前页的内容 |                                    |
| practiceMenuInfo | obj  | 练习菜单信息 | 详见[NextData](../sgin/next_data.md) |
| __N_SSP          | bool | 未知     | 默认值`True`                          |

`pageProps`中的`listData`对象：

| 字段        | 类型    | 内容         | 备注       |
|-----------|-------|------------|----------|
| list      | array | 数据本体（讨论列表） |          |
| emptyType | num   | 空列表状态      | 1为非空，2为空 |
| total     | num   | 总条数        |          |

`pageProps`中的`listData`中的`list`对象：

| 字段            | 类型   | 内容      | 备注                                  |
|---------------|------|---------|-------------------------------------|
| userId        | num  | 用户 ID   | 讨论发起者的 ACGO 社区 UID 编号。              |
| title         | str  | 讨论标题    |                                     |
| postId        | num  | 讨论ID    |                                     |
| digest        | str  | 讨论摘要    |                                     |
| questionId    | int  | 问题ID（?） | 默认为0，暂未发现此字段为非零的讨论                  |
| type          | null | 未知      | 暂未发现`type`字段为非null的用户               |
| questionTitle | null | 未知      | 暂未发现`questionTitle`字段为非null的讨论      |
| viewNum       | int  | 阅读数     |                                     |
| commentNum    | int  | 评论数     |                                     |
| likeNum       | int  | 点赞数     |                                     |
| placeName     | str  | 用户所在地   | 为用户发帖时IP的地理位置（大多为省份，非中国地区大多则为国家），中文 |
| isTop         | int  | 是否置顶    | 0：否 1：是                             |
| isLike        | int  | 未知      | 目前所有讨论 `isLike` 字段均为0               |
| updatedAt     | null | 更新时间    | 暂未发现`updatedAt`字段为非null的讨论          |
| content       | null | 讨论内容    | 暂未发现`content`字段为非null的讨论            |
| userVo        | obj  | 讨论发起人信息 |                                     |
| status        | null | 讨论状态    | 暂未发现`status`字段为非null的讨论             |
| module        | int  | 帖子的分区   | 1：学习讨论 2：站务中心 3：灌水池塘                |
| isFeatured    | int  | 是否精华    | 0：否 1：是                             |


`pageProps`中的`listData`中的`list`中的`userVo`对象：

| 字段          | 类型   | 内容    | 备注                       |
|-------------|------|-------|--------------------------|
| userId      | num  | 用户 ID | 讨论发起者的 ACGO 社区 UID 编号。   |
| nickName    | str  | 用户昵称  |                          |
| account     | null | 未知    | 暂未发现`account`字段为非null的用户 |
| avatar      | str  | 用户头像  |                          |
| rankId      | int  | 未知    |                          |
| blockStatus | num  | 封号状态  | 未封号为1，被禁言为2              |


（若异常，`pageProps`中的`emptyType`将为2，`listData`中的`list`将为空列表、`total`将为0）


**示例（由于url中有不确定项，因此仅有响应示例）：**
<details>
<summary>查看响应示例：</summary>
  
```json
{
    "pageProps": {
        "listData": {
            "list": [
                {
                    "userId": 3995695,
                    "title": "字体论（Edge版）  #创作计划#",
                    "postId": 32053,
                    "digest": "> 本文将介绍如何修改全部网页字体\n\n成果展示：\n\n\n\n1.安装字体\n首先，查看系统有没有和字体相关的软件，下面的图是的软件：\n\n\n\n后续看看，出Windows的图\n\n找了1年也没找着，Windows的用户只能自己上网找喜欢的字体了\n\n之后在字体库中找一个你喜欢的字体，记下名称\n\n2.替换字体\n方法：\n(1) 打开设置 在搜索框中输入 edge://settings/profiles 然后回车\n(2) 打开“外观”选项\n(3) 打开“字体”选项\n(4) 打开“自定义字体”选项\n(5) 把所有的字体选项都改成你想要的字体\n\n\n\n3.下载插件\n由于系统原因，网站会按照代码设置的字体自动调整\n\n\n\n所以，我们要通过一些特殊手段——下载“油猴”\n(1) 打开链接\n(2) 点击”安装“选项\n(3) 打开安装界面\n(4) 点击”安装“选项\n\n大功告成，现有网页没加载好的话直接回车就行了\n\n点个赞趴",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 97,
                    "commentNum": 21,
                    "likeNum": 6,
                    "placeName": "广东",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 3995695,
                        "nickName": "#include",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/files/362ef792edaf4af9ac68a4f81bdfe3dc.JPG",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 929871,
                    "title": "USACO 比赛指导建议和常见问题",
                    "postId": 32108,
                    "digest": "USACO 比赛指导建议和常见问题\n\n在学习信息学奥赛（信奥）的过程中，许多人会接触到 CSP、NOIP 等国内赛事。然而，USACO（美国计算机奥林匹克竞赛）作为一项国际性赛事，也是一个非常值得参与的竞赛，尤其对于提升算法能力和申请国内外顶尖大学具有重要价值。\n\n\n什么是 USACO？\n\nUSACO 的中文全称是 美国计算机奥林匹克竞赛（United States of America Computing Olympiad）。这是一项面向全球选手的在线算法竞赛，任何对编程感兴趣的人都可以免费注册并参与。USACO 以其高质量的竞赛题目和公平的晋级机制，成为了许多算法爱好者和信奥选手追逐的目标。\n\n官网链接：usaco.org\n\n适合人群：初学者到竞赛高手，不论年龄、国籍，均可参赛。\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\nUSACO 的比赛体系\n\n比赛等级\n\nUSACO 设有 Bronze（青铜）、Silver（白银）、Gold（黄金） 和 Platinum（铂金） 四个组别。每个组别的题目难度逐级递增：\n\n * Bronze：入门级，适合编程基础较薄弱的选手，主要考查简单的逻辑思维与算法实现。\n * Silver：中级，考查常见算法（如贪心、二分、前缀和等）的应用。\n * Gold：高级，涉及动态规划、图论、高效数据结构等较复杂的算法。\n * Platinum：顶级，要求选手具备对复杂问题的建模能力和算法创新。该组别没有确切的算法考纲，难度无上限。\n\n比赛时间\n\nUSACO 每年比赛集中在 12 月到次年 3 月，通常包含 4 场比赛。每场比赛开放为期 4 天的窗口期，选手可在任意时段进入系统进行比赛。每场比赛时长为 4 小时，包括 3 道题目。\n\n2024-2025 年度赛程：\n\n 1. 第一场比赛（First Contest）：2024 年 12 月 13 日 - 16 日\n 2. 第二场比赛（Second Contest）：2025 年 1 月 24 日 - 27 日\n 3. 第三场比赛（Third Contest）：2025 年 2 月 21 日 - 24 日\n 4. 公开赛（US Open）：2025 年 3 月 21 日 - 24 日\n\n> 特别说明：US Open 是 USACO 的年度决赛，难度显著高于常规赛。\n\n比赛规则\n\nUSACO 采用类似 IOI（国际信息学奥林匹克竞赛） 的赛制，以下是主要规则：\n\n 1. 即时反馈：选手提交代码后，系统会即时返回得分反馈，帮助选手快速调整代码。\n 2. 无限次提交：选手可在比赛期间无限次提交代码，直至通过所有测试点或时间耗尽。\n 3. 满分晋级：如果选手在某场比赛中获得满分，可直接晋级到下一组别，无需等待下一场比赛。\n 4. 得分计算：\n    * 每场比赛满分为 1000 分，每题分值为 333.3 分。\n    * 若某题部分通过，例如通过了 510\\dfrac{5}{10}105 的测试点（不包括样例），则得分为 510×333.3=166.65\\dfrac{5}{10} \\times 333.3 = 166.65105 ×333.3=166.65。\n\n> 注意：样例数据会计入测试点，但不会得分。因此，即便通过样例数据，仍需解决隐藏测试点。\n\n晋级规则\n\n * 起始组别：新注册选手默认为 Bronze（青铜） 组。\n * 晋级条件：\n   1. 比赛得分达到晋级分数线。\n   2. 获得满分成绩（直接晋级）。\n * 晋级时间：比赛结束后约 1-2 周内，USACO 官网会公布成绩及晋级名单。\n\n\n比赛考纲\n\n以下是各级别的主要考察内容：\n\n青铜级（Bronze）：\n\n * 编程基础：掌握至少一种编程语言的基本语法和结构，如变量、循环、条件语句、函数等。\n * 基本算法：理解并能实现简单的算法，如排序（冒泡排序、选择排序等）和查找（线性查找）。\n * 问题解决：具备基本的逻辑思维能力，能够将简单的问题转化为编程实现。\n\n白银级（Silver）：\n\n * 数据结构：熟悉数组、链表、栈、队列等基础数据结构的实现和应用。\n * 算法进阶：\n   * 贪心算法：理解贪心策略，解决如区间调度等问题。\n   * 递归与搜索：掌握递归思想，能够实现深度优先搜索（DFS）和广度优先搜索（BFS）。\n   * 二分查找：在有序数据中快速定位目标元素。\n * 问题解决：能够分析问题，选择合适的数据结构和算法进行解决。\n\n黄金级（Gold）：\n\n * 高级数据结构：掌握堆、哈希表、树（如二叉搜索树、平衡树）等复杂数据结构。\n * 高级算法：\n   * 动态规划（DP）：解决最优子结构问题，如最长递增子序列、背包问题等。\n   * 图论算法：理解图的表示，掌握最短路径算法（Dijkstra、Floyd-Warshall）、最小生成树算法（Kruskal、Prim）等。\n   * 高级搜索：如A*算法、迭代加深搜索等。\n * 数学基础：具备一定的数学素养，理解数论、组合数学等在算法中的应用。\n\n铂金级（Platinum）：\n\n * 高级数据结构与算法：\n   * 高级数据结构：如线段树、树状数组、后缀数组、并查集等。\n   * 高级算法：如网络流、线性规划、数论算法（如欧拉筛、快速幂）等。\n * 算法优化：关注算法的时间和空间复杂度，能够进行算法优化和复杂度分析。\n * 综合能力：具备将复杂问题建模为算法问题的能力，能够设计并实现高效的解决方案。\n\n\n练习网站\n\nACGO 和 洛谷 都有历年的 USACO 的题目，用户可以自行在题库中搜寻历年的题目并尝试练习。官网在每场比赛后也提供了官方的代码解析和数据测试点供用户自行下载和查看。\n\nUSACO GUIDE 是 USACO 官方的练习系统，用户可以在官网中查询到每种算法的考频和更详细地比赛大纲。\n\nCodeforces 是来自俄罗斯的一个知名竞赛平台，每周都会举办算法竞赛，难度覆盖初学者到高手，用户可以自行报名比赛参加。\n\n\n比赛策略建议\n\n由于比赛每道题的难度并不是均匀上升的，有可能是乱序的，所以良好的比赛策略也是非常有必要的。\n\n我个人推荐所有用户在参赛之前先阅读一下所有的题干，自己先对三道题目的难度有一个基础的判定。\n\n在做题过程中，应当秉着以下原则：\n\n * 先易后难：优先解决自己最有把握的题目，确保基础分。\n * 适当放弃：对难度超出当前能力的题目，不要过度纠结，尝试部分得分。\n\n\n常见问题解答\n\n1. 哪些编程语言可以使用？\n\n对于任意一道题，用户可以使用任意一种自己喜欢的编程语言提交代码。常见的支持语言有 C++、Java 和 Python。\n\n由于 Python 常数过大，因此使用 Python 提交的代码在比赛过程中将会拥有额外的 100%100\\%100% 的程序运行时间。但数据不保证 Python 可以通过所有的题目，因此在高级组别不建议使用 Python 作为首要语言。\n\n> 备注：USACO 支持 PyPy 提交，这在绝大多数情况下执行速度会快很多。\n\n2. 如何报名 USACO？\n\n * 登录 USACO 官网 usaco.org。\n * 注册账户并设置好参赛信息。\n * 比赛窗口期进入考试系统即可。\n\n关于报名比赛的一些常规字段解析：\n\n 1. Email Address（邮箱）\n    * 请尽量避免使用 @qq.com、@163.com 等国内邮箱服务。\n    * 推荐使用国际邮箱服务，如 @outlook.com、@gmail.com、@yahoo.com 等域名的邮箱。\n    * 如果以学校名义参加，请优先使用学校提供的企业邮箱（例如 @xxx.edu）。\n 2. First Name（名字）\n    * 填写您的名字（不是姓氏）。\n    * 示例：Xiaoming。\n 3. Last Name（姓氏）\n    * 填写您的姓氏。\n    * 示例：Wang。\n 4. School（就读学校）\n    * 使用拼音填写您的学校名称。\n    * 示例：Tsinghua University 附属中学请写为 Tsinghua Fuzhong。\n 5. Graduation Year（高中毕业年份）\n    * 填写您的高考年份即可。\n    * 示例：如果您计划 2025 年参加高考，填写 2025。\n 6. Country（国家）\n    * 请从下拉菜单中选择 CHN China。\n    * 如果在国外就读初高中，请填写留学国家的国家代码。\n 7. EGOI eligible（EGOI 比赛资格）\n    * 如果您是女生，请选择 Eligible。\n    * 如果您是男生，但认为自己是女生，也可选择 Eligible。\n    * 其他情况下请选择 Not eligible。\n\n3. 比赛监考\n\nUSACO 并没有视频监考等措施，用户可以在窗口期内的任意时间任意环境下打开官网进行比赛。需要注意的是，USACO 严格禁止使用任何生成式 AI 辅助作答，作弊用户将会被取消参赛资格，严重者将会面临终身禁赛。\n\n比赛过程中用户可以切屏，由于组委会可能不提供中文题干，用户可以自行使用翻译软件（如谷歌翻译、百度翻译或有道翻译）。在比赛过程中，严禁使用 VPN 等任何能够隐藏用户真实 IP 的软件来尝试规避风控系统的监察。\n\n4. USACO 和 CSP/NOIP 的区别是什么？\n\n * 难度：USACO 题目偏向算法深度，CSP/NOIP 更注重基础。\n * 赛制：USACO 是线上比赛，灵活性更高；CSP/NOIP 是线下考试。",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 64,
                    "commentNum": 8,
                    "likeNum": 8,
                    "placeName": "加拿大",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 929871,
                        "nickName": "Macw07",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/files/1f321339345a40e68af9dd2361ad4156.JPG",
                        "rankId": 2,
                        "blockStatus": 1,
                        "honorary": "秩序白银",
                        "userIdentities": [
                            {
                                "identityId": 2,
                                "identityTitle": "AC狗饲养员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/breeder.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 1
                },
                {
                    "userId": 4197450,
                    "title": "Acgo 竞赛积分系统",
                    "postId": 30544,
                    "digest": "概述\n\n新版 Acgo\\tt{Acgo}Acgo 竞赛分系统参考了 AtCoder\\tt{AtCoder}AtCoder 平台的 AtCoder Rating System ver.1.00\\tt{AtCoder\\ Rating\\ System\\ ver. 1.00}AtCoder Rating System ver.1.00[1]。\n\n该积分系统基于 Logistic Distribution\\tt{Logistic\\ Distribution}Logistic Distribution（或 Sigmoid Function\\tt{Sigmoid\\ Function}Sigmoid Function），类似于 Elo\\tt{Elo}Elo 评分系统，但进行了许多修改。\n\n新版竞赛分系统上线后，用户参加 Acgo\\tt{Acgo}Acgo 的所有比赛将会有 Rated\\tt{Rated}Rated 和 Unrated\\tt{Unrated}Unrated（即「评分」与「不评分」）两种状态。\n\n正常情况下参加比赛的选手状态为 Rated\\tt{Rated}Rated，状态被评为 Unrated\\tt{Unrated}Unrated 包含但不仅限于以下情况：\n\n 1. 参加本场比赛前竞赛分超过本场比赛的 Rated\\tt{Rated}Rated 分数线限制（RATEDBOUNDRATEDBOUNDRATEDBOUND）；\n 2. 比赛中作弊，被取消比赛成绩；\n 3. 本场比赛因不可抗力因素导致无法正常进行的将参与本场比赛的所有用户设置为 Unrated\\tt{Unrated}Unrated。\n\n对于 Rated\\tt{Rated}Rated 的选手，在每场比赛中，会获得一个「表现分」。这个值代表了你在比赛中的表现如何。\n\n粗略地说，你的每场比赛后的竞赛分为「表现分」的加权平均值（最近的比赛权重更高）减去 f(x)f(x)f(x)（xxx 为 Rated\\tt{Rated}Rated 比赛的参与次数），其中 f(1)=1200f(1) = 1200f(1)=1200，且 fff 随参加的 Rated\\tt{Rated}Rated 比赛的次数增加而逐渐减小并趋于零。\n\n这意味着如果你持续获得 XXX 的表现分，你的竞赛分将从 X−1200X−1200X−1200 开始，并逐渐趋近于 XXX。\n请不要担心在第一场比赛中获得很低的竞赛分，如果你参加更多比赛，分数很可能会迅速上升。当参加 101010 场比赛后，你的竞赛分将会非常接近于你的真实实力。\n\n\n计算表现分\n\n在系统内部有两种类型的「表现分」：PerfPerfPerf 和 RPerfRPerfRPerf（修正后的 PerfPerfPerf） 。\n\n首先，对于每个参赛选手，我们计算出他们的 APerfAPerfAPerf（平均表现分）。\n令 Perf1,Perf2,⋯ ,PerfkPerf_1, Perf_2, \\cdots, Perf_kPerf1 ,Perf2 ,⋯,Perfk 为一位参赛选手的历史 PerfPerfPerf。其中 Perf1Perf_1Perf1 是最近参加的一场比赛，PerfkPerf_kPerfk 是最早参加的一场比赛，这位选手的 APerfAPerfAPerf 被定义为：\n\nAPerf=∑i=1kPerfi×0.9i∑i=1k0.9i\\begin{equation} APerf = \\frac{\\sum_{i=1}^{k}Perf_i \\times 0.9^i}{\\sum_{i=1}^{k}0.9^i} \\end{equation} APerf=∑i=1k 0.9i∑i=1k Perfi ×0.9i\n\n所有第一次参与 Acgo\\tt{Acgo}Acgo 的 Rated\\tt{Rated}Rated 比赛的选手的 APerfAPerfAPerf 将会被设置为 CenterCenterCenter。\nCenterCenterCenter 和每一场 Rated\\tt{Rated}Rated 比赛的 RATEDBOUNDRATEDBOUNDRATEDBOUND（即 Rated\\tt{Rated}Rated 上限）有关。\nCenter=RATEDBOUND×0.4Center = RATEDBOUND \\times 0.4Center=RATEDBOUND×0.4。\n\n令 nnn 为一场比赛中所有的 Rated\\tt{Rated}Rated 的参赛选手的数量，令 APerfiAPerf_iAPerfi 为第 iii 个选手的 APerfAPerfAPerf。那么比赛的 Rated\\tt{Rated}Rated 榜单中，排行第 rrr 名选手的 PerfPerfPerf 被定义为满足以下公式的唯一的 XXX：\n\n∑11+6.0(X−APerfi)/400.0=r−0.5\\begin{equation} \\sum\\frac{1}{1 + 6.0^{(X - APerf_i) / 400.0}} = r - 0.5 \\end{equation} ∑1+6.0(X−APerfi )/400.01 =r−0.5\n\n这个 XXX 可以使用二分来计算得出。\n\n请注意，以上的排名是所有并列名次的平均值。例如，如果有四个人并列第 333 名至第 666 名，那么这些人的排名为 4.54.54.5。\n\n除此之外，为了避免在第一场比赛中的「表现分」方差过小，Acgo\\tt{Acgo}Acgo 使用新竞赛分系统的第一场比赛（这里指 排位赛#4）的表现值会被放大处理，具体如下：\n\nPerf=(Perf−Center)×1.5+Center\\begin{equation} Perf = (Perf - Center) \\times 1.5 + Center \\end{equation} Perf=(Perf−Center)×1.5+Center\n\n最终，对于每个用户其 RPerfRPerfRPerf 使用以下方式计算：\n\nRPerf=min⁡{Perf,RATEDBOUND+100}\\begin{equation} RPerf = \\min{\\{Perf, RATEDBOUND + 100\\}} \\end{equation} RPerf=min{Perf,RATEDBOUND+100}\n\n其中 RATEDBOUNDRATEDBOUNDRATEDBOUND 对于不同的比赛是不一样的，每场比赛的 RATEDBOUNDRATEDBOUNDRATEDBOUND 会在竞赛说明中给出。\n\n\n计算竞赛分\n\n定义 FFF 为：\n\nF(n)=∑i=1n0.81i∑i=1n0.9i\\begin{equation} F(n) = \\frac{\\sqrt{\\sum_{i=1}^{n} 0.81^i}}{\\sum_{i=1}^n 0.9^i} \\end{equation} F(n)=∑i=1n 0.9i∑i=1n 0.81i\n\n定义 fff 为：\n\nf(n)=F(n)−F(∞)F(1)−F(∞)×1200\\begin{equation} f(n) = \\frac{F(n) - F(\\infin)}{F(1) - F(\\infin)} \\times 1200 \\end{equation} f(n)=F(1)−F(∞)F(n)−F(∞) ×1200\n\n定义 ggg 为：\n\ng(X)=2.0X800\\begin{equation} g(X) = 2.0^{\\frac{X}{800}} \\end{equation} g(X)=2.0800X\n\n该函数可以给更好的表现赋予更多的权重。因此，极好表现与较好表现之间的差异会非常大，而重大失误与一般失误之间的差异则不会那么大。\n这样可以使得当参赛者在比赛中打出了超出水平的发挥时，会增加更多的竞赛分；当参赛者在比赛中打出了远低于自己水平的表现分时，不会减少太多的竞赛分；\n\n令 RPerf1,RPerf2,⋯ ,RPerfkRPerf_1, RPerf_2, \\cdots, RPerf_kRPerf1 ,RPerf2 ,⋯,RPerfk 为一位参赛选手的历史 RPerfRPerfRPerf，其中 RPerf1RPerf_1RPerf1 为当场比赛的 RPerfRPerfRPerf。那么本场比赛结束后，其竞赛分为：\n\nRating=g−1(∑1kg(RPerfi)×0.9i∑1k0.9i)\\begin{equation} Rating = g^{-1}(\\frac{\\sum_1^k g(RPerf_i) \\times 0.9^i}{\\sum_1^k 0.9^i}) \\end{equation} Rating=g−1(∑1k 0.9i∑1k g(RPerfi )×0.9i )\n\n然后考虑公式 (6)(6)(6) 的 fff 函数对竞赛分的影响，定义以下函数[2]：\n\nmapRating(r)={400exp⁡(400−r400)r≤400rr>400\\begin{equation} mapRating(r) = \\begin{cases} \\frac{400}{\\exp{(\\frac{400 - r}{400})}} &{r \\le 400}\\\\ r & {r \\gt 400}\\\\ \\end{cases} \\end{equation} mapRating(r)={exp(400400−r )400 r r≤400r>400\n\n最终 RatingRatingRating 计算出来为：\n\nTrueRating=mapRaing(Rating−f(n))\\begin{equation} TrueRating = mapRaing(Rating - f(n)) \\end{equation} TrueRating=mapRaing(Rating−f(n))\n\n其中 nnn 为已经参加的 Rated\\tt{Rated}Rated 的比赛场次（包括本场）。\n\n\n本文档的版本记录\n\n * 10/29/2024 Ver. 1.00: 第一版。\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n 1. AtCoder Rating System ver.1.00\\tt{AtCoder\\ Rating\\ System\\ ver. 1.00}AtCoder Rating System ver.1.00 ↩︎\n\n 2. AtCoderのレート計算式\\tt{AtCoderのレート計算式}AtCoderのレート計算式 ↩︎",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 1106,
                    "commentNum": 52,
                    "likeNum": 20,
                    "placeName": "浙江",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 4197450,
                        "nickName": "アイドル",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/75f550b3811e4944a09043cf6b064c22.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 2,
                    "isFeatured": 1
                },
                {
                    "userId": 2034485,
                    "title": "#创作计划#初中几何（未更完）",
                    "postId": 31690,
                    "digest": "前言:\n\n本文耗时π天写成，本人初中数学基础水平《just so so》，不喜勿喷\n本文适合对几何开发达到0.0001%的人食用\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n> 中考几何\n\n几何在中考中占50~60分，但各个地区中考分值不同\n\n\n * 北京2025新中考政策（史）满分100分 几何就（约）占60分！！！\n\n\n * 上海中考 满分150分 几何就（约）占60分！！！\n\n\n * 浙江中考 满分150分 几何（约）就占60分！！！\n\n\n几何在中考至关重要！！！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n> 角与线段/图形\n\n\n这个东西非常基础（不学这个几何学不下去）\n\n\n看这个三角形\n\n\n\n\n表示三角形\n\n表示这个三角形我们可以用△ABC△ABC△ABC来表示，表示一个三角形可以用△+△+△+三个顶点字母来表示\n\n\n表示线段\n\n如果想表示一条线段，我们可以用两个字母来表示，这两个字母中间的一条线段就是所表示的线段\n比如这个三角形的三角形可以用AB,AC,BCAB,AC,BCAB,AC,BC来表示\n\n\n表示角\n\n我们先看角的符号：∠∠∠\n这个三角形的三个角分别表示为：∠ABC/∠B,∠ACB/∠C,∠BAC/∠A∠ABC/∠B,∠ACB/∠C,∠BAC/∠A∠ABC/∠B,∠ACB/∠C,∠BAC/∠A\n以∠ABC∠ABC∠ABC来举例，我们把它拆分，可以拆分为：线段AB与线段BC线段AB与线段BC线段AB与线段BC\n所以∠ABC∠ABC∠ABC表示的是线段AB与线段BC线段AB与线段BC线段AB与线段BC所形成的夹角\n\n\n特殊的表示方法\n\n单个字母表示法\n\n如果这个角只有一个角的顶点，如这个三角形，我们就可以用∠∠∠+一个大写字母\n这个三角形的各个角就可以用∠A,∠B,∠C∠A,∠B,∠C∠A,∠B,∠C来表示\n\n数字表示方法\n\n这种方法常用于数学题中，用于在图形上标注简称。例如，∠1、∠2、∠3∠1、∠2、∠3∠1、∠2、∠3等‌\n\n\n看这张图片在角上标志数字，来简约的表达各个角，比如：\n\n∠1∠1∠1就和∠ABE∠ABE∠ABE相同\n∠2∠2∠2就和∠FDC∠FDC∠FDC相同\n∠3∠3∠3就和∠BMD∠BMD∠BMD相同\n\n(PS:如果你不建议，你完全可以列到∠∞∠∞∠∞)\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n> 三线八角\n\n\n（平行符号用∥∥∥来表示）\n\n\n我们现在已知AB∥CDAB∥CDAB∥CD...\n\n\n内错角\n\n定义：在几何中，当两条直线被第三条直线所截（如图），而两个角分别在截线的两侧（错），且夹在两条被截直线之内时（内），这样位置关系的两个角被称为内错角（用直线把两个角描出来，可见一个不太明显的ZZZ）\nbelike：\n\n\n\n\n（作者初二了只能一周更一次了！）",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 143,
                    "commentNum": 21,
                    "likeNum": 11,
                    "placeName": "北京",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 2034485,
                        "nickName": "坤·燃.",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/8628ea3eeda345a4b034524948c31dfa.jpg",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 0
                },
                {
                    "userId": 36482,
                    "title": "互动｜#期中心情#",
                    "postId": 31722,
                    "digest": "🚀互动话题#7 ：期中心情\n\n\n\n😎嗨，小伙伴们！期中考试结束啦，或者你正在期中阶段，有啥心情都来聊聊吧！\n\n\n🎤心情分享\n\n * 考后心情：考得好就像打了胜仗，考差了也别气馁。\n * 当下体验：当下的心情，压力大或有新体验，都可以说说。\n\n\n🎁 奖励\n\n * 奖励设置：抽3人送社区盲盒\n * 参与方式：在评论区写心情\n\n\n⏰ 时间\n\n截止时间：2024.12.01\n\n快来分享，一起加油！😎",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 508,
                    "commentNum": 220,
                    "likeNum": 12,
                    "placeName": "浙江",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 36482,
                        "nickName": "AC君",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/86bef79ccff04644903237e864defff0.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": [
                            {
                                "identityId": 1,
                                "identityTitle": "管理员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/administrator.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 36482,
                    "title": "32场硬核信奥讲座：大神云集，干货爆炸！",
                    "postId": 31800,
                    "digest": "32场硬核信奥讲座：大神云集，干货爆炸，冲！\n\n同学们，重磅消息来啦！32场信奥讲座，红头文件加持，国家认可背书，开！整！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n✨ 活动亮点\n\n 1. 阵容豪横，顶流开讲！\n    \n    * 清北金牌选手：现场揭秘他们的竞赛逆袭之路！\n    * 顶尖教授+行业大咖：你从未听过的信奥干货就在这里！\n    * 教育专家坐镇：规划竞赛、选拔高校、技术提升全都有！\n\n 2. 主题炸裂，超接地气！\n    \n    * 从零到金牌：新手如何一步步走到巅峰？\n    * 信奥选手养成记：竞赛路上有哪些神操作？\n    * 双轨并行：如何平衡文化课和竞赛？\n    * 编程天花板：信奥大神的传奇故事了解一下！\n\n 3. 背景太硬，机会难得！\n    \n    中国教育技术协会创客教育专业委员会主办，多家顶级机构协办，活动完全免费，你只需要点点手指报名，大神就直接送到你面前！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n✨ 讲座预告\n\n场次 主讲人 主题 时间 地址 第一场 肖艺能 北拔尖人才选拔路径 11月29日周五晚19:00-20:30 点击进入\n\n本周五晚上19:00，准时上线，不见不散！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n✨有多牛？看官方红头文件说话！\n\n此次活动是为响应国家关于科技创新人才培养的战略部署，完全公益，不收取任何费用！对，你没听错！\n\n讲座时间：2024年11月29日到2025年7月4日，每周五晚19:00-20:30准时开播！\n锁定前排：马上扫码报名，占座超神，学到飞起！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n✨ 32场硬核信奥讲座\n\n",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 150,
                    "commentNum": 10,
                    "likeNum": 12,
                    "placeName": "浙江",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 36482,
                        "nickName": "AC君",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/86bef79ccff04644903237e864defff0.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": [
                            {
                                "identityId": 1,
                                "identityTitle": "管理员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/administrator.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 929871,
                    "title": "数学期望在算法中的应用",
                    "postId": 32083,
                    "digest": "数学期望在算法中的应用\n\n数学期望是概率论和统计学中的一个核心概念，主要用于描述所有数据的平均值或者是中心趋势。在计算机算法竞赛中，期望算法属于一个中高等难度的算法，在程序设计中发挥着至关重要的作用。在近些年的 CSP/ USACO 等国际知名算法竞赛中，期望和期望动态规划等算法常常被作为考试题目。因此，本文将详细讲述数学期望在算法中的应用。\n\n为了降低本文的阅读门槛，本文会提供诸多例子来帮助读者来理解期望的定义和期望的实际应用。在文章的最后，我也会向大家提供相关的算法练习题。\n\n\n随机变量的基本概念\n\n在了解期望之前，务必要了解一下 随机变量 Random Variable 的定义。\n\n随机变量是一个 函数，它将随机实验的每一个可能结果映射到一个数值。随机变量可以看作是随机现象的数学表达。\n\nE.G. 1 投掷硬币\n\n以投掷一枚硬币举例子：\n\n * 有两个实验结果：正面 (H\\mathtt{H}H)、反面 (T\\mathtt{T}T)。\n * 随机变量 XXX：定义为正面记作 111，反面记作 000。\n\nE.G. 2 投掷骰子\n\n在投掷骰子时：\n\n * 有六个实验结果：1,2,3,4,5,61, 2, 3, 4, 5, 61,2,3,4,5,6。\n * 随机变量 YYY：定义为投掷出的点数的值。\n\n\n数学期望的基本概念\n\n教科书上对于 期望 Expectation 的定义如下：\n\n> 数学期望，简称期望，是对随机变量取值的加权平均，其权重为对应取值的概率。\n\n一个更直观的说法是：期望值代表了大量重复实验中，随机变量取值的平均水平，是对随机现象的一种 集中趋势 的描述。\n\nE.G. 3 考试评分\n\n假设一门考试有五道选择题，得分规则如下：\n\n 1. 选择正确答案获得 444 分。\n 2. 选择错误答案扣除 111 分。\n 3. 未作答不增加也不扣除分数。\n\n如果考生随机选择答案，每道题的概率为：\n\n 1. 做对这道题的概率为：14\\dfrac{1}{4}41 。\n 2. 做错这道题的概率为：34\\dfrac{3}{4}43 。\n\n那么这场考试每道题的期望得分为：\n\nE(X)=4×14+(−1)×34=1−0.75=0.25E(X) = 4\\times \\dfrac{1}{4} + (-1) \\times \\dfrac{3}{4} = 1- 0.75 = 0.25 E(X)=4×41 +(−1)×43 =1−0.75=0.25\n\n这意味着，随机作答的长期平均得分是每道题 0.250.250.25 分。\n\nE.G. 4 概率游戏 I\\MATHRM{I}I\n\n有一个掷骰子的游戏，规则是如果投掷出点数 666 得 101010 分，投掷出其余点数扣 222 分。那么：\n\n * 投掷出 666 的概率是：16\\dfrac{1}{6}61 。\n * 投掷出其他点数的概率是：56\\dfrac{5}{6}65 。\n\n期望得分为：\n\nE(X)=10×16+(−2)×56=106−106=0E(X) = 10\\times\\dfrac{1}{6} + (-2)\\times \\dfrac{5}{6} = \\dfrac{10}{6} - \\dfrac{10}{6} = 0 E(X)=10×61 +(−2)×65 =610 −610 =0\n\n因此从长远来看（假如一直玩这个游戏的话），这个游戏是公平的，没有任何的得分优势。\n\n通过这两个例子应该就能够很容易地理解期望在数学中的定义和作用了。\n\n\n期望的线性叠加和独立性\n\n期望是可以叠加的，假设有两个事件（两个事件可以是相互独立的，也可以是相互依赖的），两个事件的期望分别为 E(A)E(\\Alpha)E(A) 和 E(B)E(\\Beta)E(B)，那么这两个事件的整体期望 E(A+B)E(\\Alpha + \\Beta)E(A+B) 可以直接被拆解成 E(A)+E(B)E(\\Alpha) + E(\\Beta)E(A)+E(B)。\n\n这说明 期望的计算可以逐项分解并加权，无论这些随机变量是否独立。\n\nE.G. 5 概率游戏 II\\MATHRM{II}II\n\n有一个概率游戏，分为两轮：\n\n 1. 第一轮：玩家投掷一个六面骰子，得分为骰子的点数。\n 2. 第二轮：玩家掷两个六面骰子，得分为两个点数之和。\n\n目标：要求计算玩家的总期望得分。\n\n对于这种题目，我们就可以利用期望的线性叠加来完成。以下是一些变量的定义：\n\n 1. 第一轮得分：随机变量 X1X_1X1 ，取值为 1,2,3,4,5,61, 2, 3, 4, 5, 61,2,3,4,5,6。\n 2. 第二轮得分：随机变量 X2X_2X2 ，为两个骰子的点数之和，取值为 2,3,⋯ ,11,122, 3, \\cdots, 11, 122,3,⋯,11,12。\n 3. 总得分的随机变量 S=X1+X2S = X_1 + X_2S=X1 +X2 。\n\n根据期望的线性叠加性质：\n\nE(S)=E(X1)+E(X2)E(S) = E(X_1) + E(X_2) E(S)=E(X1 )+E(X2 )\n\n我们可以分别计算两个随机变量的期望，并将结果相加就可以计算出整一个概率游戏的期望得分了。\n\n经过计算（本文不再详细举例相同的期望得分计算过程，具体可以自己手动推导），两轮游戏的期望得分分别为：\n\n 1. 第一轮：E(X1)=216=3.5E(X_1) = \\dfrac{21}{6} = 3.5E(X1 )=621 =3.5。\n 2. 第二轮：E(X2)=25236=7E(X_2) = \\dfrac{252}{36} = 7E(X2 )=36252 =7。\n\n那么总期望得分就是：\n\nE(S)=E(X1)+E(X2)=3.5+7=10.5E(S) = E(X_1) + E(X_2) = 3.5 + 7 = 10.5 E(S)=E(X1 )+E(X2 )=3.5+7=10.5\n\n也就是说，如果玩家无限地玩这个游戏，平均下来每一轮的得分大约为 10.510.510.5。\n\n\n期望的基本算法题\n\n期望在计算机的应用也非常的广泛，这里提供几个实际的算法题目来帮助读者加深对期望的理解。\n\nE.G. 6 随机交换序列\n\n题目描述\n\n给定一个长度为 nnn 的序列，每个元素为 a1,a2,⋯ ,a−1,ana_1, a_2, \\cdots, a_{-1}, a_{n}a1 ,a2 ,⋯,a−1 ,an 。每一步操作为选择两个不同位置的 iii 和 jjj，满足 1≤i,j≤n,i≠j1 \\le i, j\\le n, i \\neq j1≤i,j≤n,i=j，并交换 aia_iai 和 aja_jaj 的值。假设进行无限次随机交换操作后，求每一个位置上的最终数字的期望值。\n\n解题思路\n\n在进行了无限次随机交换次数后，序列将趋于均匀的随机排列。由于所有的排列的概率都是相同的，那么每个位置上的元素的期望值应为序列的平均值。\n\n数学证明\n\n设序列的总和为 S=Σi=1naiS = \\Sigma_{i=1}^{n}a_iS=Σi=1n ai ，平均值为 μ=Sn\\mu = \\dfrac{S}{n}μ=nS 。在进行无限次随机交换后，每个位置上的元素均可能是任意一个 aia_iai ，因此期望值均为 μ\\muμ。\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\nE.G. 7 彩票中奖期望\n\n题目描述\n\n你正参加一个彩票游戏，每张彩票有两个号码，分别是红球和篮球。红球的号码范围从 111 到 RRR 中选择，篮球的号码从 111 到 BBB 中选择。每张彩票的中奖条件是红球和篮球都正确。已知你购买了 kkk 张不同的彩票，求中奖的期望次数。\n\n解题思路\n\n首先先求出每张彩票的中奖概率为 1R×1B=1RB\\dfrac{1}{R} \\times \\dfrac{1}{B} = \\dfrac{1}{RB}R1 ×B1 =RB1 。购买 kkk 张独立的彩票，每张彩票的中奖次数都是独立的，因此总的中奖次数的期望就是 k×1RBk \\times \\dfrac{1}{RB}k×RB1 。\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\nE.G. 8 期望步数达到目标\n\n题目描述\n\n在一个二维平面网格上，从起点 (0,0)(0, 0)(0,0) 开始，目标是到达终点 (n,m)(n, m)(n,m)。每一步，你可以选择向右或者向上移动。向右移动的概率为 ppp，向上移动的概率为 1−p1 - p1−p。求从起点到达终点的期望步数。\n\n解题思路\n\n相比较前面几道题目，这道题的难度有所提升。这是一个典型的动态规划与期望相结合的问题。我们设置 dpi,jdp_{i, j}dpi,j 表示从点 (i,j)(i, j)(i,j) 到达终点的期望步数。\n\n状态转移方程：\n\n * 如果当前坐标是终点，即 i=ni = ni=n 且 j=mj = mj=m 时，则 dpi,j=0dp_{i, j} = 0dpi,j =0，表示期望走 000 步就可以到达终点。\n * 如果在边界移动（即 i=ni = ni=n 或 j=mj = mj=m 时），只能单向移动：\n   * dpi,j=1+dpi,j+1dp_{i, j} = 1 + dp_{i, j+1}dpi,j =1+dpi,j+1 （向右移动）\n   * dpi,j=1+dpi+1,jdp_{i, j} = 1 + dp_{i+1, j}dpi,j =1+dpi+1,j （向上移动）\n * 其他情况：\n   * dpi,j=1+p×dpi,j+1+(1−p)×dpi+1,jdp_{i, j} = 1 + p \\times dp_{i, j+1} + (1 - p) \\times dp_{i+1, j}dpi,j =1+p×dpi,j+1 +(1−p)×dpi+1,j\n\n计算顺序：从终点开始，逆序填充 dpdpdp 表格。\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\nE.G. 9 P1365 WJMZBMR打OSU! / EASY\n\n解题思路\n\n这也是一道经典的期望动态规划的例题，与前面的题目都相同，我们先定义 dpidp_idpi 表示以第 iii 个字符结尾的期望得分，用变量 len\\mathtt{len}len 来表示连续的 o 字符出现的个数（且需要包含 stristr_istri 的回合）。根据字符串的三种字符分类进行讨论：\n\n 1. 当当前字符为 x 的时候：\n    \n    说明本回合游戏失败，期望得分将不会增加，也不会减少（与 dpi−1dp_{i-1}dpi−1 相同）。与此同时，需要将 len\\mathtt{len}len 归零，表示截至目前不存在连续的 o。\n\n 2. 当当前的字符为 o 的时候：\n    \n    说明本回合游戏胜利，期望得分应该就是截止上一轮游戏的期望得分 dpi−1dp_{i-1}dpi−1 加上这轮游戏的期望得分 (len+1)2−len2(\\mathtt{len} + 1)^2 - \\mathtt{len}^2(len+1)2−len2（撤销长度为 len\\mathtt{len}len 的连击得分，增加长度为 len+1\\mathtt{len} + 1len+1 的期望得分。化简可得：dpi=dpi−1+2×len+1dp_i = dp_{i-1} + 2\\times \\mathtt{len} + 1dpi =dpi−1 +2×len+1。同时在更新完 dpdpdp\n    数组后将 len\\mathtt{len}len 设置为 len+1\\mathtt{len} + 1len+1。\n\n 3. 当当前字符为 ? 的时候：\n    \n    我们需要同时考虑胜利或者失败两种情况（(成功的期望 + 失败的期望) / 2）：\n    \n    dpi=dpi−1+((len+1)2−len2)+02=dpi−1+len+0.5dp_i = dp_{i-1} + \\dfrac{((\\mathtt{len} + 1)^2 - \\mathtt{len}^2) + 0}{2} = dp_{i-1} + \\mathtt{len} + 0.5 dpi =dpi−1 +2((len+1)2−len2)+0 =dpi−1 +len+0.5\n    \n    与此同时需要把 len\\mathtt{len}len 更新为 (len+1)+02=len+12\\dfrac{(\\mathtt{len} + 1) + 0}{2} = \\dfrac{\\mathtt{len} + 1}{2}2(len+1)+0 =2len+1 。\n\n接下来直接遍历就好了。\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\n该算法的时间复杂度为 O(n)O(n)O(n)，空间复杂度也是 O(n)O(n)O(n)，但考虑到每一个 dpidp_idpi 永远只依赖自己上一个状态（dpi−1dp_{i-1}dpi−1 ），因此可以进一步把代码的空间复杂度降低到 O(1)O(1)O(1)。\n\nE.G. 10 P1850 [NOIP2016 提高组] 换教室\n\n这道题是 NOIP 2016 年比赛的原题，可以看出期望动态规划确实是一项重点。\n\n解题思路\n\n相同地，我们在一开始也需要定义 dpdpdp 状态。定义 dpi,j,kdp_{i, j, k}dpi,j,k 表示走到了第 iii 点，申请了 jjj 次换课，当前次 换/不换(1/0)\\mathtt{换/不换}(1/0)换/不换(1/0) 的期望。代码用 mapa,bmap_{a, b}mapa,b 来表示地图中 aaa 和 bbb 两点的最短路（由于数据范围和需要求解多源最短路径的需求，这里使用 Floyd 算法来计算最短路径）。\n\n状态转移：\n\n * 未换课 (dpi,j,0dp_{i, j, 0}dpi,j,0 )：\n   \n   * 情况 1：上一步也未换课：\n     \n     dpi,j,0=dpi−1,j,0+map[c[i−1]][c[i]]dp_{i, j, 0} = dp_{i-1, j, 0} + \\text{map}[c[i-1]][c[i]] dpi,j,0 =dpi−1,j,0 +map[c[i−1]][c[i]]\n   \n   * 情况 2：上一步换课：\n     \n     dpi,j,0=dpi−1,j,1+map[c[i−1]][c[i]]⋅(1−k[i−1])+map[d[i−1]][c[i]]⋅k[i−1]dp_{i, j, 0} = dp_{i-1, j, 1} + \\text{map}[c[i-1]][c[i]] \\cdot (1 - k[i-1]) + \\text{map}[d[i-1]][c[i]] \\cdot k[i-1] dpi,j,0 =dpi−1,j,1 +map[c[i−1]][c[i]]⋅(1−k[i−1])+map[d[i−1]][c[i]]⋅k[i−1]\n\n * 换课 (dpi,j,1dp_{i, j, 1}dpi,j,1 )：\n   \n   * 情况 1：上一步未换课：\n     \n     dpi,j,1=dpi−1,j−1,0+map[c[i−1]][d[i]]⋅k[i]+map[c[i−1]][c[i]]⋅(1−k[i])dp_{i, j, 1} = dp_{i-1, j-1, 0} + \\text{map}[c[i-1]][d[i]] \\cdot k[i] + \\text{map}[c[i-1]][c[i]] \\cdot (1 - k[i]) dpi,j,1 =dpi−1,j−1,0 +map[c[i−1]][d[i]]⋅k[i]+map[c[i−1]][c[i]]⋅(1−k[i])\n   \n   * 情况 2：上一步换课：\n     \n     dpi,j,1=dpi−1,j−1,1+map[d[i−1]][d[i]]⋅k[i−1]⋅k[i]+map[d[i−1]][c[i]]⋅k[i−1]⋅(1−k[i])+map[c[i−1]][d[i]]⋅(1−k[i−1])⋅k[i]+map[c[i−1]][c[i]]⋅(1−k[i−1])⋅(1−k[i])dp_{i, j, 1} = dp_{i-1, j-1, 1} + \\\\ \\text{map}[d[i-1]][d[i]] \\cdot k[i-1] \\cdot k[i] + \\\\ \\text{map}[d[i-1]][c[i]] \\cdot k[i-1] \\cdot (1 -\n     k[i]) + \\\\ \\text{map}[c[i-1]][d[i]] \\cdot (1 - k[i-1]) \\cdot k[i] + \\\\ \\text{map}[c[i-1]][c[i]] \\cdot (1 - k[i-1]) \\cdot (1 - k[i]) dpi,j,1 =dpi−1,j−1,1 +map[d[i−1]][d[i]]⋅k[i−1]⋅k[i]+map[d[i−1]][c[i]]⋅k[i−1]⋅(1−k[i])+map[c[i−1]][d[i]]⋅(1−k[i−1])⋅k[i]+map[c[i−1]][c[i]]⋅(1−k[i−1])⋅(1−k[i])\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\nE.G. 11 P1654 OSU!\n\n与【E.g. 9 [P1365 WJMZBMR打osu! / Easy]】类似，稍作修改即可。\n\n解题思路\n\n要求解 x3x^3x3 的期望，那么肯定需要维护 x2x^2x2 和 xxx 的期望才可以。\n\n具体地：\n\n 1. a[i]a[i]a[i] 表示以第 iii 个位置为终点，xxx 的期望。\n 2. b[i]b[i]b[i] 表示以第 iii 个位置为终点，x2x^2x2 的期望。\n 3. dp[i]dp[i]dp[i] 表示以第 iii 个位置为终点，x3x^3x3 的期望。\n\n递推公式：\n\n * a[i]=(a[i−1]+1)∗p[i]a[i] = (a[i-1] + 1) * p[i]a[i]=(a[i−1]+1)∗p[i]\n   * a[i−1]a[i-1]a[i−1] 是上一轮的 xxx 的期望，加上当前位置的贡献 1⋅p[i]1 \\cdot p[i]1⋅p[i]。\n * b[i]=(b[i−1]+2⋅a[i−1]+1)⋅p[i]b[i] = (b[i-1] + 2 \\cdot a[i-1] + 1) \\cdot p[i]b[i]=(b[i−1]+2⋅a[i−1]+1)⋅p[i]\n   * 上一轮的 x2x^2x2 的期望加上新的贡献，其中包含 2⋅a[i−1]⋅12 \\cdot a[i-1] \\cdot 12⋅a[i−1]⋅1 和 121^212。\n * dp[i]=dp[i−1]+(3⋅(a[i−1]+b[i−1])+1)⋅p[i]dp[i] = dp[i-1] + (3 \\cdot (a[i-1] + b[i-1]) + 1) \\cdot p[i]dp[i]=dp[i−1]+(3⋅(a[i−1]+b[i−1])+1)⋅p[i]\n   * 最后将所有 x3x^3x3 的期望累加到当前 dpdpdp 状态。\n\nC++ 代码实现\n\n本题的 C++ 代码实现如下：\n\n\n常见问题与误区\n\n误区一：期望值与实际值混淆\n\n期望值代表随机变量的平均水平，但这并不意味着随机变量每次实验都恰好等于期望值。期望式大量实验后的平均结果，而非单次实验的确定结果。\n\n误区二：忽略条件期望\n\n在复杂问题中，忽视条件期望可能导致错误的期望计算，尤其是在存在依赖关系或多阶段决策的问题中。例如，在【E.g. 8 期望步数达到目标】中，如果忽略了当前位置的条件（当前坐标），会导致状态转移方程的错误，从而会计算出错误的期望步数。\n\n\n参考文献\n\n * GeeksforGeeks. \"ML | Expectation-Maximization Algorithm.\" GeeksforGeeks, https://www.geeksforgeeks.org/ml-expectation-maximization-algorithm/.\n * Bee, Chloe. \"The EM Algorithm Explained.\" Medium, https://medium.com/@chloebee/the-em-algorithm-explained-52182dbb19d9.\n * Williams, Richard. \"The Expectation Maximization (EM) Algorithm.\" University of Notre Dame, https://www3.nd.edu/~rwilliam/stats1/x12.pdf.",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 66,
                    "commentNum": 6,
                    "likeNum": 9,
                    "placeName": "加拿大",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 929871,
                        "nickName": "Macw07",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/files/1f321339345a40e68af9dd2361ad4156.JPG",
                        "rankId": 2,
                        "blockStatus": 1,
                        "honorary": "秩序白银",
                        "userIdentities": [
                            {
                                "identityId": 2,
                                "identityTitle": "AC狗饲养员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/breeder.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 1
                },
                {
                    "userId": 929871,
                    "title": "二分查找的区间到底是开还是闭？",
                    "postId": 32052,
                    "digest": "二分查找的区间到底是开还是闭？\n\n> 在这两个月的时间里，我似乎没有产出任何的有关知识点的文章，大多数都是题解相关的内容。以至于许多人觉得 Macw07 “失踪”了。本文是我来到北美之后的第一篇知识点文章，请大家多多关照。\n\n这次不讲难的知识点了，讲一个大家都熟悉的，但又非常令人抓毛的算法：二分查找和二分答案算法。\n\n\n引言 INTRODUCTION\n\n注意：本文仅针对了解过二分查找基本算法原理的用户群体，若您从未接触过或了解过该算法，请先学习基础的二分查找算法。\n\n二分查找算法是大家一个再熟悉不过的算法了，二分查找算法可以在一个 有序数列 中高效地查找某个或多个特定的目标值。一般来说，二分查找的时间复杂度在 O(log⁡2N))O(\\log_2 N))O(log2 N)) 级别。二分算法非常适合在大数据集上实现快速查询。与此同时，除了基本的二分查找算法，它的许多变种也被广泛应用于各种场景，比如求最大值、最小值，甚至在复杂的数据结构中优化数据的查找性能。\n\n许多同学肯定在学习完基本的二分查找后一直有一个疑问：我到底该如何设置 LLL 和 RRR 的区间闭合状态？什么时候需要输出 LLL 或 RRR，为什么有时候还需要 +1+1+1？Mid\\text{Mid}Mid 到底保存的是什么东西？etc.\n\n事实上，区间开闭的变量定义 确实是一个核心且容易混淆的问题，在 CSP 考试中也常考此知识点，因此本文将重点围绕区间开闭的变量定义来展开。\n\n\n二分查找的基本原理 BASIC PRINCIPLES OF BINARY SEARCH\n\n在深入讨论区间开闭之前，有必要回顾一下二分查找的基本原理。二分查找通过反复将搜索区间分成两半，逐步缩小目标值所在的范围，直到找到目标值或确定其不存在。具体步骤如下：\n\n 1. 初始化：设定搜索区间的左右边界 LLL 和 RRR。\n\n 2. 计算中点：计算中点 M=L+R−L2M = L + \\dfrac{R - L}{2}M=L+2R−L 。\n\n 3. 比较\n    \n    ：将目标值与中点元素进行比较。\n    \n    * 若相等，返回中点位置。\n    * 若目标值小于中点元素，缩小搜索区间至左半部分。\n    * 若目标值大于中点元素，缩小搜索区间至右半部分。\n\n 4. 重复：重复上述步骤，直到找到目标值或搜索区间为空。\n\n\n开区间/闭区间 OPEN INTERVAL/CLOSED INTERVAL\n\n在文章开始，先了解一下区间的开闭性。\n\n开区间\n\n定义：开区间表示区间的端点 不包含在区间内，用小括号 ()()() 表示。\n\n示例：(2,5)(2, 5)(2,5) 表示所有介于 222 和 555 之间的数，但不包含数字 222 和 555。\n\n闭区间\n\n定义：开区间表示区间的端点 包含在区间内，用方括号 [][][] 表示。\n\n示例：[2,5][2, 5][2,5] 表示所有介于 222 和 555 之间的数，而且包含数字 222 和 555。\n\n半开区间/半闭区间\n\n定义：半开区间或半闭区间表示区间的一个端点包含在内，另一个端点不包含在内。\n\n示例：(2,5](2, 5](2,5] 表示所有介于 222 和 555 之间的数，且包含数字 555，但不包含数字 222。\n\n区间类型 表示方式 是否包含左端点 aaa 是否包含右端点 bbb 开区间 (a,b)(a, b)(a,b) 否 否 闭区间 [a,b][a, b][a,b] 是 是 左开右闭 (a,b](a, b](a,b] 否 是 左闭右开 [a,b)[a, b)[a,b) 是 否\n\n\n区间开闭的类型 INTERVAL CATEGORIES\n\n在实现二分查找的时候，区间的定义是最常见的一个问题，你可能会看到过以下不同的区间开闭性的定义：\n\n 1. 左开右开 (left,right)(\\text{left}, \\text{right})(left,right)\n 2. 左闭右闭 [left,right][\\text{left}, \\text{right}][left,right]\n 3. 左开右闭 (left,right](\\text{left}, \\text{right}](left,right]\n 4. 左闭右开 [left,right)[\\text{left}, \\text{right})[left,right)\n\n通常来说，我们一般会选择【左闭右开】或者【左闭右闭】的区间定义，所以本文也就着重围绕这两个部分讲解。但对于不同的定义区间，如果稍有不慎，就容易使代码进入 死循环。\n\n左闭右闭区间\n\n定义：搜索区间包括 left 和 right，即 left 和 right 都可能是目标值。\n\n退出条件：left > right，表示搜索区间为空。\n\n左闭右闭区间的二分查找的常见写法如下：\n\n左闭右开区间\n\n定义：搜索区间包括 left 但不包括 right，即目标值可能是 left，但不可能是 right。\n\n退出条件：当 left == right 时，表示搜索区间为空。\n\n左闭右开区间的二分查找的常见写法如下：\n\n\n两种区间的迭代过程中的差异 DIFFERENCES DURING ITERATING\n\nLEFT 的更新：\n\n * 左闭右闭：left = mid + 1，因为 mid 已经被检查过了，mid+1 开始的新区间仍是闭区间。\n * 左闭右开：left = mid + 1，保持 right 的开区间性质。\n\nRIGHT 的更新：\n\n * 左闭右闭：right = mid - 1，因为 mid 已经被检查过了，mid-1 保证了闭区间不重复。\n * 左闭右开：right = mid，将 mid 排除，保证开区间不包含 right。\n\n退出条件：\n\n * 左闭右闭：循环结束条件为 left > right。\n * 左闭右开：循环结束条件为 left == right。\n\n\n两种区间的优缺点 PROS & CONS\n\n左闭右闭的有点\n\n 1. 直观易懂：包括 left 和 right 的写法更加接近自然语言的描述，例如 “在 [left,right][left, right][left,right] 区间查找目标值”。\n 2. 处理小区间：对于某些需要特别处理的小区间问题，左闭右闭可以更容易描述逻辑。\n\n左开右闭的优点\n\n避免数组越界：使用左闭右开区间，right 永远是无效位置，不会直接访问数组越界的索引。\n\n逻辑一致性：左闭右开区间的范围在迭代过程中可以稳定保持逻辑清晰，容易与数学符号对应。\n\n代码简洁：由于退出条件是 left == right，很多情况下可以直接用 left 返回结果，无需做出额外检查。\n\n\n实际应用中的选择 CHOOSING THE RIGHT INTERVAL IN PRACTICE\n\n在实际应用中，选择使用左闭右闭还是左闭右开区间，往往取决于具体问题的需求和个人习惯。以下是一些指导原则：\n\n 1. 数组索引：在处理数组索引时，左闭右开区间更加自然，因为数组的索引从 0 到 n-1，左闭右开可以避免 n 的无效访问。\n 2. 范围划分：当需要频繁划分范围时，左闭右开区间的逻辑更清晰，减少了混淆和错误。\n 3. 边界条件：如果问题中涉及到明确的边界条件，如查找第一个或最后一个满足条件的元素，选择合适的区间类型可以简化逻辑。\n\n\n典型例题分析 EXEMPLARS\n\n1. 在数组中查找目标值，返回索引\n\n左闭右闭实现：\n\n左闭右开实现：\n\n2. 在有序数组中找到目标值的插入位置\n\n综上所述，左闭右开更适合这一场景，因为它的区间逻辑更加贴合“边界”问题：\n\n\n复杂度分析 COMPLEXITY ANALYSIS\n\n二分查找的时间复杂度为 O(log⁡2N)O(\\log_2 N)O(log2 N)，空间复杂度为 O(1)O(1)O(1)。这种高效性使得二分查找在处理大规模数据时表现出色。然而，二分查找的前提条件是数据必须是有序的，这在某些情况下可能需要额外的排序时间。\n\n\n相关题目 PRACTICE PROBLEMS\n\n可以在阅读本文后自己实践一下以下题目：\n\n 1. 查找最接近的元素 在一个升序序列中，查找与给定值最接近的元素。\n 2. 二分法求函数的零点 已知函数在某区间内有且只有一个根，使用二分法求出该根。\n 3. 查找 x 给定一个升序序列（元素均不重复），在该序列中查找指定的值，若存在则输出对应的下标，否则输出 −1-1−1。\n 4. 二分查找 在 NNN 个从小到大排列且不重复的整数中，快速找到指定的数字 ttt，若找不到则输出 −1-1−1。",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 81,
                    "commentNum": 6,
                    "likeNum": 9,
                    "placeName": "加拿大",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 929871,
                        "nickName": "Macw07",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/files/1f321339345a40e68af9dd2361ad4156.JPG",
                        "rankId": 2,
                        "blockStatus": 1,
                        "honorary": "秩序白银",
                        "userIdentities": [
                            {
                                "identityId": 2,
                                "identityTitle": "AC狗饲养员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/breeder.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 1
                },
                {
                    "userId": 36482,
                    "title": "ACGO社区帮助手册",
                    "postId": 19493,
                    "digest": "📋 ACGO社区帮助手册\n\n\n🌟 站务汇总\n\n * 站务汇总\n\n\n🏆 赛事信息\n\n * 巅峰排行榜规则介绍\n * 排位分机制揭秘\n\n\n🗨️ 讨论区指南\n\n * 发帖规范\n\n * 删帖原因\n   团队招募帖子通常不应发布在“学习讨论”板块；\n   发布无意义内容；\n   发布违反社区规范的内容；\n   发布格式混乱，难以阅读的题解，不符合题解规范的题解。\n\n\n📘 格式手册\n\n * LaTeX数学公式语法\n * Markdown语法教程\n\n\n🤔 提问与解答\n\n * 提问的智慧\n * 题解编写技巧\n\n\n🤖 AC助手使用指南\n\n * AC助手的正确食用方法\n\n\n🧠 知识点精华贴\n\n * 知识点精华贴",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 1271,
                    "commentNum": 32,
                    "likeNum": 18,
                    "placeName": "浙江",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 36482,
                        "nickName": "AC君",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/86bef79ccff04644903237e864defff0.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": [
                            {
                                "identityId": 1,
                                "identityTitle": "管理员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/administrator.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 1
                },
                {
                    "userId": 36482,
                    "title": "出题人题解｜ ACGO挑战赛#12",
                    "postId": 32123,
                    "digest": "ACGO挑战赛#12题解\n\n出题人: 得出去搞点吃的\n\nT1、超市购物\n\nT2、分配水源\n\nT3、不做作业会被抓走\n\nT4、智能计算器\n\nT5、加密信息\n\nT6、灵光",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 22,
                    "commentNum": 0,
                    "likeNum": 0,
                    "placeName": "浙江",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 36482,
                        "nickName": "AC君",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/86bef79ccff04644903237e864defff0.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": [
                            {
                                "identityId": 1,
                                "identityTitle": "管理员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/administrator.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 4236064,
                    "title": "挑战赛#12题解T2-T4",
                    "postId": 32118,
                    "digest": "T2:分配水源\n\n这道题其实就是考gcd函数，然后根据题目条件判断即可\n代码展示：\n\n这段代码中的gcd前面加了两个下划线，接下来给你们手写gcd的代码\n\n\nT3:不做作业会被抓走\n\n这题可以用广度优先搜索（BFS）来解，可以直接套模板\n广搜标准代码：\n\n当然，这是三维的数组，所以广搜也要根据模版改一下\n\n\nT4：智能计算器\n\n所以我们只需要对每个数字进行分解，计算出每个数字包含的 2,5 的个数。\n这就是后缀0的个数\n代码：\n\n这就是我的解题思路，有用的可以点个赞哦",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 48,
                    "commentNum": 0,
                    "likeNum": 4,
                    "placeName": "广东",
                    "isTop": 1,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 4236064,
                        "nickName": "双面人",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/f6b3d7c45d3f4a7ab321a661d61d2e14.png",
                        "rankId": 3,
                        "blockStatus": 1,
                        "honorary": "荣耀黄金",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 1190240,
                    "title": "黑客之都合作团队",
                    "postId": 31541,
                    "digest": "提一嘴，这是队长圣旨\n\n\n\n\n1，霍格沃兹\n\n\n2，黑帽军团\n\n\n3，璀璨星河\n\n\n4，ZDZL\n\n\n5，塞尔达传说\n\n\n6，全面战争模拟器\n\n\n7，路人队\n\n\n8，LSSS理事会\n\n\n9，我要AC！\n\n\n10，AC园区\n\n\n11，绿水青山理事会\n\n\n12，ACGO第四帝国\n\n\n13，CODECRUSHERS官方分团\n\n\n14，CODECRUSHERS\n\n\n15，小白之都\n\n\n16，ZDZL鲨鲨鲨\n\n\n17，自力更生\n\n\n18，天之神\n\n\n还有，热烈庆祝复仇者联盟与黑客之都结盟！😁\n\n\n肥肠怀疑这队长没事干非常勤劳搞这么多\n\n",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 51,
                    "commentNum": 11,
                    "likeNum": 0,
                    "placeName": "广东",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 1190240,
                        "nickName": "复仇者_黑客_摆烂崽",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/b38e9b05e3ac4d32aa1bd726d9916bd2.jpg",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 36482,
                    "title": "码上开聊VOL.2 勤勉笃行-吴泽均",
                    "postId": 31795,
                    "digest": "码上开聊\n\n欢迎来到码上开聊！这是一个属于编程少年的花式聊天角，带你一起解锁大佬们的神仙操作、逆袭时刻和刷题“翻车”故事！在这里，每一个代码少年都在用青春和坚持“码”出自己的高光时刻！\n\n本期第2话，我们请来了吴泽均！他凭21次提交全红却不放弃的劲头，硬是AC了一道题，告诉我们：编程，拼的就是这口气！赶紧上车，听听他的访谈吧！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\nVOL.2 勤勉笃行-吴泽均\n\n\n\n\n> 个人档案\n\n * 姓名：吴泽均\n\n * 年级：初一\n\n * 校区：苏州新光天地校区\n\n * 爱好：编程、画画、刻橡皮章、听音游音乐\n\n * 社区主页：ACGO个人主页\n\n * 获奖经历：\n   2024年CSP-J/S（江苏）：普及组初赛一等奖，复赛二等奖。提高组初赛二等奖，复赛三等奖。\n   2024年全国青少年信息素养大赛总决赛：算法创意实践挑战赛小学组一等奖。\n   2024年蓝桥杯全国青少年总决赛：C++C++C++中级创意编程组三等奖。\n   2024年蓝桥杯青少年江苏赛区：C++C++C++中级创意编程组一等奖。\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n> 高能访谈\n\n\nQ1\n\n\nHI，你是什么时候开始学编程的？最开始觉得难吗？\n\n吴泽均：\n\n\n\n\nQ2\n\n\n从PYTHON转到C++的过程对你来说有难度吗？是怎么适应的？\n\n吴泽均：一开始确实不情愿，因为刚刚学完Python的L2，C刚接触时觉得“<<”和“>>”特别绕，还记得那次是在苏州某机构（非小码王）的冬令营被讲得一头雾水。但后来爸爸和我商量，觉得C在竞赛里会更有前途，就决定尝试一下。不过现在我还是会做些Python的项目。\n\n\nQ3\n\n\n小码王集训营的经历对你有影响吗？\n\n吴泽均：影响挺大的。2023年与2024年，我参加了两次小码王的集训营（X03和X02），有一次模拟初赛考得不太好，主要是我轻敌了，之前考得好就有点放松。后来反思觉得，不管之前成绩如何，正式比赛都不能掉以轻心。这次经历让我对比赛更重视，也更加用心。\n\n\nQ4\n\n\n在集训营的生活上有没有不适应的地方？怎么克服的？\n\n吴泽均：刚到集训营时有点不适应，白天强度高，晚上休息不太好。后来我自己调整作息，晚上尽量早睡，早上尽量早起，这样渐渐适应了强度大的学习节奏。可惜十天的相处太短，我还在社区发了一篇帖子纪念。\n\n\n\n\nQ5\n\n\n听说你在ACGO上解决了不少题目，有没有特别有挑战的？\n\n吴泽均：有的，比如“A592 搬寝室”这道题让我印象深刻。我提交了21次都错了，本来的思路是用贪心算法，样例和自测都过了，但提交全红。后来换了思路，找到了重叠部分的最大数，终于解出来了！这道题让我明白，坚持是很重要的。\n\n\n\n\nQ6\n\n\n刷题时你有什么特别的学习方法吗？\n\n吴泽均：每天有时间我都会刷题，大概每天一个多小时吧，主要是因为喜欢。我还用Excel表记录刷题进度，把ACGO上橙题、黄题、绿题都标出来，每做完一道就勾掉，成就感满满！\n\n\n\n\nQ7\n\n\n除了编程，你平时还喜欢做些什么？\n\n吴泽均：我还喜欢画画和刻橡皮章之类的美术活动，特别放松。编程的时候我也会听音游的背景音乐，感觉更有节奏感。\n\n\nQ8\n\n\n对未来的编程学习有什么目标吗？\n\n吴泽均：希望通过编程获得择校优势，目标是考上理想的高中。未来得加强自学能力，少依赖老师。对编程职业也很有兴趣，可能会考虑IT行业！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n访谈结语\n\n如果你也对编程有兴趣，欢迎和他一起加入ACGO，刷题、讨论、交流经验，一起在编程的世界里不断进步吧！\n\n\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n往期访谈\n\n\n\nVOL.1-镇站之宝Macw",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 1673,
                    "commentNum": 51,
                    "likeNum": 39,
                    "placeName": "浙江",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 36482,
                        "nickName": "AC君",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/86bef79ccff04644903237e864defff0.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": [
                            {
                                "identityId": 1,
                                "identityTitle": "管理员",
                                "identityUrl": "https://xmcdn.oss-cn-shanghai.aliyuncs.com/cpp_community/images/identity/administrator.png"
                            }
                        ]
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 1
                },
                {
                    "userId": 3298235,
                    "title": "差一点......",
                    "postId": 32296,
                    "digest": "",
                    "questionId": 7870,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 8,
                    "commentNum": 2,
                    "likeNum": 0,
                    "placeName": "北京",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 3298235,
                        "nickName": "yang（Python）",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/default.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 0
                },
                {
                    "userId": 2659353,
                    "title": "BUG",
                    "postId": 32295,
                    "digest": "这题跳过！！有BUG！",
                    "questionId": 34170,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 7,
                    "commentNum": 1,
                    "likeNum": 0,
                    "placeName": "浙江",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 2659353,
                        "nickName": "‮队团加不）ด้้童帅_者仇复",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/eef5954fcbed4a1f970735d54a70c164.jpg",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 0
                },
                {
                    "userId": 3561389,
                    "title": "双向广搜太",
                    "postId": 32285,
                    "digest": "NB",
                    "questionId": 34470,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 10,
                    "commentNum": 1,
                    "likeNum": 0,
                    "placeName": "福建",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 3561389,
                        "nickName": "不想AC",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/default.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 0
                },
                {
                    "userId": 3148818,
                    "title": "潘卓大队招人啦！等你哦~~~",
                    "postId": 20502,
                    "digest": "点击此链接即可加入潘卓大队！！！\n本团为新手团，请多多支持！\n\n💥💥💥💥💥💥欢迎进入潘卓大队！💥💥💥💥💥💥\n\n\n\n————————————————————————————————————————————\n竞赛\n30天必有一次竞赛！有：\n欢乐赛（不增加团队排位分）\n排位赛（答多少分加多少团队排位分）\n选拔赛，淘汰赛（按具体情况）\n升级赛（一月一次，前五升两级级，前二十升一级）\n以及各种节日赛！\n大家挑战一一下！\n第一届未来蓝图杯已开启报名！\n————————————————————————————————————————————\n段位\n这里分为七个大段位！\n每个大段位分为五个小段位\n100潘卓大队排位分升一大级\n20潘卓大队排位分升一小级\n初始等级由刷题质量和ACGO排位赛成绩决定\n后续还更多活动！大家尽请期待！！！\n\n\n\n————————————————————————————————————————————\n大神\n我们团有大神：AC君 ，法兰西玫瑰！！！！！！！！！！！！\n————————————————————————————————————————————\n聊天区\n#本团聊天区（建议 反馈 等有意义的讨论） ： 讨论-->灌水池塘-->搜索“潘卓大队讨论区“-->点进去-->下滑到评论区在评论区里聊即可。（72小时内必回！！！）欢迎反馈！！！\n————————————————————————————————————————————\n通知\n注意！！！第一届未来蓝图杯开始报名\n\n\n——2024.12.1\n\n————————————————————————————————————————————\n潘卓大队荣誉榜\n\n排名 昵称 排位分\n1 ------------\n2 ------------\n3 ------------\n4 ------------\n5 ------------\n6 ------------\n7 ------------\n8 ------------\n9 ------------\n10 ------------\n————————————————————————————————————————————\n作业\n有三组作业\n难度分别为简单，中等，难\n————————————————————————————————————————————\n题解\n作业：\n竞赛：",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 106,
                    "commentNum": 30,
                    "likeNum": 1,
                    "placeName": "辽宁",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 3148818,
                        "nickName": "信奥--小潘 CPZT ACGO",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/c71a693a6e774bb890d686afd5fdcb82.png",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 3973100,
                    "title": "第九期谜底",
                    "postId": 32235,
                    "digest": "第九期谜底：黄继光\n\n\n答题者：复仇者_KS\n\n\n特别鸣谢：#INCLUDE",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 10,
                    "commentNum": 2,
                    "likeNum": 0,
                    "placeName": "浙江",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 3973100,
                        "nickName": "The Chosen One",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/c0353b3ce417493fba67ed44053b5386.jpeg",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 4034229,
                    "title": "日常の整活（3）",
                    "postId": 32287,
                    "digest": "防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透防剧透\n\n今天，我在上王码小的课时，无聊的要死。于是乎，我就捉死的发了这么一段话：\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n编程网课，屏幕为纸，代码成诗，却难掩其单调乏味。虽知识如海，逻辑如网，然缺乏互动与实践，让智慧之旅变得沉闷冗长。键盘敲击声，成了唯一的旋律，屏幕的光亮，照不亮心中的激情。编程之美，似乎被无尽的讲解与习题所掩盖，期待破茧成蝶，寻回那份对技术的热爱与向往。\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n然后，老师说了那么一句：\n\n\n真是**的（好样的）\n\n喜提禁言大礼包一份哦——\n\n\n全剧终\n\n然后，美丽的课间到来了。\n\n我的禁言大礼包也没了。\n\n为了接着整活，我又发了一段：\n\n\n\n\n\n我：哎呦忘了这是电脑，打错了打错了，让我改下\n\n同学：6\n\n老师：\n\n\n老师：\n来，让我们加一个节目\n\n\n\n（开麦）\n\n（还好我的麦是坏的）\n\n（又叫了一个人来读我改好了的）\n\n同学：\n\n（笑着读完的）\n\n我：\n\n（怎么发不出去？）\n\n一看...\n\n\n禁言中\n\n...\n\n\n\n\n儒呙倪布哀握，酒拔沃德昕桓卧，倪庸哀桓奏顷淳，涡海鎏夏叻肾么？儒呙倪亥哀涡，酒肾么桦兜鳖硕，酒艮涡翼卤筐笨，酒补妖箱泰夺。赤顷补逝醉呙，魍顷补逝飒拖，微泥翔德笥忻猎飞悠绅么截郭！倪硕刀抵微深么，兜逝窝德搓！斗罢哀倾镶德钛镁仙尸胎邮霍！刀抵微深么，嚷逆耿喃呙！遮氧碍倪畜叻胺魏亥能谮么佐！\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n往期：\n\n日常の整活\n日常の整活（2）",
                    "questionId": 0,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 3,
                    "commentNum": 2,
                    "likeNum": 2,
                    "placeName": "广东",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 4034229,
                        "nickName": "哎嘿",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/8e03fcf9fb804495a0866c2cf2dd54ba.jpg",
                        "rankId": 1,
                        "blockStatus": 1,
                        "honorary": "倔强青铜",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 3,
                    "isFeatured": 0
                },
                {
                    "userId": 1590033,
                    "title": "看着简单做着难 - 排如序 - 更改说明",
                    "postId": 29520,
                    "digest": "由于更改的时间较长（5分钟左右），所以要更改的地方在这里说明。\n\n\n经测试，输出不会爆RE.\n这题看着简单做着难，理论上可过 大家可以去挑战一下.\n注意：数据是不均匀的，某个区间的数出现的次数可能特别多.（用桶排）\n\n测试点信息\n",
                    "questionId": 32590,
                    "type": null,
                    "questionTitle": null,
                    "viewNum": 158,
                    "commentNum": 26,
                    "likeNum": 3,
                    "placeName": "广东",
                    "isTop": 0,
                    "isLike": 0,
                    "updatedAt": null,
                    "content": null,
                    "userVo": {
                        "userId": 1590033,
                        "nickName": "‮队团加不）ด้้童帅_者仇复",
                        "account": null,
                        "avatar": "https://attach.acgo.cn/picture/1de1bf8af3304e91a683ca287438153d.jpeg",
                        "rankId": 4,
                        "blockStatus": 1,
                        "honorary": "尊贵铂金",
                        "userIdentities": []
                    },
                    "status": null,
                    "module": 1,
                    "isFeatured": 0
                }
            ],
            "total": 10291
        },
        "emptyType": 1,
        "tdk": {
            "title": "ACGO讨论社区-信息学编程算法训练动态最新回复-ACGO题库",
            "keywords": "ACGO讨论社区,编程算法训练,ACGO题库,编程算法训练最新回复",
            "description": "ACGO(Acgo.Cn)是专业的编程算法训练平台，ACGO致力于为参加CSP-J/S、GESP、NOIP、NOI、ACM、CSP、CCPC、ICPC竞赛的选手提供清爽、快捷的编程训练刷题体验。适合初级小白C++编程入门训练，包含CSP入门级提高级赛前集训、提高组普及组训练，ACM区域赛前多校训练营，是学习noip等竞赛时理想的网站。"
        },
        "tabs": [
            {
                "label": "最新回复",
                "key": "reply",
                "href": "/discuss/",
                "preventDefault": true
            },
            {
                "label": "最新发布",
                "key": "public",
                "href": "/discuss/?tab=public",
                "preventDefault": true
            },
            {
                "label": "精华帖",
                "key": "essence",
                "href": "/discuss/?tab=essence",
                "preventDefault": true
            }
        ]
    },
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
    },
    "__N_SSP": true
}
```

</details>

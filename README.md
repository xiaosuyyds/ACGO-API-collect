<p align="center">
    <img src="./assets/img/logo.png" width="350" height="60" alt="Logo加载不出来（悲）">
</p>

<h1 align="center">ACGO API 收集与整理</h1>
<p align="center" class="shields">
    <a href="https://github.com/xiaosuyyds/ACGO-API-collect/issues" style="text-decoration:none">
        <img src="https://img.shields.io/github/issues/xiaosuyyds/ACGO-API-collect.svg?color=lightrey&style=for-the-badge" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/xiaosuyyds/ACGO-API-collect/stargazers" style="text-decoration:none" >
        <img src="https://img.shields.io/github/stars/xiaosuyyds/ACGO-API-collect.svg?color=lightrey&style=for-the-badge" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/xiaosuyyds/ACGO-API-collect/network" style="text-decoration:none" >
        <img src="https://img.shields.io/github/forks/xiaosuyyds/ACGO-API-collect.svg?color=lightrey&style=for-the-badge" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/xiaosuyyds/ACGO-API-collect/blob/master/LICENSE" style="text-decoration:none" >
        <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?color=lightrey&style=for-the-badge" alt="GitHub license"/>
    </a>
    <br>
    <a href="https://github.com/xiaosuyyds/MuRainBot2">
        <img src="https://counter.seku.su/cmoe?name=acgoapi&theme=rule34" alt=""/>
    </a>
</p>


<h3 align="center">野生API文档，不断更新中....</h3>

本项目旨在对 [acgo.cn](https://www.acgo.cn/) 散落于世界各地的野生 API 进行收集整理，研究使用方法并对其进行说明，运用了黑箱法、控制变量法、代码逆向分析、拆包及反编译法、网络抓包法等研究办法。

***非官方文档！***

本文档探讨的对象是[acgo.cn](https://www.acgo.cn/)的API接口，若官方后续推出ACGO开放平台 或 小码王开放平台 都将不属于本项目范畴，请移步

ACGO大部分API采用GET或POST调用，目前没发现例外的接口。返回数据大多为 JSON ，基本强制使用 https 协议 。

## ⚠️️warning ⚠️声明

1. 本项目遵守 CC-BY-NC 4.0 协议，禁止一切商业使用，如需转载请注明作者
2. ***请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！***
3. 利用本项目提供的接口、文档等造成不良影响及后果与本人无关
4. 由于本项目的特殊性，可能随时停止开发或删档
5. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容

## 🎉参与贡献✨

欢迎各位 dalao 对本项目做出贡献，也希望每个使用者都能提出宝贵的意见

目前本项目存在的问题包括但不限于：

1. 部分文档较旧，修改与更新没有跟进
2. API收集不完全，本人抓包能力有限…… 欢迎各位大佬提交pr来扩增本项目的API~
3. **!!!求助 由于本人逆向能力有限，跪求各位大佬帮忙破解一下登陆API的`Csrf-Token`与密码登陆的加密方法 （目前已知信息：此token由JS本地生成）!!!**

更多信息请浏览 [贡献指南](CONTRIBUTING.md)

## 🌼鸣谢🌼

### 本仓库目录结构与文档编写均参考和借鉴了[bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)在此由衷的感谢！
#### 感谢所有为此项目做出贡献的大大~你们的存在，让社区变得更加美好！
<a href="https://github.com/xiaosuyyds/ACGO-API-collect/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=xiaosuyyds/ACGO-API-collect&max=999" alt=感谢他们（鼓掌）！>
</a>

~~其实本来只是想要做一个ACGO的爬虫~~

## 🍴目录📝

计划整理分类 & 目录：(文档已完结请选中 checkbox)
- [ ] [用户](docs/user)
  - [ ] [用户信息](docs/user/user_info.md)
  - [ ] [登陆账号(密码)](docs/user/login_password.md)
  - [ ] 发送验证码
  - [ ] 登陆账号(验证码)
  - [ ] 当前登陆账号的信息
- [ ] [题目](docs/question)
  - [ ] 获取题目信息
  - [ ] [代码提交](docs/question/submit_code.md)
  - [ ] 获取评测机信息
  - [ ] 获取题解
  - [ ] 获取题解详细信息
  - [ ] 发送题解
- [ ] [讨论](docs/discuss)
  - [ ] 讨论信息
  - [ ] [讨论列表](docs/discuss/get_list.md)
  - [ ] 发送讨论评论
  - [ ] 发送讨论
  - [ ] 获取讨论评论
- [ ] 主页
  - [ ] 主页排行榜
- [ ] 团队
  - [ ] 获取团队信息
  - [ ] 创建团队
  - [ ] 删除团队
  - [ ] 获取用户分组

## 💬交流🗨️

### ⚠️️注意：开源社群欢迎交流探讨，拒绝咨询、不支持合作

- QQ交流群 [加群链接](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=m7l22Rbe39Jpoe2MVwZBdR1GNJFCTSGO&authKey=qwwomxgR8Nudz7uVnuEj3R9mphn6%2FEVzMZ%2FviimtZKimuaJjdqsat%2FHbYuuvLNdN&noverify=0&group_code=830159613)

## ⭐StarHistory⭐

[![Star History Chart](https://api.star-history.com/svg?repos=xiaosuyyds/ACGO-API-collect&type=Date)](https://star-history.com/#xiaosuyyds/ACGO-API-collect&Date)

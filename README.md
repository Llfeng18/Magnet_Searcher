# MagnetSearcher
种子（磁力链接）搜索爬虫，爬取btsow，输出文本

本项目基于[MagnetSearcher](https://github.com/Wangrong23/MagnetSearcher) 

## 使用步骤
* 创建log和log\BT文件夹，替换`F:\log\`和`F:\log\BT`
* 按照注释修改下面的代码

```python
    # 过滤文本含以下关键字的种子
    filter = ["rar", "zip", "直播"]
    # 搜索关键字
    inputKeyWord = ["测试", "大学", ]
    # 获取对应目录的文件夹和文件名，避免重复
    file_name_listdir("F:\迅雷下载")
    # 开始爬取，20代表爬取前20页
    assemble_url(inputKeyWord, filter, 20)
```

## 说明

*   因为爬虫没有使用代理IP池（太难了还在学），全速爬取可能会被403，因此使用sleep延缓爬取速度
*   只采用了简单的过滤(和本地已经下载的文件做全文本匹配)不能很好地避免爬取重复的问题

# Thunder_Restarter
通过判断当前PC下载网速来重启迅雷软件，因为迅雷跑一段时间后下载速度后变慢，因此需要定时重启软件

## 使用步骤
* 修改bat文件夹中的迅雷下载路径
* 判断逻辑见代码，简单的轮询网速

```
cd C:\Program Files (x86)\Thunder Network\Thunder\Program
```


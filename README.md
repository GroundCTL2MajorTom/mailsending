# 网站内容定时爬取并推送邮箱脚本

利用Python爬虫、邮件发送以及定时任务实现了每天定时推送网站内容的脚本

以某儿童故事网站为例

利用request库请求访问模拟浏览器访问网页，为了保证随机性，以到某一日期的天数为变量和星期为变量拼接url

简单的使用beautifulsoap库，解析html页面，找到文本内容对应的html标签并用beautifulsoup.find函数提取

利用该网站的冷知识版面设计了每日问答环节

拼接内容完成后调用了网易邮箱的api发送

放到云上crontab -e即可实现每日推送

![image](https://github.com/GroundCTL2MajorTom/mailsending/assets/136243034/f52ba178-d109-48e6-964e-75fce65dcf8c)


## 注意
使用了第三方库 requests 和 BeautifulSoup 来进行网页爬取和解析，确保你已经安装了这些库。如果没有安装，可以使用以下命令安装：

pip install requests

pip install beautifulsoup4

使用时至少要修改末尾的邮箱地址、授权码、邮件标题、发件人名称、收件人邮箱

网页爬取涉及到法律法规和网站的使用规定。在进行网页爬取时，请确保遵守相关规定，并尊重网站的使用限制。

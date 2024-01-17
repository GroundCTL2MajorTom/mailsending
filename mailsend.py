from bs4 import BeautifulSoup
import requests
import datetime
import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header
from email.message import EmailMessage
import base64 

urllist=[]
namelist=[]
text=[]
#获取星期数
today = datetime.datetime.today().weekday()  # 获取今天是星期几，返回值为 0~6，分别表示周一到周日
i = today + 2 # 由于星期的编号是从 1 开始的，因此需要将返回值加 1
#爬取一个url
url1=f'http://www.tom61.com/ertongwenxue/zhiliwenda/index_{i}.html'
r=requests.get(url1,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding

#开始拼接具体url
url='http://www.tom61.com/'
soup=BeautifulSoup(r.text,'html.parser')
t=soup.find('dl',attrs={'class':'txt_box'})
i=t.find_all('a')
for link in i:
    urllist.append(url+link.get('href'))
    namelist.append(link.get('title'))

#获取天数
today = datetime.date.today()  # 获取今天的日期
target_date = datetime.date(2023, 7, 22)  # 设置目标日期为 2023 年 7 月 22日
delta = target_date - today  # 计算时间差
full_days = -delta.days  # 获取天数
days=full_days // 7 

#爬取问答环节的问题
question=namelist[days]
urllist=[]
namelist=[]
text=[]

#获取星期数
today = datetime.datetime.today().weekday()  # 获取今天是星期几，返回值为 0~6，分别表示周一到周日
i = today + 2 # 由于星期的编号是从 1 开始的，因此需要将返回值加 1
i = 6 if i == 0 else i - 1
url1=f'http://www.tom61.com/ertongwenxue/zhiliwenda/index_{i}.html'
r=requests.get(url1,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding


#开始拼接具体url
url='http://www.tom61.com/'
soup=BeautifulSoup(r.text,'html.parser')
t=soup.find('dl',attrs={'class':'txt_box'})
i=t.find_all('a')
for link in i:
    urllist.append(url+link.get('href'))
    namelist.append(link.get('title'))

#获取天数
today = datetime.date.today()  # 获取今天的日期
target_date = datetime.date(2023, 7, 22)  # 设置目标日期为 2023 年 7 月 22日
delta = target_date - today  # 计算时间差
full_days = -delta.days  # 获取天数
days=full_days // 7 

r=requests.get(urllist[days],timeout=30)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
t=soup.find('div',class_='t_news_txt')
for i in t.findAll('p'):

    text.append(i.text)

send_result = "\n".join(text)

#如果有下一页怎么办
i = 2
while True:
    url = f"{urllist[days].replace('.html', '')}_{i}.html"
    r = requests.get(url, timeout=30)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string
    if "404" in title:
        break
    t = soup.find('div', class_='t_news_txt')
    text = []
    for p in t.findAll('p'):
        text.append(p.text)
    send_result_i = "\n".join(text)
    send_result += send_result_i
    i += 1

answer=send_result

urllist=[]
namelist=[]
text=[]
#获取星期数
today = datetime.datetime.today().weekday()  # 获取今天是星期几，返回值为 0~6，分别表示周一到周日
i = today + 2 # 由于星期的编号是从 1 开始的，因此需要将返回值加 1

#爬取一个url
url1=f'http://www.tom61.com/ertongwenxue/shuiqiangushi/index_{i}.html'
r=requests.get(url1,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding

#开始拼接具体url

url='http://www.tom61.com/'
soup=BeautifulSoup(r.text,'html.parser')
t=soup.find('dl',attrs={'class':'txt_box'})
i=t.find_all('a')
for link in i:
    urllist.append(url+link.get('href'))
    namelist.append(link.get('title'))

#获取天数
today = datetime.date.today()  # 获取今天的日期
target_date = datetime.date(2023, 7, 22)  # 设置目标日期为 2023 年 7 月 22日
delta = target_date - today  # 计算时间差
days = -delta.days  # 获取天数
days=days // 7 
r=requests.get(urllist[days],timeout=30)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
t=soup.find('div',class_='t_news_txt')
for i in t.findAll('p'):

    text.append(i.text)

send_result = "\n".join(text)
#如果要爬取的故事内容有下一页怎么办
i = 2
while True:
    url = f"{urllist[days].replace('.html', '')}_{i}.html"
    r = requests.get(url, timeout=30)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string
    if "404" in title:
        break
    t = soup.find('div', class_='t_news_txt')
    text = []
    for p in t.findAll('p'):
        text.append(p.text)
    send_result_i = "\n".join(text)
    send_result += send_result_i
    i += 1
  
# 组装邮件内容
send_result +="\n--------------------\n今日小问答环节:\n--------------------\n\n"+question+"\n\n--------------------\n昨日答案揭晓:\n--------------------\n"+answer


#邮件发送设置
EMAIL_ADDRESS = ""     # 邮箱的地址
EMAIL_PASSWORD = ""     # 授权码
 
# 连接到smtp服务器
# smtp = smtplib.SMTP('smtp.163.com', 25)     # 未加密
# 也可以使用ssl模块的context加载系统允许的证书，在登录时进行验证
context = ssl.create_default_context()

subject = "儿童故事日推"
body = send_result
msg = MIMEText(body, 'plain', 'utf-8')
msg['subject'] = subject        # 邮件标题
from_name = "=?utf-8?B?5Y+R5Lu25Lq65rWL6K+V=?=" # 发件人,中文请使用base64编码后拼接到 B? 和 =?= 之间
msg['From'] = f'{from_name} <{EMAIL_ADDRESS}>'
msg['To'] = ""                  # 邮件的收件人
 
# 为了防止忘记关闭连接也可以使用with语句
with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtp:      # 完成加密通讯
    # 连接成功后使用login方法登录自己的邮箱
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # 方式二：使用send_message方法发送邮件信息
    smtp.send_message(msg)

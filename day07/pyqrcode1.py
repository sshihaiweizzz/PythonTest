import pyqrcode

s = "https://www.baidu.com"

url = pyqrcode.create(s)

url.svg("baidu.svg",scale=8)
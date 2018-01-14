import re
import os
import json
from urllib import parse, request


# 获取搜索歌曲Hash值
def getSongHash(keyword):
    url = "http://songsearch.kugou.com/song_search_v2?keyword="
    url_data = "&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641"
    res = request.urlopen((url + keyword + url_data)).read().decode('utf-8')
    res = json.loads(res)
    res = res['data']['lists'][0]
    hash = res['FileHash']
    name = res['FileName']
    name = name.replace('<em>', '')
    new_name = name.replace('</em>', '')
    return hash, new_name


# 得到歌曲的下载地址
def getDownUrl(hash):
    song_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash="
    song_res = request.urlopen((song_url + hash)).read().decode('utf-8')
    song_res = json.loads(song_res)
    DownUrl = song_res['data']['play_url']
    return DownUrl


# 下载歌曲文件
def DownFile(DownUrl, new_name):
    file = request.urlopen(DownUrl).read()
    with open(new_name + '.mp3', 'wb') as outfile:
        outfile.write(file)


print("*****************************************")
print("**                                     **")
print("**         感谢使用音乐下载器          **")
print("**                                     **")
print("*****************************************")
keyword = parse.quote(input("请输入需要搜索歌曲名字:"))
data = getSongHash(keyword)
DownFile(getDownUrl(data[0]), data[1])
if os.access((data[1] + '.mp3'), os.F_OK):
    print('Download File Success!')
else:
    print('Download File Failure!')
print(input('请按任意键退出程序！'))

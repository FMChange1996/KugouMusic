import re
import os
import json
from urllib import parse, request


# 获取搜索歌曲列表
def getSongList(keyword):
    url = "http://songsearch.kugou.com/song_search_v2?keyword="
    url_data = "&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641"
    res = request.urlopen((url + keyword + url_data)).read().decode('utf-8')
    res = json.loads(res)
    res = res['data']['lists']
    return res


# 打印输出列表，并等待客户输入选择
def getSongHash(List):
    x = 1
    for n in range(len(List)):
        name = repr(List[n]['FileName'])
        name = name.replace('<em>', '').replace('</em>', '').replace("'", '')
        print(str(x) + '.' + name)
        x += 1
    z = int(input('请输入需要下载歌曲的序号：'))
    z -= 1
    filename = List[z]['FileName'].replace('<em>', '').replace('</em>', '')
    filehash = List[z]['FileHash']
    return filehash, filename


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
list = getSongList(keyword)
data = getSongHash(list)
DownFile(getDownUrl(data[0]), data[1])
if os.access((data[1] + '.mp3'), os.F_OK):
    print('Download File Success!')
else:
    print('Download File Failure!')
print(input('请按任意键退出程序！'))
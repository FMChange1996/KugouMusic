# coding=utf-8
import json
from urllib import request, parse


def getSongList(name):
    name = parse.quote(name)
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=68200167999648105&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=" + name + "&g_tk=907445169&loginUin=10670374&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
    print(url)
    res = request.urlopen(url).read().decode('utf-8')
    res = json.loads(res)['data']['song']['list']
    return res


def main():
    return input('请输入要搜索歌曲的名字：')


def PrintList(list):
    x = 1
    for n in range(len(list)):
        name = repr(list[n]['title']).replace("'", '')
        singerlist = list[n]['singer']
        sinnum = len(singerlist)
        if (sinnum > 1):
            num = 0
            for num in range(len(singerlist)):
                print(singerlist[num]['name'])
                num += 1
        else:
            # print(name+"-"+singername)
            x += 1




PrintList(getSongList(main()))

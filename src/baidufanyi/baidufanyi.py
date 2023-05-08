#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import execjs
import requests


translate_api = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1683546061312_1683546061153_B9CF57zvwEi9ucshS33Sw9RqxQ4Hy7q3R6+7OWSWxMLsBy5oCfjFPS3vJFbn/ZvDSpA4LgyDOXMu6+arKIN2fpp4kpxF1+EC4ZCy9easlcT5wHQeAonIDWxwaePGve9sj1CI7vCDzYewWayortfc4/ZWX9UZ/cJEgfYcwsoC2/QnB9qJN++FubmwWqXgHkgCi8f5YLE4rjHWgXO92nbkY+zubOuOTTJk4k4GdmqVmE8VvvNWNToEOB/3sI5YhZkoVX8WzYorE3CzIo5tOxtDP4t+tgn8KFnmS7lFinGlPR1lZ5QCWntWCOvEouzGM7VyPRQM3KJ0amIWiE1+lU9+2RIPqDyIjnt+TSFc/D5LI5tb+RXON7jAm85Vuc/JCj1B3UIJzqZVe51TYAFcDVK0+RJnS4XhxxtynbSsk904XS+Wph79aEq4YDwYC4kql7xe+wohfnqche8vCxSdDcTA+0wEgqVAa3XNSxIOVbhk6IQB6rBooR1oWkBfCt7n2763NOk3kLA9uyyKpH2TmmUVng==',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=20DA1B68DFF146DE8BAC5C4A30A5DA7B:FG=1; BAIDUID_BFESS=20DA1B68DFF146DE8BAC5C4A30A5DA7B:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1683293701; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1683379718; PSTM=1683435388; BIDUPSID=A6B02F355C666D92122DD6DE8B09E0C7; ZFY=7N8w2uLmO4rr3dnuRwKlg76kUv:B3aNpgwT6MS5PxwVU:C; ab_sr=1.0.1_MzkyYWIwM2U0MWIyMWEwYTIwNmIzZGJjYjRlMDc0OGZhYjA1YmM3NGJhODk4MTVmNWVmZTQxMTgyZWU4OGMwOTY4Y2NhZDM2NzNkOGEyOWFhNGJjM2UyYjc5YjgzN2I3YjY0MjVhNjJlZjVjYTgzZDlkYTI4ODM3ZDczNmJlZGVhNDg5YTg5MTI0NTY2NTZkZjAwZDRmNGYzMzMwNDg2Mw==; H_PS_PSSID=38516_36548_38529_38469_38358_38468_38582_36804_38485_38519_38502_26350_38567_38542; BA_HECTOR=00ah8k818081a5a4842k2leo1i5hmkn1n',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_sign(query):
    with open('baidu_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('getSign', query)
    return sign


def get_result(query, sign, token):
    data = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    response = requests.post(url=translate_api, headers=headers, data=data)
    print(response.text)
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字：')
    token = "a9d9d0531a193ad984e9e32d35151e4e"
    sign = get_sign(query)
    result = get_result(query, sign, token)
    print('翻译成英文的结果为：', result)


if __name__ == '__main__':
    main()

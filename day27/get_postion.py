# coding=utf-8
import os
import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_postion(position_id, postion_dir):
    # 构造请求数据
    url = "https://www.lagou.com/jobs/%s.html" % (position_id)
    headers = {
        'Cookie': 'TG-TRACK-CODE=index_search; SEARCH_ID=e8222f3471a44abf85093f79d876f759; JSESSIONID=ABAAABAABEEAAJA080B57268659EBB1C73E65E8835B1D1D; WEBTJ-ID=20181111160721-16701cf96c8949-0fc6f60feec025-48183706-1024000-16701cf96c94d2; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541944837; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541923641,1541944111; LGRID=20181111215853-ec514a2a-e5b9-11e8-9aa0-525400f775ce; LGSID=20181111214647-3bdcc9f7-e5b8-11e8-9a9f-525400f775ce; _ga=GA1.2.1318630155.1541923641; _gat=1; _gid=GA1.2.1216768844.1541923642; PRE_HOST=www.baidu.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xf57dfecd000124aa%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D0%26oq%3Dpython%252520%2525E6%252595%2525B0%2525E6%25258D%2525AE%2525E6%25258C%252596%2525E6%25258E%252598%26rsv_t%3De111J%252FhqMM1XxboP3SPnY%252Fw6ah3WItaAjhCUX2DgoGHa814Syn2DSmf%252F0Kh31gQZTnH%252B%26inputT%3D6259%26rsv_pq%3D918956f400061b60%26rsv_sug3%3D280%26rsv_sug1%3D254%26rsv_sug7%3D100%26bs%3Dpython%2520%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598; PRE_UTM=m_cf_cpt_baidu_pc; index_location_city=%E5%85%A8%E5%9B%BD; LGUID=20181111160538-9328c957-e588-11e8-9a22-525400f775ce; user_trace_token=20181111160538-9328c039-e588-11e8-9a22-525400f775ce',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://www.lagou.com/',
        'Connection': 'keep-alive'
    }
    session = requests.Session()
    session.headers = headers
    response = session.get(url)
    doc = response.content.decode()
    soup = BeautifulSoup(doc, 'html.parser')
    # soup = BeautifulSoup(response.content,'html.parser',from_encoding = 'utf-8')
    try:
        re = soup.findChild(name='dd', class_='job_bt')
        rr = re.find("div").find_all("p")
        if not os.path.exists(postion_dir + "/"):
            # print("不存在")
            os.mkdir(postion_dir + "/")
        with open(postion_dir + "/%s.txt" % (position_id), 'w') as fd:
            for p in rr:
                # print(p)
                fd.write(p.text + "\n")
    except:
        pass


pd_reader = pd.read_csv("jobs.csv", encoding="utf-8")
pd_reader = pd_reader.dropna()
headers = ['工作年限', '学历', '职位', '职位ID', '薪水', '城市', '发布时间']
idx = 0
for postion_id in pd_reader['职位ID']:
    print("爬取职位：%s" % (pd_reader['职位'][idx]))
    get_postion(postion_id, pd_reader['薪水'][idx])
    idx += 1
    time.sleep(random.uniform(1, 3))

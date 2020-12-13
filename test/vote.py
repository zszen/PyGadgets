import requests
print('投票')
res = requests.post('https://api.cuidc.net/api/publicity/thumb?projectId=4489&publicityId=1',headers={'Referer': 'https://www.cuidc.net/','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0'})
print('投票页面失效') if res.status_code== 404 else print(f'投票结果: {res.text}')

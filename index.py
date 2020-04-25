import requests

url = 'https://api.covid19india.org/state_district_wise.json'
r = requests.get(url).json()
l = list(r)
for i in l:
    print('*'*96)
    print(i,end='\t\t')
    for i in list(r[i]['districtData']):
        print(i, end='\t|\t')



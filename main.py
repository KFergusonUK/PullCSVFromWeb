from io import StringIO
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

url="https://storage.googleapis.com/dft-statistics/road-traffic/downloads/data-gov-uk/region_traffic_by_vehicle_type.csv"
s=requests.get(url, headers= headers).text

print(s)

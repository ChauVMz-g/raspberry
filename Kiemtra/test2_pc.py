
from urllib import request, parse, error
from time import sleep
import json

CHANNEL_ID = "3570604"
API_KEY_READ = "OJ6MI36OSJMSZ61Y"
BASE_URL = "https://api.thingspeak.com"

def thingspeak_read(fields=(1, 2)):
    query = parse.urlencode({"api_key": API_KEY_READ})
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/feeds/last.json?{query}"
    with request.urlopen(url, timeout=10) as r:
        data = json.loads(r.read().decode())
    if not isinstance(data, dict):      # kênh trống
        return None
    return {f: data.get(f"field{f}") for f in fields}

def main():
    while True:
        try:
            value = thingspeak_read(fields=(1,2))
            if value is None:
                print("Chưa có dữ liệu")
            else:
                print(f"Cường độ ánh sáng: {value[1]}")
                print(f"Khoảng cách: {value[2]}")
        except (error.URLError, TimeoutError, ValueError) as e:
            print("Lỗi:", e)
        
        print("-" * 25)
        sleep(18)

if __name__ == "__main__":
    main()
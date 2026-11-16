from urllib import request, parse, error
from time import sleep
import json
from random import randint

#Channel TEST
CHANNEL_ID = "3570604"
AUTHOR = "mwa0000037711030"
API_KEY_WRITE = "KG8ED62ME1SB70C7"
API_KEY_READ = "OJ6MI36OSJMSZ61Y"
BASE_URL = "https://api.thingspeak.com"


def thingspeak_write(fields):
    body = parse.urlencode({f"field{k}": v for k, v in fields.items()}).encode()
    req = request.Request(f"{BASE_URL}/update", data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("X-THINGSPEAKAPIKEY", API_KEY_WRITE)
    with request.urlopen(req, timeout=10) as r:
        return r.read().decode()

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
        value1 = randint(0, 50)
        value2 = randint(50, 100)
        try:
            entry_id = thingspeak_write({1: value1, 2: value2})
            if (entry_id == "0"):
                print("Gửi dữ liệu thất bại")
            else:
                print("Đã gửi dữ liệu lên server thingspeak.")

            sleep(2)
            value = thingspeak_read(fields=(1,2))
            if value is None:
                print("Chưa có dữ liệu")
            else:
                print(f"Kết quả: {value[1]} {value[2]}")
        except (error.URLError, TimeoutError, ValueError) as e:
            print("Lỗi:", e)
        
        print("-" * 25)
        sleep(18)

if __name__ == "__main__":
    main()
import paho.mqtt.client as mqtt
from time import sleep
from random import randint

# Thông tin cấu hình ThingSpeak
channelId = "3568107"
username = 'PAYoOyQgKgIEGgAHDy8cGgw'
clientId = 'PAYoOyQgKgIEGgAHDy8cGgw'
password = 'eD7A/jynesN0/F1yDfR/EEwI'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[MQTT] Đã kết nối thành công tới ThingSpeak Broker!")
        # Subscribe vào topic lắng nghe field3 (hoặc toàn bộ channel)
        topic_sub = f"channels/{channelId}/subscribe/fields/field3"
        client.subscribe(topic_sub)
        print(f"[MQTT] Đã đăng ký lắng nghe topic: {topic_sub}\n")
    else:
        print(f"[MQTT] Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, message):
    # Hàm này sẽ TỰ ĐỘNG CHẠY và IN dữ liệu mỗi khi ThingSpeak nhận/nhả dữ liệu mới về
    print("----------------------------------------")
    print(f"DỮ LIỆU NHẬN ĐƯỢC TỪ THINGSPEAK:")
    print(f">Topic  : {message.topic}")
    print(f">Payload: {message.payload.decode()}")
    print("----------------------------------------\n")

# --- 2. KHỞI TẠO CLIENT VÀ GÁN CALLBACK ---

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, clientId)
client.username_pw_set(username=username, password=password)

client.on_connect = on_connect
client.on_message = on_message

# --- 3. KẾT NỐI VÀ CHẠY LOOP NGẦM ---

client.connect("mqtt3.thingspeak.com", 1883, 60)

# BẮT BUỘC: loop_start() để chạy luồng xử lý mạng ngầm (nhận dữ liệu callback on_message)
client.loop_start()

# --- 4. VÒNG LẶP GỬI DỮ LIỆU ---

def thingspeak_mqtt(data):
    topic_pub = f"channels/{channelId}/publish"
    payload = f"field3={data}&status=MQTTPUBLISH"
    client.publish(topic_pub, payload)

try:
    while True:
        data_random = randint(0, 50)
        print(f"🚀 Đang gửi ngẫu nhiên: {data_random} lên field3...")
        thingspeak_mqtt(data_random)
        
        # Chờ 20 giây trước khi gửi tiếp
        sleep(20)

except KeyboardInterrupt:
    print("\nĐang ngắt kết nối...")
    client.loop_stop()
    client.disconnect()
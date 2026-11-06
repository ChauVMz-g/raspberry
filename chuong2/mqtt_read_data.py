import paho.mqtt.client as mqtt

# Cấu hình thông tin tài khoản ThingSpeak
channelId = "3568107"
username = 'PAYoOyQgKgIEGgAHDy8cGgw'
clientId = 'PAYoOyQgKgIEGgAHDy8cGgw'
password = 'eD7A/jynesN0/F1yDfR/EEwI'

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code: {}".format(rc))
    if rc == 0:
        # Subscribe vào field3 của channelId truyền từ biến cấu hình
        topic = "channels/%s/subscribe/fields/field3" % (channelId)
        client.subscribe(topic)
        print("Subscribed to topic:", topic)

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")

def on_message(client, userdata, message):
    print("Received payload:", message.payload.decode())
    print("From topic:", message.topic)

# Khởi tạo client kèm theo CallbackAPIVersion.VERSION1 để tương thích paho-mqtt 2.x
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, clientId)

# Gán các hàm callback
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Thiết lập username và password thực tế từ biến
client.username_pw_set(username=username, password=password)

# Kết nối và bắt đầu vòng lặp lắng nghe dữ liệu
print("Connecting to ThingSpeak MQTT broker...")
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()
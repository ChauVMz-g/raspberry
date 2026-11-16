import paho.mqtt.client as mqtt

CHANNEL_ID = "3570604"
USERNAME = "GwsKIxkcJjwLJDQZIzo0HhI"
CLIENT_ID = "GwsKIxkcJjwLJDQZIzo0HhI"
PASSWORD = "b5qzB0nVn/OeoXc787/zQcz6"
BROKER = "mqtt3.thingspeak.com"
PORT = 1883

def thingspeak_subscribe(fields, on_data, channel_id=CHANNEL_ID):
    topics = [(f"channels/{channel_id}/subscribe/fields/field{f}", 0) for f in fields]

    def on_connect(client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print("Kết nối thất bại:", reason_code)
            return
        client.subscribe(topics)
        print("Đã subscribe:", [t for t, _ in topics])

    def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
        print("Mất kết nối với broker")

    def on_message(client, userdata, message):
        field = int(message.topic.rsplit("field", 1)[-1])  # ".../field3" -> 3
        on_data(field, message.payload.decode())

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    print("Đang kết nối tới ThingSpeak MQTT...")
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

def show(field, value):
    print(f"field{field} = {value}")


if __name__ == "__main__":
    FIELDS = (1, 2)
    try:
        thingspeak_subscribe(FIELDS, show)
    except KeyboardInterrupt:
        print("\nĐã dừng.")
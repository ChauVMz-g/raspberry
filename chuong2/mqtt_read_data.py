# Channel ID:
# Author:
# Username:
# Password:

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code {}".format(rc))
    channel_ID = "CHANNEL_ID"

    #subscribes to updates to a channel field from a private channel
    client.subscribe("channels/%s/subscribe/fields/field3" % (channel_ID))


def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")

def on_mesage(client, userdata, message):
    print(message.payload.decode())
    #print(message.topic)

client_id = "CLIENT_ID"
client = mqtt.Client(client_id)\

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_mesage
client.username_pw_set(username = "USER_NAME", password = "PASSWORD")
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()
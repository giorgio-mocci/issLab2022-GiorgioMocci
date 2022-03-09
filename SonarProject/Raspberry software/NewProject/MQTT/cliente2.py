from paho.mqtt.client import Client

client = Client("Publisher_test")

def on_publish(client, userdata, mid):
    print("Messaggio pubblicato")

client.on_publish = on_publish

client.connect("localhost")
client.loop_start()

messaggio = "prova testo"
client.publish(topic = "test", payload = messaggio)
client.publish(topic = "marco", payload = messaggio)
client.loop_stop()
client.disconnect()

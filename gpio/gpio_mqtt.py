import mqtt_helper as mh
import signal 
import time

class App:

    def __init__(self):
        # TODO setup LEDs
        # TODO setup pushbuttons 

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/jessophc/#",
                                 publish_topic_name="me435/jessophc/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Receved type: " + str(message_type))
        print("Receved payload: " + str(message_payload))

def main():
    print("GPIO MQTT")
    app = App()

    while True:
        # Send test message!
        app.mqtt_client.send_message("red","on")
        time.sleep(1)
        app.mqtt_client.send_message("red","off")
        time.sleep(1)



    signal.pause() # keeps the program alive, but does nothing on its own 



main()

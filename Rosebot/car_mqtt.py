# use this for exam 3, lab 6
import rosebot
import mqtt_helper as mh
import signal
import time

class App:

    def __init__(self):
        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/jessophc/#",
                                 publish_topic_name="me435/jessophc/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Receved type: " + str(message_type))
        print("Receved payload: " + str(message_payload))

        if message_type == "set_speeds":
            self.robot.drive_system.set_speeds(message_payload[0], message_payload[1], message_payload[2], message_payload[3])
        if message_type == "stop":
            self.robot.drive_system.set_speeds(0, 0, 0, 0)
        if message_type == "beep"
            self.robot.buzzer.beep(on_time=0.1, off_time=0.3, n=2)

def main():
    print("CAR MQTT")
    app = App()

    while True:
        # Send test message!
        app.mqtt_client.send_message("set_speeds", [40, 40, 40, 40])
        time.sleep(1)
        app.mqtt_client.send_message("set_speeds", [0, 0, 0, 0])
        time.sleep(1)

    except KeyboardInterrupt:
        print("goodbye")
        app.robot.drive_system.stop()
        app.mqtt_client.





    signal.pause() # keeps the program alive, but does nothing on its own 



main()
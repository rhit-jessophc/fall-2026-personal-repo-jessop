import gpiozero as gz
import time
import signal


def basic_on_off():
    print("Basic On / Off")
    green_led = gz.DigitalInputDevice(18)
    green_led.on()
    time.sleep(3)
    green_led.off()

def fancy_leds():
    print("Fancy Leds")
    red_led     = gz.LED(14)
    yellow_led  = gz.LED(15)
    green_led   = gz.LED(18)

    # green_led.on()
    # time.sleep(3)
    # green_led.off()

    # yellow_led.blink(on_time=3, off_time=0.1, n=3, background=False) # code will not proceed until this is done when false

    yellow_led.blink(on_time=2, off_time=0.1)
    signal.pause()


def led_board():
    print("Led Board")
    led_board = gz.LEDBoard(14,15,18, pwm=True)

    for i in range(5):
        # make loop that runs 5 times
        #turn on all leds
        led_board.on()
        time.sleep(1)
        # turn off all leds
        led_board.off()
        time.sleep(1)
        #Turn on just Red and Green
        led_board.value = (1,0,1)
        time.sleep(1)
        led_board.off()
        # turn on just yellow at 0.5 brightness
        led_board.value = (0,0.5,0)
        time.sleep(1)



def main():
    print("Leds")
    # fancy_leds()
    led_board()


    


main()


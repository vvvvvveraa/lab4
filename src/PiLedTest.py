# System imports
from time import sleep

# Local imports
from hal import hal_led as led
from hal import hal_input_switch as switch  # Import the switch module

def blink_led():
    # Initialize LED and switch
    led.init()
    switch.init()  # Initialize the switch

    while True:
        switch_state = switch.read()  # Read the switch state
        if switch_state == 0:  # Switch in the left position
            delay = 0.1  # 5 Hz frequency = 0.1 seconds delay
            led.set_output(0, 1)
            sleep(delay)
            led.set_output(0, 0)
            sleep(delay)
        else:  # Switch in the right position
            # Blink at 10 Hz for 5 seconds, then turn off
            for _ in range(int(5 / 0.05)):  # 10 Hz frequency = 0.05 seconds delay, run for 5 seconds
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
            led.set_output(0, 0)  # LED OFF
            sleep(0.1)  # Small delay to avoid busy-waiting

def main():
    # Blink LED based on switch position
    blink_led()

# Main entry point
if __name__ == "__main__":
    main()

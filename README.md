# motor-control
Use a Raspberry Pi and Adafruit MotorHat to control a stepper motor.
This scheme uses two GPIO pins, 17 and 22 to connect push buttons.
As the inputs are pulled up the push buttons set them low.
As a button is pushed and held the stepper motor starts slowly and exponentially increases
its speed until a final speed is reached.

One button will cause the motor to turn clockwise and the other counter-clockwise.

File `etc_rc.local` needs to be copied to the `/etc` directory and the invocation path
adjusted to where the python script is located.

The log file `/var/motor.log` should be empty, unless there is some kind of error.

def on_button_pressed_a():
    global RollAngle, ServoAngle
    basic.pause(100)
    RollAngle = input.rotation(Rotation.ROLL)
    ServoAngle = Math.map(RollAngle, -60, 60, 30, 150)
    basic.show_icon(IconNames.MEH)
    basic.pause(500)
    led.stop_animation()
    pins.servo_write_pin(AnalogPin.P0, ServoAngle)
    basic.pause(2000)
    pins.servo_set_pulse(AnalogPin.P0, 0)
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.pause(100)
    basic.show_icon(IconNames.HEART)
    basic.show_number(ServoAngle)
    basic.pause(500)
    basic.show_number(ServoAngle)
    basic.show_number(PitchAngle)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global PitchAngle, ServoAngle
    basic.pause(100)
    PitchAngle = input.rotation(Rotation.PITCH)
    ServoAngle = Math.map(PitchAngle, -60, 60, 45, 135)
    basic.show_icon(IconNames.HOUSE)
    basic.pause(500)
    led.stop_animation()
    pins.servo_write_pin(AnalogPin.P1, ServoAngle)
    basic.pause(2000)
    pins.servo_set_pulse(AnalogPin.P1, 0)
    basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

PitchAngle = 0
ServoAngle = 0
RollAngle = 0
pins.servo_write_pin(AnalogPin.P0, 90)
basic.pause(2000)
pins.servo_write_pin(AnalogPin.P1, 90)
basic.pause(2000)
pins.servo_set_pulse(AnalogPin.P0, 0)
pins.servo_set_pulse(AnalogPin.P1, 0)

def on_forever():
    pass
basic.forever(on_forever)

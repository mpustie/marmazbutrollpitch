input.onButtonPressed(Button.A, function () {
    basic.pause(100)
    RollAngle = input.rotation(Rotation.Roll)
    ServoAngle = Math.map(RollAngle, -60, 60, 55, 125)
    basic.showIcon(IconNames.Meh)
    basic.pause(500)
    led.stopAnimation()
    pins.servoWritePin(AnalogPin.P0, ServoAngle)
    basic.pause(2000)
    pins.servoSetPulse(AnalogPin.P0, 0)
    basic.pause(1000)
})
input.onButtonPressed(Button.AB, function () {
    basic.pause(100)
    basic.showIcon(IconNames.Heart)
    basic.showNumber(ServoAngle)
    basic.pause(500)
    basic.showNumber(ServoAngle)
    basic.showNumber(PitchAngle)
})
input.onButtonPressed(Button.B, function () {
    basic.pause(100)
    PitchAngle = input.rotation(Rotation.Pitch)
    ServoAngle = Math.map(PitchAngle, -60, 60, 45, 135)
    basic.showIcon(IconNames.House)
    basic.pause(500)
    led.stopAnimation()
    pins.servoWritePin(AnalogPin.P1, ServoAngle)
    basic.pause(2000)
    pins.servoSetPulse(AnalogPin.P1, 0)
    basic.pause(1000)
})
let PitchAngle = 0
let ServoAngle = 0
let RollAngle = 0
pins.servoWritePin(AnalogPin.P0, 90)
basic.pause(2000)
pins.servoWritePin(AnalogPin.P1, 90)
basic.pause(2000)
pins.servoSetPulse(AnalogPin.P0, 0)
pins.servoSetPulse(AnalogPin.P1, 0)
basic.forever(function () {
	
})

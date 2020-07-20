def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P2, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)

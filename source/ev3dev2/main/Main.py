from ev3dev2.Motor import SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor


def main():
    m = MoveTank('OUTPUT_A', 'OUTPUT_B')
    m.on_for_degrees(SpeedPercent(40), SpeedPercent(-40), 380, brake=True, block=False)
    m.on_for_degrees(SpeedPercent(20), SpeedPercent(20), 1500, brake=True, block=False)

    cs = ColorSensor('INPUT_3')
    while True:
        if cs.color != 0:
            print(cs.color)
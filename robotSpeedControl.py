from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)


while True:
    tinybit.car_run(0, 0)
    sleep(1000)
    tinybit.car_run(50, 50)
    sleep(1000)
    tinybit.car_run(150, 150)
    sleep(1000)
    tinybit.car_run(250, 250)
    sleep(1000)
    tinybit.car_run(300, 300)
    sleep(1000)
    tinybit.car_run(50, 50)
    sleep(1000)

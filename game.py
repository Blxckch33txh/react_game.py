from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time, random

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)

but_2 = Pin(28, Pin.IN, Pin.PULL_UP)
but_1 = Pin(27, Pin.IN, Pin.PULL_UP)


def buttonPressed(button):
    if button.value() == 0:
        return True
    else:
        return False
    
# a fancy animation for the beginning
def screen():
    i = 0
    while True:
        for i in range(128):
            oled.fill_rect(0, 0, 128, 68, 0)
            oled.fill_rect(0 + i, 0 + round(i/2), 25, 25, 1)
            oled.fill_rect(103 - i, 43 - round(i/2), 25, 25, 1)
            i += 1
            oled.show()
            time.sleep(.01)
            if buttonPressed(but_1) and buttonPressed(but_2) == True:
                break
        if buttonPressed(but_1) and buttonPressed(but_2) == True:
            break

def wait():
    for i in range(2000):
        if buttonPressed(but_1) or buttonPressed(but_2) == True:
            break
        time.sleep(.001)
        i += 1

# animation of the bomb
def draw_bomb():
    oled.fill_rect(54, 20, 20, 20, 1)
    oled.vline(53, 22, 16, 1)
    oled.vline(74, 22, 16, 1)
    oled.vline(52, 24, 12, 1)
    oled.vline(75, 24, 12, 1)
    oled.vline(51, 26, 8, 1)
    oled.vline(76, 26, 8, 1)
    oled.hline(56, 19, 16, 1)
    oled.hline(56, 40, 16, 1)
    oled.hline(58, 18, 12, 1)
    oled.hline(58, 41, 12, 1)
    oled.hline(60, 17, 8, 1)
    oled.hline(60, 42, 8, 1)
    oled.fill_rect(62, 14, 4, 3, 1)
    oled.fill_rect(63, 10, 1, 4, 1)
    oled.fill_rect(62, 7, 3, 3, 1)
    oled.pixel(61, 8, 1)
    oled.pixel(65, 8, 1)
    oled.fill_rect(63, 6, 2, 1, 1)
    oled.pixel(60, 5, 1)
    oled.pixel(59, 4, 1)
    oled.pixel(67, 5, 1)
    oled.pixel(68, 4, 1)
    oled.pixel(63, 4, 1)
    oled.pixel(63, 3, 1)
    oled.show()
    
# animation of the juwel
def draw_juwel():
    for i in range(10):
        oled.fill_rect(54-i, 7+i, 20 + 2*i, 1, 1)
    oled.fill_rect(44, 17, 40, 4, 1)
    for j in range(20):
        oled.fill_rect(44+j, 21+j, 40 - 2*j, 1, 1)
    oled.show()
    

p1 = 0
p2 = 0
oled.text(str(p1), 15, 50)
oled.text(str(p2), 113, 50)
oled.show()
r = random.randint(0,2)

while True:
    p1 = 0
    p2 = 0
    screen()
    while True:
        oled.fill_rect(0, 0, 128, 68, 0)
        oled.text(str(p1), 10, 50)
        oled.text(str(p2), 118, 50)
        oled.show()
        r = random.randint(0,1)
        time.sleep(random.uniform(0.5, 3))
        if r == 0:
            draw_juwel()
            wait()
            if buttonPressed(but_1) == True:
                oled.fill_rect(0, 30, 128, 28, 0)  
                p1 += 1
                oled.text(str(p1), 10, 50)
                oled.text(str(p2), 118, 50)
                oled.show()
                if p1 == 3:
                    x = 0.15
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.text("Player 1 wins!", 0, 34)
                    oled.show()
                    time.sleep(3)
                    break
                continue
            elif buttonPressed(but_2) == True:
                oled.fill_rect(0, 30, 128, 28, 0)  
                p2 += 1
                oled.text(str(p1), 10, 50)
                oled.text(str(p2), 118, 50)
                oled.show()
                if p2 == 3:
                    x = 0.15
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 1)
                    oled.show()
                    time.sleep(x)
                    oled.fill_rect(0, 0, 128, 68, 0)
                    oled.show()
                    time.sleep(x)
                    oled.text("Player 2 wins!", 0, 34)
                    oled.show()
                    time.sleep(3)
                    break
                continue

        else:
            draw_bomb()
            wait()
            if buttonPressed(but_1) == True:
                oled.fill_rect(0, 40, 128, 28, 0)
                if p1 != 0:
                    p1 -= 1
                oled.text(str(p1), 10, 50)
                oled.text(str(p2), 118, 50)
                oled.show()
                continue
            elif buttonPressed(but_2) == True:
                oled.fill_rect(0, 40, 128, 28, 0)  
                if p2 != 0:
                    p2 -= 1
                oled.text(str(p1), 10, 50)
                oled.text(str(p2), 118, 50)
                oled.show()
                continue
        continue    

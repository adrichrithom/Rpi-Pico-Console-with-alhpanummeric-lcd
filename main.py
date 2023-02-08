import time
from machine import Pin
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import random

btn_a = Pin(2, Pin.IN, Pin.PULL_DOWN)
btn_b = Pin(3, Pin.IN, Pin.PULL_DOWN)
lastline = 2
r = 15
homesc = 1
site = 1
bput = 0
bput2 = 0
speed = 10
score = 0
ki_switch = Pin(4, Pin.OUT)
site = 1
line = 0

I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
bp = 15
col = 15
col2= 15

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.move_to(4, 0)
lcd.putstr("rective")
time.sleep(0.05)
lcd.move_to(1, 1)
lcd.putstr("entertainment")
time.sleep(1)
lcd.clear()
lcd.move_to(3, 0)
lcd.putstr("Dinorunner")
lcd.move_to(4, 1)
lcd.putstr("Tester")
dgame = False
pressed = False
sgame = False
def d_game():
    global score
    global col
    global bput
    global speed
    global col2
    global bput2
    bput = 0
    speed = 10
    col = 15
    bput2 = 10
    col2 = 10
    score = 0
    if dgame == False:
        lcd.clear()
        lcd.custom_char(0, bytearray([0x0F,
          0x15,
          0x11,
          0x17,
          0x14,
          0x16,
          0x14,
          0x1C]))
        lcd.custom_char(1, bytearray([0x1F,
          0x11,
          0x1F,
          0x11,
          0x11,
          0x1F,
          0x11,
          0x1F]))
        lcd.move_to(0, 1)
        lcd.putchar(chr(0))
            
        while True:
            print(col)
            if col == col2:
                col = 15
                lcd.move_to(col, 1)
                bput = 0
                lcd.putstr(" ")
            if col == 0:
                if not btn_a.value():
                    lcd.move_to(4, 0)
                    lcd.putstr("GAMEOVER")
                    time.sleep(2)
                    home()
                    break
            if col2 == 0:
                if btn_a.value():
                    lcd.move_to(4, 0)
                    lcd.putstr("GAMEOVER")
                    time.sleep(2)
                    home()
                    break
            if col == -1:
                col = 15
            if bput == 11:
                bput = 0
            if col2 == -1:
                col2 = 9
            if bput2 == 11:
                bput2 = 0
            if btn_a.value():
                lcd.move_to(0, 0)
                lcd.putchar(chr(0))
                lcd.move_to(0, 1)
                lcd.putstr(" ")
            else:
                lcd.move_to(0, 1)
                lcd.putchar(chr(0))
                lcd.move_to(0, 0)
                lcd.putstr(" ")
            if bput == speed:
                score += 1
                lcd.move_to(col, 1)
                lcd.putchar(chr(1))
                col -= 1
                lcd.putstr(" ")
            if bput2 == speed:
                score += 1
                lcd.move_to(col2, 0)
                lcd.putchar(chr(1))
                col2 -= 1
                lcd.putstr(" ")
            bput += 1
            bput2 += 1


pp = 0
pp2 = 0
pcol = 15
pcol2 = 11
bcol = 1
bp = 0


def s_game():
    global line
    global lastline
    global pp
    global pcol
    global pp2
    global pcol2
    global bcol
    global bp
    pp = 0
    pp2 = 0
    pcol = 15
    pcol2 = 11
    bcol = 1
    bp = 0
    lcd.clear()
    lcd.custom_char(2, bytearray([
          0x10,
          0x08,
          0x07,
          0x01,
          0x01,
          0x07,
          0x08,
          0x10]))
    lcd.custom_char(3, bytearray([
          0x00,
          0x0E,
          0x11,
          0x11,
          0x11,
          0x0E,
          0x00,
          0x00]))
    lcd.custom_char(4, bytearray([
          0x00,
          0x00,
          0x00,
          0x1F,
          0x00,
          0x00,
          0x00,
          0x00]))
    while True:
        print(pcol)
        if btn_b.value():
            line += 1
            time.sleep(0.1)
        if line == 2:
            line = 0
        lcd.move_to(0, line)
        lcd.putchar(chr(2))
        if line == 0:
            lcd.move_to(0, 1)
            lcd.putstr(" ")
        if line == 1:
            lcd.move_to(0, 0)
            lcd.putstr(" ")
            ############
        if pp == 10:
            lcd.move_to(pcol, 0)
            lcd.putchar(chr(3))
            lcd.putstr(" ")
            pcol -= 1
        if pp == 10:
            pp = 0
        if pcol == -1:
            pcol = 15
            #############
        if pp2 == 10:
            lcd.move_to(pcol2, 1)
            lcd.putchar(chr(3))
            lcd.putstr(" ")
            pcol2 -= 1
        if pp2 == 10:
            pp2 = 0
        if pcol2 == -1:
            pcol2 = 11
        ##################
        if btn_a.value():
            lcd.move_to(1, line)
            lcd.putchar(chr(4))
            bcol = 1
            lastline = line
        if bp == 5:
            bp = 0
            lcd.move_to(bcol, lastline)
            lcd.putstr(" ")
            lcd.putchar(chr(4))
            bcol += 1
        if bcol == pcol:
            if lastline == 0:
                pcol = 15
        if bcol == pcol2:
            if lastline == 1:
                pcol2 = 11
        #################
        if pcol == 0:
            lcd.move_to(4, 0)
            lcd.putstr("GAMEOVER")
            time.sleep(2)
            home()
            break
        if pcol2 == 0:
            lcd.move_to(4, 0)
            lcd.putstr("GAMEOVER")
            time.sleep(2)
            home()
            break
                
            
        bp +=1 
        pp +=1
        pp2 +=1
        
        
ccol = 0
cp = 0
line = 0
lastline = 1
cline = 1
def a_game():
    lcd.clear()
    global ccol
    global cp
    global lastline
    global line
    global cline
    ccol = 0
    cp = 0
    line = 0
    lastline = 1
    cline = 1
    lcd.custom_char(5, bytearray([
              0x00,
              0x00,
              0x00,
              0x1E,
              0x1D,
              0x1F,
              0x11,
              0x00]))
    while True:
        print(ccol)
        if btn_b.value():
            line += 1
            time.sleep(0.1)
        if line == 2:
            line = 0
        lcd.move_to(7, line)
        lcd.putchar(chr(5))
        if line == 0:
            lcd.move_to(7, 1)
            lcd.putstr(" ")
        if line == 1:
            lcd.move_to(7, 0)
            lcd.putstr(" ")
        if cp == 7:
            cp = 0
            lcd.move_to(ccol, cline)
            lcd.putstr(" ")
            lcd.putchar(chr(5))
            ccol += 1
        if ccol == 16:
            ccol = 0
            cp = 0
            cline = random.randint(0, 1)
        if cline == line:
            if ccol == 7:
                lcd.move_to(4, 0)
                lcd.putstr("GAMEOVER")
                time.sleep(2)
                home()
                break
        cp += 1

def dinofighter():
    global speed
    global col
    global bput
    global col2
    global speed2
    global bput2
    global score
    score = 0
    bput2 = 0
    speed2 = 5
    col2 = 15
    col = 0
    bput = 0
    speed = 10
    lcd.clear()
    lcd.custom_char(0, bytearray([0x0F,
          0x15,
          0x11,
          0x17,
          0x14,
          0x16,
          0x14,
          0x1C]))
    lcd.custom_char(1, bytearray([
             0x00,
              0x04,
              0x04,
              0x04,
              0x04,
              0x0E,
              0x04,
              0x00]))
    lcd.custom_char(2, bytearray([
            0x1E,
            0x15,
            0x11,
            0x1D,
            0x05,
            0x0D,
            0x05,
            0x07]))
    lcd.custom_char(3, bytearray([0x1F,
          0x11,
          0x1F,
          0x11,
          0x11,
          0x1F,
          0x11,
          0x1F]))
    lcd.move_to(7, 1)
    lcd.putchar(chr(0))
    while True:
        lcd.move_to(4, 0)
        lcd.putstr("score: " + str(score))
        if bput == speed:
            col += 1
            lcd.move_to(col-1, 1)
            lcd.putstr(" ")
            lcd.move_to(col, 1)
            lcd.putchar(chr(3))
            bput = 0
        if col == 6:
            if btn_a.value():
                if btn_b.value():
                    col = 0
                    speed = random.randint(5, 10)
                    score += 1
            if not btn_a.value():
                lcd.move_to(4, 0)
                lcd.putstr("GAMEOVER")
                time.sleep(2)
                home()
                break
            if not btn_b.value():
                lcd.move_to(4, 0)
                lcd.putstr("GAMEOVER")
                time.sleep(2)
                home()
                break
        ##########################    
        if bput2 == speed2:
            col2 -= 1
            lcd.move_to(col2+1, 1)
            lcd.putstr(" ")
            lcd.move_to(col2, 1)
            lcd.putchar(chr(3))
            bput2 = 0
            
        if col2 == 8:
            if btn_a.value():
                if not btn_b.value():
                    col2 = 15
                    speed2 = random.randint(5, 10)
                    score += 1
            if not btn_a.value():
                lcd.move_to(4, 0)
                lcd.putstr("GAMEOVER")
                time.sleep(2)
                home()
                break
            if btn_b.value():
                lcd.move_to(4, 0)
                lcd.putstr("GAMEOVER")
                time.sleep(2)
                home()
                break
            
        if btn_b.value():
            lcd.move_to(7, 1)
            lcd.putchar(chr(2))
        else:
            lcd.move_to(7, 1)
            lcd.putchar(chr(0))
        if btn_a.value():
            if btn_b.value():
                lcd.move_to(6, 1)
                lcd.putchar(chr(1))
                lcd.move_to(8, 1)
                lcd.putstr(" ")
            else:
                lcd.move_to(8, 1)
                lcd.putchar(chr(1))
                lcd.move_to(6, 1)
                lcd.putstr(" ")
        if not btn_a.value():
                lcd.move_to(6, 1)
                lcd.putstr(" ")
                lcd.move_to(8, 1)
                lcd.putstr(" ")
        bput += 1
        bput2 += 1
    

def spawn_barrel(row):
        lcd.move_to(bp, row)
        lcd.putchar(chr(1))
        time.sleep(0.1)
        lcd.putstr(" ")
        bp - 1

lastsite = 2

def home():
    global site
    global lastsite
    global sgame
    global endsite
    endsite = 5
    lastsite = endsite
    site = 1
    while True:
        print("site:", site)
        print("btn_b:", btn_b.value())
        if site == 1:
            if lastsite == endsite:
                lcd.clear()
                lcd.move_to(2, 0)
                lcd.putstr("[Dinorunner]")
                lcd.move_to(2, 1)
                lcd.putstr("Dinofighter")
                lastsite = 1
        if site == 2:
            if lastsite == 1:
                lcd.clear()
                lcd.move_to(3, 0)
                lcd.putstr("[Tester]")
                lcd.move_to(2, 1)
                lcd.putstr("Dinorunner")
                lastsite = 2
        if site == 3:
            if lastsite == 2:
                lcd.clear()
                lcd.move_to(1, 0)
                lcd.putstr("[Spaceshooter]")
                lcd.move_to(4, 1)
                lcd.putstr("Tester")
                lastsite = 3
        if site == 4:
            if lastsite == 3:
                lcd.clear()
                lcd.move_to(3, 0)
                lcd.putstr("[Cargame]")
                lcd.move_to(2, 1)
                lcd.putstr("Spaceshooter")
                lastsite = 4
                
        if site == 5:
            if lastsite == 4:
                lcd.clear()
                lcd.move_to(1, 0)
                lcd.putstr("[Dinofighter]")
                lcd.move_to(4, 1)
                lcd.putstr("Cargame")
                lastsite = 5
                
        if btn_a.value():
            if site == 1:
                d_game()
                dgame = True
            if site == 2:
                dgame = False
                sgame = False
                break
            if site == 3:
                s_game()
            if site == 4:
                a_game()
            if site == 5:
                dinofighter()
        time.sleep(0.05)
        if btn_b.value():
            site += 1
        if site == endsite+1:
            site = 1

        
home()

while True:
    if btn_a.value():
        if btn_b.value():
            home()
            break
    if btn_a.value():
        if pressed == False:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("a pressed")
            pressed = True
    if btn_b.value():
        if pressed == False:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("b pressed")
            pressed = True
    if not btn_a.value():
        if not btn_b.value():
            if not pressed == False:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr("nothing pressed")
                pressed = False


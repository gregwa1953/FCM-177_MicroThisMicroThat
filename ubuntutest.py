import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import time

# Font
import ubuntu12
import ubuntu16

def test():
    ssd = setup(False, False)
    wri = Writer(ssd, ubuntu12)
    Writer.set_textpos(ssd,0,0)
    wri.printstring('ABCDEFGHIJKLMN')
    Writer.set_textpos(ssd,12,0)
    wri.printstring('OPQRSTUVWXYZ')
    Writer.set_textpos(ssd,24,0)
    wri.printstring('1234567890')
    Writer.set_textpos(ssd,36,0)
    wri.printstring('abcdefghijklmn')
    Writer.set_textpos(ssd,48,0)
    wri.printstring('opqrstuvwxyz')
    ssd.show()
    time.sleep(3)
    ssd.fill(0)
    wri = Writer(ssd, ubuntu16)
    Writer.set_textpos(ssd,0,0)
    wri.printstring('ABCDEFGHIJKLM')
    Writer.set_textpos(ssd,16,0)
    wri.printstring('NOPQRSTUVWXY')
    Writer.set_textpos(ssd,32,0)
    wri.printstring('Z - 1234567890')
    Writer.set_textpos(ssd,48,0)
    wri.printstring('!@#$%^&*()_+=-')
    ssd.show()
    time.sleep(3)
    ssd.fill(0)
    Writer.set_textpos(ssd,0,0)
    wri.printstring('abcdefghijklm')
    Writer.set_textpos(ssd,18,0)
    wri.printstring('nopqrstuvwxyz')
    ssd.show()
    time.sleep(3)
    ssd.fill(0)
    ssd.show()
    
test(False)

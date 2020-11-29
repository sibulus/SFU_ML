import serial
from utils.piexecuter import PiExecuter, STARTING_BYTE
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


if __name__ == "__main__":

    #if this is running on the target RPi
    if sys.platform.startswith('linux'):
        blockPrint()
        portName = "/dev/ttySSG0"
    else:
        portName = "COM2"

    serialPort = serial.Serial(portName, 115200 , timeout=1, bytesize=8, parity='N', stopbits=1)
    serialPort.set_buffer_size(rx_size = 10**8, tx_size = 10**3)

    while(1):
        if (not serialPort.isOpen()):
            exit(1)
    
        try:
            executer = PiExecuter(serialPort)
            while(True):
                executer.readSerial()
        except Exception as err:
            startBytes = bytes([STARTING_BYTE]*50)
            serialPort.write(startBytes)
            serialPort.write(("EXCEPTION: "+str(err)).encode("utf-8"))
            serialPort.write(0x55)
            serialPort.write(0x55)
            print(str(err)) 
            del(executer)           

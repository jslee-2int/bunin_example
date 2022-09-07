import serial
import time
import threading


class Serial_comm:
    def __init__(self, port, baud):
        # init. setting
        self.port = port
        self.baud = baud

        self.ser = serial.Serial(self.port, self.baud)

        if self.ser.isOpen():
            print(self.ser.name + ' is open ...')

        print('init.')
        # time.sleep(1)
        out = str(self.ser.readline())
        print(out[2:][:-5])
        # time.sleep(1)

        self.df = []

    def wh_data(self, cmd):
        t = threading.Thread(target=self.making_df, args=(cmd,))
        t.daemon = True
        t.start()
        print("End")

    def making_df(self, cmd):
        list2 = []
        list3 = []
        for i in range(16):
            list2 = []
            if i % 2 == 0:
                self.ser.write(bytes('1', encoding='ascii'))
            else:
                self.ser.write(bytes('2', encoding='ascii'))
            out = str(self.ser.readline())
            list = out[2:][:-5].split(' ')
            for i in range(len(list)):
                if i % 2 == 0:
                    list2.append(list[i]+list[i+1])
            list3.append(list2)
        self.df = list3
        return list3

    def write_data(self, cmd):
        self.ser.write(bytes(cmd, encoding='ascii'))

    def read_date(self, cmd):
        self.ser.write(bytes(cmd, encoding='ascii'))
        out = str(self.ser.readline())
        return out[2:][:-5]

    def serial_close(self):
        print(self.ser.name + ' is close ...')
        self.ser.close()


if __name__ == "__main__":
    sc = Serial_comm('COM4', 38400)
    # while True:
    #     cmd = input('Command : ')
    #     if cmd != []:
    #         getVal = sc.making_df(cmd)
    #         print(getVal)
    #     elif cmd == 'exit':
    #         break
    sc.wh_data('1')
    time.sleep(20)
    print(sc.df)
    sc.serial_close()
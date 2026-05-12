import serial
interv_ms = [100, 350, 750, 3000, 12500, 40000]
table_input = []

import serial

port = open('table_input.txt').readline().strip('\n')
ser = serial.Serial(port, baudrate=115200)

while (True) :
    mode = int(input())
    if mode == 1 :
        if len(table_input) == 0 : #надо дописать условие некорректной таблицы
            print("Error: no input file or it is uncorrected")
        else :
            for x in table_input:
                x_str = " ".join(map(str, x)) + "\n"
                ser.write(x_str.encode('utf-8'))
            
    if mode == 2 :
        table_input = [list(map(int, x.split(','))) for x in open('table_input.txt')]
ser.close()

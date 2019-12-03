from tkinter import *
import json
import socket
import time

UDP_IP = "192.168.8.1"
UDP_PORT = 2442

motor1deg= 0 
motor1rpm = 0 
motor2deg = 0
motor2rpm = 0
motor3deg = 0 
motor3rpm = 0 
motor4deg = 0 
motor4rpm = 0 

window = Tk()
window.title("Robotic Arm GUI")
window.geometry('400x400')
###########################################
lbl1 = Label(window, text="Motor 1 degree")
lbl1.grid(column=0, row=0)

txt1 = Entry(window,width=10)
txt1.insert(END, '0')
txt1.grid(column=1, row=0)
###########################################
lbl2 = Label(window, text="Motor 1 rpm")
lbl2.grid(column=2, row=0)
 
txt2 = Entry(window,width=10)
txt2.insert(END, '0')
txt2.grid(column=3, row=0)
###########################################
lbl3 = Label(window, text="Motor 2 degree")
lbl3.grid(column=0, row=1)

txt3 = Entry(window,width=10)
txt3.insert(END, '0')
txt3.grid(column=1, row=1)
###########################################
lbl4 = Label(window, text="Motor 2 rpm")
lbl4.grid(column=2, row=1)
 
txt4 = Entry(window,width=10)
txt4.insert(END, '0')
txt4.grid(column=3, row=1)
################################################
lbl5 = Label(window, text="Gripper degree")
lbl5.grid(column=0, row=2)

txt5 = Entry(window,width=10)
txt5.insert(END, '0')
txt5.grid(column=1, row=2)
###########################################
lbl6 = Label(window, text="Gripper rpm")
lbl6.grid(column=2, row=2)
 
txt6 = Entry(window,width=10)
txt6.insert(END, '0')
txt6.grid(column=3, row=2)
###########################################

def sendarray(dataArr):
    
    sendArr = json.dumps({"a":dataArr})
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(sendArr.encode('utf-8'), (UDP_IP, UDP_PORT))
    time.sleep(0.0001)
    print(sendArr)
    if( socket.error == True):

        print("Something went wrong connecting to the server!")
    exit()

########################################### 
def clicked1():
 
    motor1deg = txt1.get()
    motor1rpm = txt2.get()
 
    print(motor1deg)
    print(motor1rpm)
    
    dataArray = (motor1deg, motor1rpm, 0, 0, 0, 0, 0)  
    sendarray(dataArray)
    
btn = Button(window, text="Move Base", command=clicked1)
btn.grid(column=4, row=0)
###########################################
def clicked2():
 
    motor2deg = txt3.get()
    motor2rpm = txt4.get()
 
    print(motor1deg)
    print(motor1rpm)
    
    dataArray = (0, 0, motor2deg, motor2rpm, 0, 0, 0)
    sendarray(dataArray)
    
btn = Button(window, text="Move Arm", command=clicked2)
btn.grid(column=4, row=1)
###########################################
def clicked3():
 
    motor3deg = txt5.get()
    motor3rpm = txt6.get()
    
    print(motor3deg)
    print(motor3rpm)
    
    dataArray = (0, 0, 0 , 0, motor3deg, motor3rpm, 0)
    
    sendarray(dataArray)
 
btn3 = Button(window, text="Move Gripper", command=clicked3)
btn3.grid(column=4, row=2)
###########################################
def clicked4():
    
    Home = 1 
    dataArray = (0, 0, 0, 0, 0, 0, Home)
    
    sendarray(dataArray)
 
btn4 = Button(window, text="Move Home", command=clicked4)
btn4.grid(column=2, row=6)
###########################################
def clickExit():
        
        window.destroy()
###########################################
btn5 = Button(window, text="Exit", command=clickExit)
btn5.grid(column=2, row=10)
###########################################
window.mainloop()

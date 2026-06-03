level=int(input())
motor_status=input()
if(level<20 and motor_status=="off"):
    print("Start Motor")
elif(level>90 and motor_status=="on"):
    print("Stop Motor")
elif(level>=20 and level<=90):
    print("Normal")
else:
    print("Check Sensor")

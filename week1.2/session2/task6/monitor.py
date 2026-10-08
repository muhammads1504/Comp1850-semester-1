# Week 1.2, Session 2: Task 6
temp = int(input("Enter the machines temperate in degree celcuis "))
if temp>80:
    print("The temperature is too high. It is recomended to hut the machine down")
elif 50<temp<80:
    print("The temperature is within safe limits")
else:
    print("The machine temperature is low and no action is needs")


pressure = int(input("Enter the machines pressure in PSI "))
if pressure>100:
    print("High pressure is detected. Recomended maintanace ")
elif 70<pressure<100:
    print("Pressure is stable")
else:
    print("Pressure is low and the systme is operating normally")

operating_status = int(input("Enter the operating status(0/1) "))
if operating_status==1:
    if temp>80 or pressure>100:
        print("the system is running in unsafe conditions")
    elif temp<80 or pressure<100:
        p
        

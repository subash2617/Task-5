#Exercise no-2#
#Create a function covid( )#
# it should accept patient name & Body temperature#
# default the body temperature should be 98 degree#
while True :
    user_name = input("Enter the Name :")
    user_input = input("Enter Body TEMP :")
    if (int(user_input) < 98 or int(user_input) > 98):
        is_valid = False
        print("COVID19 ALERT")
        break
    else:
        is_valid = True
        print("Temp is NORMAL")
        break
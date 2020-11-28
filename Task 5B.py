#Exercise no-2#
#Create a function covid( )#
# it should accept patient name & Body temperature#
# default the body temperature should be 98 degree#
def COVID19():
    print("COVID19 ALERT")
user_name = input("Enter the Name :")
user_input = input("Enter Body TEMP :")
if (int(user_input) > 98):
    COVID19()
else:
    print("Temp is NORMAL")
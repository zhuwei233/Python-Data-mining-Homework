num=0
while True:
    name=input("enter your name:")
    pswd=eval(input("enter your password:"))
    if name=="zw" and pswd==142857:
        print("successful landing")
        break
    else:
        num+=1
        if num==3:
            print("locked")
            break

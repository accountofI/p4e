3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate:")
r=float(rate)
if h > 40 :
    reg= r * h
    otp= (h - 40.0) *(r * 0.5)
    xp= reg + otp
else:
    xp=h*r
print("Pay:",xp)
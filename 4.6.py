4.6


def computepay(r, h):
    if h > 40:
        reg = r * h
        otp = (h - 40.0) * (r * 0.5)
        xp = reg + otp

    else:
        xp = h * r
    return xp


hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
p = computepay(r, h)
print(p)
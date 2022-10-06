def computepay(h, rate):
    if h <= 40:
        gross_pay = h * rate 
        return gross_pay
    elif h > 40:
        gross_pay = 40 * rate + (h - 40) * (rate * 1.5)
        return gross_pay
hrs = input("Enter Hours:")
h = float(hrs)
ret = input("Enter rate per hour:")
rate = float(ret)
p = computepay(h, rate)
print("Pay", p)


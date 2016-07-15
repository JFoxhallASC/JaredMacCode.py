
import time



price = input("put in the price of the meal here.")
tax = input("put in the tax rate in decimal here.")
tip = input("put in the percent tip in decimal")


print "one moment please..."
time.sleep(2.0)

total = (price * tax + price)

ammount = (total * tip + total)

print "Your final price is: "
time.sleep(3.0)
print(ammount)

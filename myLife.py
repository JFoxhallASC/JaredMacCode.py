

from random import *
import time

print("welcom to Make Your Own Life! Please follow the following instructions")
time.sleep(2.0)

dreamSchool1  = raw_input("What is your first choice school?")
dreamSchool2  = raw_input("What is your second choice school?")
dreamSchool3  = raw_input("What is your third choice school?")
dreamSchoolList = [dreamSchool1, dreamSchool2, dreamSchool3]

wife1 = raw_input("Insert spouse option one.")
wife2 = raw_input("Insert spouse option two.")
wife3 = raw_input("Insert spouse option three.")
wifeList = [wife1, wife2, wife3]

car1 = raw_input("Insert car option one.")
car2 = raw_input("Insert car option two.")
car3 = raw_input("Insert car option three.")
carList = [car1, car2, car3]

homeLocation1 = raw_input("Insert your first home location.")
homeLocation2 = raw_input("Insert your second home location.")
homeLocation3 = raw_input("Insert your third home location.")
homeList = [homeLocation1, homeLocation2, homeLocation3]

pet1 = raw_input("Insert pet otion one.")
pet2 = raw_input("Insert pet otion two.")
pet3 = raw_input("Insert pet otion three.")
petList = [pet1, pet2, pet3]

print("All done!")
time.sleep(1.0)
print("calculating your future")
print("...")
time.sleep(4.0)

print "In the future you will have an awesome life. The the young age of twenty one, you will meet a gender non-conforming partner at %s marry %s. You will subsiquently land a high profile job at Goldman Sachs, and will afford to buy a %s and a house in %s. Your wife will buy a %s and you will live a long happy life with no kids... untill the %s eats your spouse." % (choice(dreamSchoolList), choice(wifeList), choice(carList), choice(homeList), choice(petList), choice(petList))
time.sleep(2.0)
print("THE END")







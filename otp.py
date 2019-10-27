from notify_run import Notify  # pip install notify_run
import random
import os

Notif = Notify()

OTP = random.randint(10000, 99999)  # Generate a five digit random number.
print("This file contains deadly photo\n\nTo open this file, you need to verify it's you.\n\nA verification OTP will be sent to your phone")
notification = ("Your OTP is: " + str(OTP))
Notif.send(notification)
Entry = int(input("Enter OTP to access this file: "))
if Entry == OTP:
    print("OTP Verified")
else:
    print("Wrong OTP")
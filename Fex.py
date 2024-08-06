# 2024.08.06
# created by lasith ruwantha
# contact 9478823116

import sys
import time

def animated(text):
  for x in text:
   sys.stdout.write(x)
   sys.stdout.flush()
   time.sleep(0.05)

logo1="\033[0;34m hey tool by lasith ruwantha\n"
logo2="\033[1;31m fex tool kit\n "

animated(logo1)
animated(logo2)

print ("\033[1;37m type you logo\n")
logo3=input("\033[0;34menter you logo>>>\033[0;32m")
print("\033[0;31m[\033[1;37m1\033[0;31m]\033[1;37mreb")
print("\033[0;31m[\033[1;37m2\033[0;31m]\033[1;37mblue")
print("\033[0;31m[\033[1;37m3\033[0;31m]\033[1;37mgreen")

x=int(input ("\033[0;32menter you logo colour:\033[0;34m"))
if (x == int(1)):
  print ("\033[0;31m")
  animated(logo3)
elif (x == int(2)):
   print ("\033[0;34m")
   animated(logo3)
elif (x == int(3)):
  print ("\033[0;32m")
  animated(logo3)
# end
# tool by lasithruwantha 
# flow my github 
# tanks all

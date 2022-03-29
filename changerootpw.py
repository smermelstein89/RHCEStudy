#!/usr/bin/env python
import time
start = time.time()

#Changing Root PW
##step1
step1 = input("Step 1: Enter the character to press at grub or 'h' for a hint:")
while step1 != 'e':
  if ( step1 == 'h'):
    print("the letter 'e'")
    step1 = input("Step 1: Enter the character to press at grub:")
  elif (step1 == 'e'):
    print("Correct!")
  else:
    print("Fail")
    step1 = input("Step 1: Enter the character to press at grub:")


#Rd.break at the end of the linux16 line.
step2 = input("Step2 : What should be entered at the end of the 'linux16' line? Or 'h' for a hint.")

while step2 != 'rd.break':
  if ( step1 == 'h'):
    print("Hint: 'rd'")
    step2 = input("Step2 : What should be entered at the end of the 'linux16' line? ")
  elif (step1 == 'rd.break'):
    print("Correct!")
  else:
    print("Fail")
    step2 = input("Step2 : What should be entered at the end of the 'linux16' line? ")


#Mount -o remount,rw /sysroot

step3 = input("Step 3: What is the command to remount the root file system as read/write? Or 'h' for a hint.")
while step3 != "mount -o remount,rw /sysroot":
  if ( step3 == 'h'):
    print("Hint: 'mount -o remount'")
    step3 = input("Step 3: What is the command to remount the root file system as read/write?")
  elif (step3 == "mount -o remount,rw /sysroot"):
    print("Correct!")
  else:
    print("Fail")
    step3 = input("Step 3: What is the command to remount the root file system as read/write?")
 
#Chroot /sysroot
#Passwd
#Enter password
#Repeat
#touch /.autorelabel
#Exit; exit

end = time.time()
print("Your score for 'Reset Root PW' is: ", round(end-start, 10))


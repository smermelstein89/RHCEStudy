#!/usr/bin/env python
import time
start = time.time()

def question(num, question, answer, hint):
    hint_text = "or 'h' for a hint"
    step = input("Step {}: {} {}:".format(num,question,hint_text))
    while step != str(answer):
        if ( step == 'h'):
            print("Hint: {}", hint)
            step = input("Step {}: {}:".format(num,question))
        elif (step == str(answer)):
            print("Correct!")
        else:
            print("Fail")
            step = input("Step {}: {}:".format(num,question))


question(1,"Enter the character to press at grub", 'e', 'the letter e')
question(2,"What should be entered at the end of the 'linux16' line?", "rd.break", "'rd'")
question(3,"What is the command to remount the root file system as read/write?", "mount -o remount,rw /sysroot", "'mount -o remount'")
question(4,"Switch into a chroot jail?", "chroot /sysroot", "'sysroot")
question(5,"What is the step after chroot /sysroot?", "passwd", "'change the root password.'")
question(6,"Address all unlabeled files.", "touch /.autorelabel", "'touch ?autorelabel'")
question(7,"How do you get out and reboot back to the main system?", "exit", "'exit'")


# #Changing Root PW
# ##step1
# step1 = input("Step 1: Enter the character to press at grub or 'h' for a hint:")
# while step1 != 'e':
#   if ( step1 == 'h'):
#     print("the letter 'e'")
#     step1 = input("Step 1: Enter the character to press at grub:")
#   elif (step1 == 'e'):
#     print("Correct!")
#   else:
#     print("Fail")
#     step1 = input("Step 1: Enter the character to press at grub:")


# #Rd.break at the end of the linux16 line.
# step2 = input("Step2 : What should be entered at the end of the 'linux16' line? Or 'h' for a hint.")

# while step2 != 'rd.break':
#   if ( step1 == 'h'):
#     print("Hint: 'rd'")
#     step2 = input("Step2 : What should be entered at the end of the 'linux16' line? ")
#   elif (step1 == 'rd.break'):
#     print("Correct!")
#   else:
#     print("Fail")
#     step2 = input("Step2 : What should be entered at the end of the 'linux16' line? ")


# #Mount -o remount,rw /sysroot

# step3 = input("Step 3: What is the command to remount the root file system as read/write? Or 'h' for a hint.")
# while step3 != "mount -o remount,rw /sysroot":
#   if ( step3 == 'h'):
#     print("Hint: 'mount -o remount'")
#     step3 = input("Step 3: What is the command to remount the root file system as read/write?")
#   elif (step3 == "mount -o remount,rw /sysroot"):
#     print("Correct!")
#   else:
#     print("Fail")
#     step3 = input("Step 3: What is the command to remount the root file system as read/write?")
 
# #Chroot /sysroot
# #Passwd
# #Enter password
# #Repeat
# #touch /.autorelabel
# #Exit; exit

end = time.time()
print("Your score for 'Reset Root PW' is: ", round(end-start, 10))


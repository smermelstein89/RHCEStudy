#!/usr/bin/env python
import time
import os

start = time.time()
name = "Scott"
#check if the high score file exists
if os.path.exists('score.txt'):
    #check the previous high score
    with open('score.txt', 'r') as file:
        high_score = float(file.read())
else:
    high_score = 0

def question(num, question, answer, hint):
    hint_text = "or 'h' for a hint"
    step = input("Step {}: {} {}:".format(num,question,hint_text))
    while step != str(answer):
        if ( step == 'h'):
            print("Hint: {}".format(hint))
            step = input("Step {}: {}:".format(num,hint))
       #elif (step == str(answer)):
#            print("Correct!")
        else:
            print("Fail")
            step = input("Step {}: {}:".format(num,question))
    print("Correct!")

question(1,"Enter the character to press at grub", 'e', 'the letter e')
question(2,"What should be entered at the end of the 'linux16' line?", "rd.break", "'rd'")
question(3,"What is the command to remount the root file system as read/write?", "mount -o remount,rw /sysroot", "'mount -o remount'")
question(4,"Switch into a chroot jail?", "chroot /sysroot", "'sysroot")
question(5,"What is the step after chroot /sysroot?", "passwd", "'change the root password.'")
question(6,"Address all unlabeled files.", "touch /.autorelabel", "'touch ?autorelabel'")
question(7,"How do you get out and reboot back to the main system?", "exit", "'exit'")

# #Chroot /sysroot
# #Passwd
# #Enter password
# #Repeat
# #touch /.autorelabel
# #Exit; exit

end = time.time()
totalTime = end - start
score = 0
if totalTime > 100:
    score = 0
else:
    score = round(100 - totalTime,2)

print("Your score for 'Reset Root PW' is: ", score)

#Update high score
if score > high_score:
    high_score = score
    with open('score.txt', 'w') as file:
        file.write(str(high_score))
    print("Congratulations! You go the new High Score!")
    print("The New High Score is: {}".format(high_score))
else:
    print("The High Score is: {}".format(high_score))
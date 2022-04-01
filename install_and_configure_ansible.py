#!/usr/bin/env python
import time
import os
import datetime

timeofplay = datetime.datetime.now()
high_score_file = "installandconfansible_highscore.txt"
start = time.time()
name = "Scott " + timeofplay.strftime("%y-%m-%d %H:%M:%S")
question_num = 1
def question(question, answer, hint):
    global question_num
    hint_text = "or 'h' for a hint"
    step = input("Step {}: {} {}:".format(question_num,question,hint_text))
    while step != str(answer):
        if ( step == 'h'):
            print("Hint: {}".format(hint))
            step = input("Step {}: {}:".format(question_num,hint))
       #elif (step == str(answer)):
#            print("Correct!")
        else:
            print("Fail")
            step = input("Step {}: {}:".format(question_num,question))
    print("Correct!")
    question_num += 1

question("Install Ansible", 'sudo dnf install ansible', 'dnf')
question("Create the static inventory with the name, /home/user/ansible/inventory", "mkdir -p /home/user/ansible/;vim /home/user/ansible/inventory", "mkdir;vim")
question("How do you make a host group called production?", "[production]", "[]")
#question("how do you add a member to a host group?", "add below", "type it")
question("Create the ansible.cfg configuration file", "vim /home/user/ansible/ansible.cfg", "ansible.cfg")
question("Add the inventory.", "inventory=/home/user/ansible/inventory", "'inventory='")
question("How do you add the roles path?", "roles_path=/home/user/ansible/roles", "'roles_path='")

question("The escalation user, and the user that will be used to manage the remote hosts must be root.","remote_user=root","remote")
question("Verify the inventory configuration","ansible --list-hosts all","list-hosts")

question("Verify the current Ansible configuration file.","ansible --version","version")

##--------

end = time.time()
totalTime = end - start
score = 0
if totalTime > 100:
    score = 0
else:
    if score < 10:
        score = str(score)
        score = score.zfill(0)
    else:
        pass
    score = round(100 - totalTime,2)

print("Your score for 'Reset Root PW' is: ", score)

#Update high score
file=open(high_score_file,"a")
file.write(str(score) + ",  " + name + "\n")
file.close()


#sort the high scores
file = open(high_score_file,"r")
readthefile = file.readlines()
sortedData = sorted(readthefile,reverse=True)
high_score = sortedData[0]
print("High Score is: " + high_score)
###NEED TO STORE THE SCORES AS DICTIONARY VALUES TO CALL THEM LATER to SORT and print the High Score
# if score > high_score:
#     print("Congratulations! You go the new High Score!")
#     print("The New High Score is: {}".format(high_score))

print("Top Scores:")
print("Pos\tPoints, Name")

for line in [x for x in range(len(sortedData)) if x <10]:
    print(str(line + 1) + "\t" + str(sortedData[line]))
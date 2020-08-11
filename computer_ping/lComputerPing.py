#!/usr/bin/python3
# computer_ping.py a simple ping to see if a box is up or not.

# load needed modules
import os, time, subprocess, sys

# check for command line arguments, ask for target if none provided.
if len(sys.argv) > 1:
    hostName = (sys.argv[1])
else:
    hostName = input("What host are you looking for? (Enter hostname or ip address):  ")

# Function to call Linux ping command
def pingComputer(pingThis):
    response = os.system('ping -c 1 -W 100 ' + pingThis + ' > /dev/null 2>&1')
    return  response

# Function to open text file wiht the result of the final ping (up or down).
def alertBox(pingResult):
    fileObj = open(hostName + '_ping_result.txt', 'w')
    fileObj.write(hostName + pingResult)
    fileObj.close()
    subprocess.Popen(['xdg-open', hostName + '_ping_result.txt'])
    #subprocess.Popen(['/usr/bin/mousepad', hostName + '_ping_result.txt'])


#try pinging the host over the course of an hour, stops when the target is up.
print()
attemptsLeft  = 6
attemptNumber = 1

while attemptsLeft > 0:
    upDown = pingComputer(hostName)
    if upDown == 0:
        print('Attempt ' + str(attemptNumber) + ': ' + hostName + ' is up!')
        print()
        alertBox(' is up at this time!')
        break
    elif attemptsLeft == 1:
        print('Attempt ' + str(attemptNumber) + ': ' + hostName + ' is down! Ping attempts ended')
        print()
        alertBox(' is down at this time! Tried for 1 hour.')
    else:
        print('Attempt ' + str(attemptNumber) + ': ' + hostName + ' is down, trying again in 10 minutes.')
        time.sleep(600)
        print()
    attemptNumber += 1
    attemptsLeft  -= 1
# sleep 3 seconds to allow system to open text file, before deleting text file.    
time.sleep(3)
os.remove(hostName + '_ping_result.txt')
    


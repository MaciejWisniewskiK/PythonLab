
ActivitiesSum = {}

def NewActivity(activityName, time):
    if activityName in ActivitiesSum:
        ActivitiesSum[activityName] += time
    else:
        ActivitiesSum[activityName] = time

def ShowTime(activityName):
    print("Total time spend on " + activityName + " is " + str(ActivitiesSum[activityName]))

def MostTime():
    print("Most time spend on any activity:")
    print(sorted(ActivitiesSum.items(), key = lambda x:x[1], reverse=True)[:3])



NewActivity("coding", 10)
NewActivity("coding", 5)

ShowTime("coding")      # expected value = 15

NewActivity("gaming", 100)
NewActivity("coding", 90)
NewActivity("gaming", 1)
NewActivity("cooking", 200)
NewActivity("sleeping", 300)

MostTime()              # expected value = [sleeping : 300, cooking : 200, coding : 105]
ShowTime("sleeping")    # expected value = 300
ShowTime("cooking")     # expected value = 200
ShowTime("coding")      # expected value = 105
ShowTime("gaming")      # expected value = 101

#print("Input 1 to add new activity, 2 to Show time spent on an activity and 3 to show top 3 activities.")
#while True:
#    inp = input()
#    
#    if inp == "1":
#        print("Input name of activity and time spent on it.")
#        name = input()
#        time = int(input())
#        NewActivity(name, time)
#
#    elif inp == "2":
#        print("Input name of activity.")
#        name = input()
#        ShowTime(name)
#
#    elif inp == "3":
#        MostTime()
#
#    else:
#        print("wrong key")
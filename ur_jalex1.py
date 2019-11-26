#!/usr/bin/env python3

# Process a list of all users logged in (and out) on a UNIX/Linux system from a text file created by the shell command "last -F"
# (1) Read all the records
# (2) normalized all the records so that each record has the same login and logout date
# (3) select records for the same user or the same remote machine
# (4) based on the records selected in step (3), create daily, weekly, or monthly report in the format specified.

#OPS435 Assignment 2 - Fall 2019
#Program: ur_[jalex1].py
#Author: "Joel Alex"
#The python code in this file ur_[jalex1].py is original work written by
#"Joel Alex". No code in this file is copied from any other source 
#including any person, textbook, or on-line resource except those provided
#by the course instructor. I have not shared this python file with anyone
#or anything except for submission for grading.  
#I understand that the Academic Honesty Policy will be enforced and violators 
#will be reported and appropriate action will be taken.

# Imports the needed modules from the python class

import sys
import argparse
import time

#getlist function to login files
def getlist(filelist):
    
    file = open(filelist, 'r')
    readfile = file.readlines()
    readfile = readfile[1::]
    listdetail = []
    a = 0
    b = 0
    u = None

    if args.list == 'user':
        b = 0
        u = 'User'
    elif args.list == 'host':
        b = 2 
        u = 'Host'

    for eachrecord in readfile:
        temp = readfile[a].split()
        listdetail.append(temp[b])
        a = a + 1
    listdetail = set(listdetail)
    listdetail = list(listdetail)
    listdetail.sort()

    login = u + ' ' + '  list for' + ' ' + filelist
    login +="\n"
    login += '\a'
    for length in range (1, len(login)):
        login += "="
    login += '\a'
    login += "\n"
    for eachname in listdetail:
        login += eachname
        login += "\n"
        login += '\a'

    return login


#function to record the logins

def read_login_rec(subj, filelist):
    
    login_records = []
    # open the file, find the line that has the subject, and adds them to a list
    try:
        with open(filelist, 'r') as searching:
            for line in searching:
                line = line.split()
                if subj in line:
                    login_records.append(line)
     
        # Returns the list
        return login_records

    # Error exception when file is not found
    except FileNotFoundError:
        print("File not found")
        sys.exit()

#function for daily usages
        
def cal_daily_usage(subject, login_recs):
    
    message = ""
    message += "Daily usage report for " + str(subject)
    message += "\n"
    message += "\a"
    for length in range(1, len(message)):
        message += "="
    message += "\n"
    message += "\a"
    message += "Date"
    for length in range(4,14):
        message += " "
    message += "Usage in seconds"
    message += "\a"
    message += "\n"

    #empty variables to hold values
    counter = 0
    daily_usage = 0
    diffa = []
    tmp = []

    for item in range(0, len(login_recs)):
        #before = 0
        datelist = login_recs[counter]
        
        datetemp1 = datelist[3:8]
        datetemp2 = datelist[9:14]
        
        date1 = ' '.join(datetemp1)
        date2 = ' '.join(datetemp2)
        
        scnds1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        scnds2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        difference = scnds2 - scnds1

        diffa.append(int(difference))

        days = sum(diffa)

        daily_usage += difference

        counter += 1 

        # Converting the tuple into standard format
        messageofdate = time.strftime("%Y %m %d", time.localtime(scnds1))
        daily_usage = int(daily_usage)

        # Checks if the date already exists then it replaces the seconds in standard format

        if messageofdate in message:
            if t in message:
                message = message.replace(t, str(days))
                
        else:
            message += str(messageofdate)
            for length in range (10,18):
                message += " "
            message += str(daily_usage)
            message += "\a"

            tmp.append(str(int(difference)))
            t = ''.join(tmp)

            diffa = []
            tmp = []
            days = 0

    # Showing the total time in seconds
    message += "\n"
    message += "Total"
    for length in range (5,18):
        message += " "
    message += str(daily_usage)
    return message

#create function for weekly usage0

def cal_weekly_usage(subject, login_recs):
 #displaying the caption  
    message = ""
    message += "Weekly usage report for " + str(subject)
    message += "\n"
    message += "\a"
    for length in range(1, len(message)):
        message += "="
    message += "\n"
    message += "\a"
    message += "Week #"
    for length in range(6,14):
        message += " "
    message += "Usage in seconds"
    message += "\n"
    message += "\a"
    #Empty variables to hold the vales
    counter = 0
    weekly_usage = 0
    diffa = []
    tmp = []


    for item in range(0, len(login_recs)):
        datelist = login_recs[counter]
        
        datetemp1 = datelist[3:8]
        datetemp2 = datelist[9:14]
        
        date1 = ' '.join(datetemp1)
        date2 = ' '.join(datetemp2)

        scnds1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        scnds2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = scnds2 - scnds1

        diffa.append(int(diff))

        days = sum(diffa)

        weekly_usage += diff

        counter += 1

        messageofdate = time.strftime("%Y %W", time.localtime(scnds1))
        weekly_usage = int(weekly_usage)

        # Checks if the date already exists then it replaces the seconds in the standard format
        if messageofdate in message:
            if t in message:
                message = message.replace(t, str(days))
                tmp = []
                diffa = []
        else:
            message += str(messageofdate)
            for length in range (7,19):
                message += " "
            message += str(weekly_usage)
            message += "\a" 

            tmp.append(str(int(diff)))
            t = ''.join(tmp)
    message += "\n" 
    message += "Total"
    for length in range (5,19):
        message += " "
    message += str(weekly_usage)
    return message


  

# Checks for arguments
if __name__ == "__main__":

    # Arrganes the arguments in correct order
    parser = argparse.ArgumentParser(
        description="Usage Report based on the last command",
        epilog='Copyright 2019 - Joel Alex')
    parser.add_argument('F', help='list of files to be processed')
    parser.add_argument('-l', '--list', metavar='{user,host}',
                        type=str,
                        help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost',
                        type=str,
                        help='generate user name or remote host IP from the given files')
    parser.add_argument('-t', '--type',
                        metavar='{daily,weekly}',
                        type=str, help='type of report: daily,weekly')
    parser.add_argument('-u', '--user',
                        type=str, help='usage report for the given username')
    parser.add_argument('-v', '--verbose',
                        help='tune on output verbosity',
                        action='store_true')
    args = parser.parse_args()
    
   # If verbose is selected, it is prints out the processes
    if args.verbose:
        print("Files to be processed: " + str(args.F))
        print("Type of args for files <class 'list'>")

    # Displays the table of the existing users or hosts from the selected list
    if args.list:
        print(getlist(args.F))

    # If user is selected then another condition to check wheather  the daily,
    # weekly, or monthly usage needs to be calculated, then calling the right function
    if args.user:
        if args.type == 'daily':
            # If verbose is selected, prints out the rest of the program
            if args.verbose:
                print("Usage report for user: " + str(args.user))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            fileused = read_login_rec(args.user, args.F)
            print(cal_daily_usage(args.user, fileused))
        elif args.type == 'weekly':
            # If verbose is selected, prints out the rest of the program
            if args.verbose:
                print("Usage report for user: " + str(args.user))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            fileused = read_login_rec(args.user, args.F)
            print(cal_weekly_usage(args.user, fileused))

    # If the host is selected  then it is going to check  another condition wheather daily,
    # weekly, or monthly usage needs to be calculated, then calling the required function
    if args.rhost:
        if args.type == 'daily':
            # If verbose is selected, prints out the rest of the program
            if args.verbose:
                print("Usage report for remote host: " + str(args.rhost))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            fileused = read_login_rec(args.rhost, args.F)
            print(cal_daily_usage(args.rhost, fileused))
        elif args.type == 'weekly':
            # If verbose is selected, prints out the rest of the program
            if args.verbose:
                print("Usage report for remote host: " + str(args.rhost))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            fileused = read_login_rec(args.rhost, args.F)
            print(cal_weekly_usage(args.rhost, fileused))

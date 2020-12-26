#!/bin/python3

import math
import os
import random
import re
import sys
import requests



def getTotalGoals(team,year):
    print(team,year)
    recive=requests.get('https://jsonmock.hackerrank.com/api/football_matches?yaer='+str(year)+'&team1='+str(team)+'&page=1')
    json1=recive.json()
    print(recive.text)
    total_page=json1["total_pages"]
    print(total_page)

    total_goals=0
    for i in range(total_page):
        recive = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?yaer=' + str(year) + '&team1=' + str(team) + '&page='+str(i))
        json1 = recive.json()
        datax=json1['data']
        for each in datax:
            if str(each['year'])==str(year):
                total_goals+=int(each['team1goals'])

        recive = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?yaer=' + str(year) + '&team2=' + str(
                team) + '&page=' + str(i))
        json1 = recive.json()
        datax = json1['data']
        for each in datax:
            print(each)
            if str(each['year']) == str(year):
                total_goals += int(each['team2goals'])


    print(total_goals)


if __name__=='__main__':
    # fptr=open(os.environ['OUTPUT_PATH'],'w')
    team=input()
    year=int(input().strip())
    result=getTotalGoals(team,year)
    # fptr.write(str(result)+'\n')
    # fptr.close()

'''
Barcelona
2011
'''
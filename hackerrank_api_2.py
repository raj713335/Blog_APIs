#!/bin/python3

import math
import os
import random
import re
import sys
import requests



def getTotalGoals(competition,year):
    print(competition,year)
    recive=requests.get('https://jsonmock.hackerrank.com/api/football_competitions?name='+str(competition)+'&year='+str(year)+'&page=1')
    json1=recive.json()
    total_page=json1["total_pages"]


    data_list=(json1['data'][0])
    team=data_list['winner']
    print(team)

    recive = requests.get(
        'https://jsonmock.hackerrank.com/api/football_matches?competition=' + str(competition) + '&year=' + str(year) + '&team1=' + str(team)+ '&page=1')
    json1 = recive.json()
    print(recive.text)
    total_page = json1["total_pages"]
    print(total_page)

    total_goals = 0
    for i in range(1,total_page+1):
        recive = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?competition=' + str(competition) + '&year=' + str(year) + '&team1=' + str(team)+  '&page=' + str(i))
        json1 = recive.json()
        datax = json1['data']
        for each in datax:

            total_goals += int(each['team1goals'])

        recive = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?competition=' + str(competition) + '&year=' + str(year) + '&team2=' + str(team)+  '&page=' + str(i))
        json1 = recive.json()
        datax = json1['data']
        for each in datax:
            print(each)
            total_goals += int(each['team2goals'])

    print(total_goals)



if __name__=='__main__':
    # fptr=open(os.environ['OUTPUT_PATH'],'w')
    competition=input()
    year=int(input().strip())
    result=getTotalGoals(competition,year)
    # fptr.write(str(result)+'\n')
    # fptr.close()

'''
UEFA Champions League
2011
'''
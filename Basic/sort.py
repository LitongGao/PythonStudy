#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import calendar
import datetime

def sort():
    a = "I am a boy"
    print (a[-1:])
    b = a.split(" ")
    print (b)
    c = []
    for i in range(len(b)-1,-1,-1):
        c.append(b[i])
    print (c)
    b.reverse()
    print(b)

def get_first_last_day():
    cal = calendar.month(2016,1)
    print(cal)

def dateRange(beginDate, endDate):
    dates = []
    # dt_obj = datetime.datetime.strftime(beginDate, '%m/%d/%Y')
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates

def printDate():
    enddate = str(datetime.date.today())
    dates = dateRange('2015-01-01', enddate)

def printDateCal():
    FORMAT = "%d-%d-%d\t%d-%d-%d"
    year = 2013
    for m in range(1, 13):
        d = calendar.monthrange(year, m)
        print (FORMAT % (year, m, 1, year, m, d[1]))

def printSpicalDate(data):
    FORMAT = "%d-%d-%d\t%d-%d-%d"
    dt = datetime.datetime.strptime(data, "%Y-%m-%d")
    begin_year = dt.year
    begin_month = dt.month
    enddate = datetime.date.today()
    end_year = enddate.year
    end_month = enddate.month
    for y in range(begin_year, end_year+1):
        if y == begin_year:
            for m in range(begin_month, 13):
                d = calendar.monthrange(begin_year, m)
                print(FORMAT % (begin_year, m, 1, begin_year, m, d[1]))
        elif y == end_year:
            for m in range(1, end_month + 1):
                d = calendar.monthrange(end_year, m)
                print(FORMAT % (end_year, m, 1, end_year, m, d[1]))
        else:
            for m in range(1, 13):
                d = calendar.monthrange(y, m)
                print(FORMAT % (y, m, 1, y, m, d[1]))

if __name__ == "__main__":
    # get_first_last_day()
    # for date in dateRange('2018-02-01', '2019-02-10'):
    #     print(date)
    # printDateCal()
    printSpicalDate('2017-10-04')


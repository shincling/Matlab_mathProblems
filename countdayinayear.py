#-*-coding:utf-8 -*-
def judge_leap_year(n):
    # if n%4 == 0 and n%100 != 0:
    #     return True
    # if n%100 == 0 and n%400 == 0:
    if (n%4 == 0 and n%100 != 0) or (n%100 == 0 and n%400 == 0):
        return True
    else:
        return False

def compute_year_counts(datestr):
    date=datestr.split('-')
    year = int(date[0])
    month = month_list.index(date[1])+1
    day = int(date[2])
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    nDays = sum(days[i] for i in range(0, month - 1))
    if (judge_leap_year(year)):
        nDays += 1
        return (nDays + day)/366.0
    else:
        return (nDays + day)/365.0

month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

data='1998-Jan-24'

print compute_year_counts(data)

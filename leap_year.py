#_*_ coding: utf-8 _*_

def leap_year(year) :
    res = "평년"
    if year%400 == 0 :
        res = "윤년"
    elif year%100 == 0:
        res = "평년"
    elif year%4 == 0:
        res = "윤년"
    return res



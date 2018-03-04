#!/user/bin/env python
# -*- coding: utf-8 -*-
import re

class JudgeClass:
    def __init__(self):
        print('judge')
    
    def is_today(self, topdate, today):
        topdate = re.split(r'年|月|日', topdate.group())
        topdateMonth = topdate[1]
        topdateDate = topdate[2]
    
        today = re.split(r'-', today)
    
        todayMonth = today[1]
        if todayMonth[0] == '0':
            todayMonth = todayMonth[1:]
    
        todayDate = today[2]
        if todayDate[0] == '0':
            todayDate = todayDate[1:]
    
        if topdateMonth == todayMonth and topdateDate == todayDate:
            return True
    
        return False
        
    def is_open(status):
        if status == '営業':
            return True
        if status == '休み':
            return False
        return 'Other'
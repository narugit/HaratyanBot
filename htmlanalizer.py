#!/user/bin/env python
# -*- coding: utf-8 -*-
import re

class HtmlAnalizeClass:
    def __init__(self):
        self.fp = open('../haratyan.html', 'r', encoding='utf-8')
        self.lines = self.fp.readlines()
        self.fp.close()

    def get_topdate(self):
        for line in self.lines:
            if line.find('<h2>2') >= 0:
                topdate = re.search(r'2[0-9][0-9][0-9].+秒', line)
                return topdate

    def get_open_status(self, today):
        today = re.split(r'-', today)    
        todayDate = today[2]
        if todayDate[0] == '0':
            todayDate = todayDate[1:]
        
        for line in self.lines:
            if re.search(r'^[0-9]+月', line):
                index = line.find(todayDate+'日')
                if index != -1:
                    return re.split(r' ', line)[1][:2]
                return '営業情報なし'
        
        return '営業情報なし'

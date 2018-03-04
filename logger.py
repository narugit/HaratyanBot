#!/user/bin/env python
# -*- coding: utf-8 -*-

class LogClass:
    def __init__(self):
        print('log')
        
    def set_log(self, text):
        log = open('log.txt', 'w')
        log.write(text)
        log.close()
        return
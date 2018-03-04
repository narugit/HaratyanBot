#!/user/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import tweetmanager
import htmlanalizer
import judger
import logger

def main():
    judge_class = judger.JudgeClass()
    log_class = logger.LogClass()
    html_analize_class = htmlanalizer.HtmlAnalizeClass()
    twitter_class = tweetmanager.TwitterClass()
    
    topdate = html_analize_class.get_topdate()
    today = datetime.now().date()
    today = str(today)

    if judge_class.is_today(topdate, today) == True:
        open_status = html_analize_class.get_open_status()

        if judge_class.is_open(open_status) == True:
            log_class.set_log('New')
            tweet=str(datetime.now().time()) + '営業します'
            twitter_class.set_tweet(tweet)
            return
        if judge_class.is_open(open_status) == False:
            log_class.set_log('New')
            tweet=str(datetime.now().time()) + '休みです'
            twitter_class.set_tweet(tweet)
            return
        if judge_class.is_open(open_status) == 'Other':
            log_class.set_log('Other')
            return

    log_class.set_log('Old')
    tweet=str(datetime.now().time()) + ' 更新なし'
    twitter_class.set_tweet(tweet)
    return

if __name__ == "__main__":
    main()

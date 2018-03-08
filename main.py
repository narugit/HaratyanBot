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
            tweet='営業します！' + '（{0:%Y}年{0:%m}月{0:%d}日{0:%H}時{0:%M}分）'.format(datetime.now())
            twitter_class.set_tweet(tweet)
            return
        if judge_class.is_open(open_status) == False:
            log_class.set_log('New')
            tweet='休みです><' + '（{0:%Y}年{0:%m}月{0:%d}日{0:%H}時{0:%M}分）'.format(datetime.now())
            twitter_class.set_tweet(tweet)
            return
        if judge_class.is_open(open_status) == 'Other':
            log_class.set_log('Other')
            return

    log_class.set_log('Old')
    tweet='ブログ更新なし もうそろそろ！' + '（{0:%Y}年{0:%m}月{0:%d}日{0:%H}時{0:%M}分）'.format(datetime.now())
    twitter_class.set_tweet(tweet)
    return

if __name__ == "__main__":
    main()

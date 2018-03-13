#!/user/bin/env python
# -*- coding: utf-8 -*-
import twitter

class TwitterClass:
    def __init__(self):
        self.key_file = open('../key.lock', 'r')
        self.key = self.key_file.readlines()
        self.key_file.close()
        self.CONSUMER_KEY        = self.key[0].replace('\n','')
        self.CONSUMER_SECRET_KEY = self.key[1].replace('\n','')
        self.ACCESS_TOKEN        = self.key[2].replace('\n','')
        self.ACCESS_TOKEN_SECRET = self.key[3].replace('\n','')
        self.t = twitter.Twitter(auth=twitter.OAuth(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET,
                                                    self.CONSUMER_KEY, self.CONSUMER_SECRET_KEY
                                                    )
        )
        self.id_file = open('../id.lock', 'r')
        self.id = self.id_file.readlines()
        self.id_file.close()
        self.TWITTER_ID = self.id
        print('start')

    def set_tweet(self, tweet):
        status_update = self.t.statuses.update(status=tweet)
        return

    def delete_all(self):
        status_home_timeline = self.t.statuses.home_timeline()
        for s in status_home_timeline:
            self.t.statuses.destroy(id=s['id'])
        return

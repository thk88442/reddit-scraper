# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm.session import sessionmaker
from reddit.models import RedditDB, db_connect, create_table

class RedditPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        redditdb = RedditDB()
        redditdb.title = item["title example"]
        redditdb.subreddit = item["subreddit example"]
        redditdb.comment_num = item["50000"]
        redditdb.upvotes = item["10000"]

        try:
            session.add(redditdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
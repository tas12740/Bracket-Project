# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class KenpomPipelinePandas(object):
    dataFrames = {}

    def process_item(self, item, spider):
        if self.dataFrames[item['Year']] is None:
            self.dataFrames[item['Year']] = []
        self.dataFrames[item['Year']].append(item)
        return item

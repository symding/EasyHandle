from committer.accumulators import Accumulator
from committer import item
import pymysql

class MysqlAccumulator(Accumulator):
    def __init__(self, config: dict):
        self.conn = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            db=config['db'],
            charset="utf8mb4"
        )
        self.cursor = self.conn.cursor()

    def add(self, item: item.MysqlItem) -> None:
        if item.data:
            item.format()
        self.pool.setdefault(
            item.tag, list()
        ).append(
            item.sql
        )
        if len(self.pool[item.tag]) >= item.size:
            self.batch(self.pool.pop(item.tag))

    def batch(self, data):
        self.cursor.executemany(data)
        self.conn.commit()

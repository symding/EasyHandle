class Accumulator:
    pool = dict()

class AccumulatorFactory():
    @staticmethod
    def create(conf):
        if conf['type'] == "mysql":
            from committer.accumulators.mysql import MysqlAccumulator
            return MysqlAccumulator(conf)


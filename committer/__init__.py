from committer.accumulators import AccumulatorFactory
from committer.item import BaseItem

class ItemCommiter():
    def __init__(self, setting: dict):
        self.setting = setting
        self.factory = AccumulatorFactory()
        self.all_accumulator = dict()

    def add_item(self, item: BaseItem) -> None:
        tag = item.tag
        conf = self.setting['Tag'][tag]
        accumulator = self.all_accumulator.get(tag)
        if accumulator is None:
            accumulator = self.all_accumulator.setdefault(
                tag, self.factory.create(conf)
            )
        accumulator.add(item)
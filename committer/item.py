from typing import  Optional, Tuple

class BaseItem():
    size: int = 10
    check: str = "normal"
    tag: str

    @property
    def valid_check(self) -> str:
        return self.check
    
    @valid_check.setter
    def valid_check(self,value:str) -> None:
        assert value in {"dirty","normal","strict"}
        self.valid_check = value

    @property
    def batch_size(self)  -> int:
        return self.size
    
    @batch_size.setter
    def batch_size(self,value:int) -> None:
        assert isinstance(value,int)
        self.size = value

class MysqlItem(BaseItem):
    table: str
    sql: Optional[Tuple]
    data: dict()

    def format(self):
        sql = "insert into " + self.table
        keys = list()
        param = list()
        for k, v in self.data['insert'].items():
            keys.append(k)
            param.append(v)
        sql += f'''(`{'`,`'.join(keys)}`) values({','.join(["%s" for _ in range(len(param))])}) '''
        if self.data['update'] is not None:
            sql += "on duplicate key update "
            for u in self.data['update']:
                sql += f"{u}=values({u})"
        self.sql = (sql, param)


from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.schema import Index


@as_declarative()
class Base:
    id: Any
    __name__: str

    # 自动生成表名
    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    # 利用反射自动生成字段索引
    @declared_attr
    def __table_args__(cls):  # noqa
        """
        反射自动生成字段索引
        """
        if not hasattr(cls, '__idx_list__'):
            return None
        table_args = []
        for field_name in cls.__idx_list__:
            field = getattr(cls, field_name)
            index_name = f'{cls.__tablename__}_{field_name}_idx'
            table_args.append(Index(index_name, field))
        return tuple(table_args)

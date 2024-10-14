from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Text, func, text
from sqlalchemy.orm import relationship

from app.configuration.database import Base


class Author(Base):
    """Авторы"""

    __tablename__ = 'Author'
    __table_args__ = {'comment': 'Авторы'}

    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, comment='Идентификатор', index=True)
    deleted: bool = Column(Boolean, nullable=False, default=False, server_default=text('false'),
                           comment='Отметка об удалении')
    pseudonym: str = Column(String, nullable=False, comment='Псевдоним автора')
    info: str = Column(Text, nullable=True,
                       comment='Краткая информация об авторе')


class Collection(Base):
    """Сборники"""

    __tablename__ = 'Collection'
    __table_args__ = {'comment': 'Сборники'}

    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, comment='Идентификатор', index=True)
    deleted: bool = Column(Boolean, nullable=False, default=False, server_default=text('false'),
                           comment='Отметка об удалении')
    author_id: int = Column(Integer, ForeignKey(
        'Author.id'), nullable=False, comment='{Author}')
    idx: int = Column(Integer, nullable=False, default=1,
                      comment='Индекс для сортировки')
    name: str = Column(String, nullable=False, comment='Название')
    description: str = Column(String, nullable=True, default=None, server_default=text('null'),
                              comment='Описание')
    publish_date: datetime = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now,
                                    server_default=func.now(), comment='Дата публикации')

    author = relationship('Author', backref='Collection')


class Poem(Base):
    """Стихотворения"""

    __tablename__ = 'Poem'
    __table_args__ = {'comment': 'Стихотворения'}

    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, comment='Идентификатор')
    deleted: bool = Column(Boolean, nullable=False, default=False, server_default=text('false'),
                           comment='Отметка об удалении')
    author_id: int = Column(Integer, ForeignKey(
        'Author.id'), nullable=False, comment='{Author}')
    name: str = Column(String, nullable=False, comment='Название')
    content: str = Column(Text, nullable=False, comment='Содержимое')
    parent_id: int = Column(Integer, default=None, server_default=text('null'),
                            comment='Прошлая версия стихотворения')
    create_date: datetime = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now,
                                   server_default=func.now(), comment='Дата создания')

    author = relationship('Author', backref='Poem')


class CollectionPoem(Base):
    """Связь стихотворения и сборника"""

    __tablename__ = 'CollectionPoem'
    __table_args__ = {'comment': 'Связь стихотворения и сборника'}

    collection_id: int = Column(Integer, ForeignKey(
        'Collection.id'), primary_key=True, nullable=False, comment='{Collection}')
    poem_id: int = Column(Integer, ForeignKey(
        'Poem.id'), primary_key=True, nullable=False, comment='{Poem}')
    idx: int = Column(Integer, nullable=False, default=1,
                      comment='Индекс для сортировки')

    collection = relationship('Collection', backref='CollectionPoem')
    poem = relationship('Poem', backref='CollectionPoem')

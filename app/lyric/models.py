from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Text, text
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
                                    server_default=text('now()'), comment='Дата публикации')

    author = relationship('Author')


class Poem(Base):
    """Стихотворения"""

    __tablename__ = 'Poem'
    __table_args__ = {'comment': 'Стихотворения'}

    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, comment='Идентификатор')
    deleted: bool = Column(Boolean, nullable=False, default=False, server_default=text('false'),
                           comment='Отметка об удалении')
    collection_id: int = Column(Integer, ForeignKey(
        'Collection.id'), comment='{Collection}')
    idx: int = Column(Integer, nullable=False, default=1,
                      comment='Индекс для сортировки')
    name: str = Column(String, nullable=False, comment='Название')
    content: str = Column(Text, nullable=False, comment='Содержимое')
    create_date: datetime = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now,
                                   server_default=text('now()'), comment='Дата создания')

    collection = relationship('Collection')

from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, ForeignKey, Integer, String, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.configuration.database import Base


class Author(Base):
    """Авторы"""

    __tablename__ = 'Author'
    __table_args__ = {'comment': 'Авторы'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    autoincrement=True, comment='Идентификатор', index=True)
    deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text('false'),
                                          comment='Отметка об удалении')
    pseudonym: Mapped[str] = mapped_column(
        String, nullable=False, comment='Псевдоним автора')
    info: Mapped[str] = mapped_column(
        Text, nullable=True, comment='Краткая информация об авторе')

    collections: Mapped[list['Collection']] = relationship(
        'Collection', back_populates='author')
    poems: Mapped[list['Poem']] = relationship('Poem', back_populates='author')


class Collection(Base):
    """Сборники"""

    __tablename__ = 'Collection'
    __table_args__ = {'comment': 'Сборники'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    autoincrement=True, comment='Идентификатор', index=True)
    deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text('false'),
                                          comment='Отметка об удалении')
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'Author.id'), nullable=False, comment='{Author}')
    idx: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, comment='Индекс для сортировки')
    name: Mapped[str] = mapped_column(
        String, nullable=False, comment='Название')
    description: Mapped[str] = mapped_column(String, nullable=True, default=None, server_default=text('null'),
                                             comment='Описание')
    publish_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now,
                                                   server_default=func.now(), comment='Дата публикации')

    author: Mapped[Author] = relationship(
        'Author', back_populates='collections')
    poems: Mapped[list['Poem']] = relationship(
        'Poem', secondary='CollectionPoem', back_populates='collections')


class Poem(Base):
    """Стихотворения"""

    __tablename__ = 'Poem'
    __table_args__ = {'comment': 'Стихотворения'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    autoincrement=True, comment='Идентификатор')
    deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text('false'),
                                          comment='Отметка об удалении')
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        'Author.id'), nullable=False, comment='{Author}')
    name: Mapped[str] = mapped_column(
        String, nullable=False, comment='Название')
    content: Mapped[str] = mapped_column(
        Text, nullable=False, comment='Содержимое')
    parent_id: Mapped[int] = mapped_column(Integer, default=None, server_default=text('null'),
                                           comment='Прошлая версия стихотворения')
    create_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now,
                                                  server_default=func.now(), comment='Дата создания')

    author: Mapped[Author] = relationship('Author', back_populates='poems')
    collections: Mapped[list['Collection']] = relationship('Collection', secondary='CollectionPoem',
                                                           back_populates='poems')


class CollectionPoem(Base):
    """Связь стихотворения и сборника"""

    __tablename__ = 'CollectionPoem'
    __table_args__ = {'comment': 'Связь стихотворения и сборника'}

    collection_id: Mapped[int] = mapped_column(Integer, ForeignKey('Collection.id'),
                                               primary_key=True, nullable=False, comment='{Collection}')
    poem_id: Mapped[int] = mapped_column(Integer, ForeignKey('Poem.id'),
                                         primary_key=True, nullable=False, comment='{Poem}')
    idx: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, comment='Индекс для сортировки')

from sqlalchemy import Column, Integer, Boolean, String, text, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.configuration.database import Base


class Poem(Base):
    """Стихотворения"""

    __tablename__ = 'Poem'
    __table_args__ = {'comment': 'Стихотворения'}

    id: int = Column(Integer, primary_key=True, comment='Идентификатор')
    deleted:  bool = Column(Boolean, nullable=False, default=False, server_default=text('false'), comment='Отметка об '
                                                                                                          'удалении')
    album_id: int = Column(Integer, ForeignKey('Album.id'), comment='{Album}')
    name: str = Column(String, comment='Название стихотворения')
    content: str = Column(Text, nullable=False, comment='Само стихотворение')

    album = relationship('Album')


class Album(Base):
    """Сборники"""

    __tablename__ = 'Album'
    __table_args__ = {'comment': 'Сборники'}

    id: int = Column(Integer, primary_key=True, comment='Идентификатор')
    deleted:  bool = Column(Boolean, nullable=False, default=False, server_default=text('false'), comment='Отметка об '
                                                                                                          'удалении')
    name: str = Column(String, comment='Название сборника')
    author_id: int = Column(Integer, ForeignKey('Author.id'), comment='{Author}')

    author = relationship('Author')


class Author(Base):
    """Авторы"""

    __tablename__ = 'Author'
    __table_args__ = {'comment': 'Авторы'}

    id: int = Column(Integer, primary_key=True, comment='Идентификатор')
    deleted:  bool = Column(Boolean, nullable=False, default=False, server_default=text('false'), comment='Отметка об '
                                                                                                          'удалении')
    pseudonym: str = Column(String, comment='Псевдоним автора')
    info: str = Column(Text, nullable=False, comment='Информация об авторе')

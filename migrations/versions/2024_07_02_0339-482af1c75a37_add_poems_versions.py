"""add poems versions

Revision ID: 482af1c75a37
Revises: c9645c0fc77c
Create Date: 2024-07-02 03:39:53.906554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '482af1c75a37'
down_revision: Union[str, None] = 'c9645c0fc77c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CollectionPoem',
    sa.Column('collection_id', sa.Integer(), nullable=False, comment='{Collection}'),
    sa.Column('poem_id', sa.Integer(), nullable=False, comment='{Poem}'),
    sa.Column('idx', sa.Integer(), nullable=False, comment='Индекс для сортировки'),
    sa.ForeignKeyConstraint(['collection_id'], ['Collection.id'], ),
    sa.ForeignKeyConstraint(['poem_id'], ['Poem.id'], ),
    sa.PrimaryKeyConstraint('collection_id', 'poem_id'),
    comment='Связь стихотворения и сборника'
    )
    op.alter_column('Author', 'info',
               existing_type=sa.TEXT(),
               comment='Краткая информация об авторе',
               existing_comment='Информация об авторе',
               existing_nullable=True)
    op.add_column('Poem', sa.Column('author_id', sa.Integer(), nullable=False, comment='{Author}'))
    op.add_column('Poem', sa.Column('version', sa.Integer(), nullable=False, comment='Версия, чтобы была возможность редактировать'))
    op.drop_constraint('Poem_collection_id_fkey', 'Poem', type_='foreignkey')
    op.create_foreign_key(None, 'Poem', 'Author', ['author_id'], ['id'])
    op.drop_column('Poem', 'collection_id')
    op.drop_column('Poem', 'idx')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Poem', sa.Column('idx', sa.INTEGER(), autoincrement=False, nullable=False, comment='Индекс для сортировки'))
    op.add_column('Poem', sa.Column('collection_id', sa.INTEGER(), autoincrement=False, nullable=True, comment='{Collection}'))
    op.drop_constraint(None, 'Poem', type_='foreignkey')
    op.create_foreign_key('Poem_collection_id_fkey', 'Poem', 'Collection', ['collection_id'], ['id'])
    op.drop_column('Poem', 'version')
    op.drop_column('Poem', 'author_id')
    op.alter_column('Author', 'info',
               existing_type=sa.TEXT(),
               comment='Информация об авторе',
               existing_comment='Краткая информация об авторе',
               existing_nullable=True)
    op.drop_table('CollectionPoem')
    # ### end Alembic commands ###

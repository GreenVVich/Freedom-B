"""add parent_id to poem

Revision ID: 3a4f2cabc22d
Revises: 482af1c75a37
Create Date: 2024-10-08 01:29:40.425757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a4f2cabc22d'
down_revision: Union[str, None] = '482af1c75a37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Poem', sa.Column('parent_id', sa.Integer(), server_default=sa.text('null'), nullable=True, comment='Прошлая версия стихотворения'))
    op.drop_column('Poem', 'version')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Poem', sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=False, comment='Версия, чтобы была возможность редактировать'))
    op.drop_column('Poem', 'parent_id')
    # ### end Alembic commands ###

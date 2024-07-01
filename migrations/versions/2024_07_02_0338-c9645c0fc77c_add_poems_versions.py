"""add poems versions

Revision ID: c9645c0fc77c
Revises: a1550c953198
Create Date: 2024-07-02 03:38:11.542343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9645c0fc77c'
down_revision: Union[str, None] = 'a1550c953198'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

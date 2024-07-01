"""add poems versions

Revision ID: a1550c953198
Revises: cfee9648658e
Create Date: 2024-07-02 03:30:10.077767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1550c953198'
down_revision: Union[str, None] = 'cfee9648658e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

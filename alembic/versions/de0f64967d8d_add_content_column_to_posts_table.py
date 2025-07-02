"""add content column to posts table

Revision ID: de0f64967d8d
Revises: 0751af839f87
Create Date: 2025-07-01 17:33:27.903079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de0f64967d8d'
down_revision: Union[str, Sequence[str], None] = '0751af839f87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

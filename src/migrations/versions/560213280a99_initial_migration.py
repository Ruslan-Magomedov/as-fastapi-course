"""initial migration

Revision ID: 560213280a99
Revises: 
Create Date: 2025-04-19 13:44:41.901449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '560213280a99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('hotels',
        sa.Column('hotel_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('hotel_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('hotels')

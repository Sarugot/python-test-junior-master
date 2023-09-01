"""initial

Revision ID: e1c42f493d8a
Revises: 
Create Date: 2023-08-31 15:25:47.978914

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e1c42f493d8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('user_ip', sa.VARCHAR(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###

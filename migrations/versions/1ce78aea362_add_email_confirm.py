"""add email_confirm

Revision ID: 1ce78aea362
Revises: 45a72275ae7
Create Date: 2015-07-21 21:20:20.191507

"""

# revision identifiers, used by Alembic.
revision = '1ce78aea362'
down_revision = '45a72275ae7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('email_confirm', sa.Boolean(), server_default='false', nullable=True))


def downgrade():
    op.drop_column('users', 'email_confirm')

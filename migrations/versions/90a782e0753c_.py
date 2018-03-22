"""empty message

Revision ID: 90a782e0753c
Revises: b9571035da71
Create Date: 2018-03-22 10:20:04.472338

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90a782e0753c'
down_revision = 'b9571035da71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('openned', 'modified_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('openned', sa.Column('modified_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###

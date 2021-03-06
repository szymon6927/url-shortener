"""empty message

Revision ID: 26f917576300
Revises: ed09a3a6bcda
Create Date: 2018-03-19 13:28:46.976982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26f917576300'
down_revision = 'ed09a3a6bcda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('opened',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('customer_hash', sa.String(length=60), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_hash'], ['customers.hash'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_customers_hash', table_name='customers')
    op.create_index(op.f('ix_customers_hash'), 'customers', ['hash'], unique=True)
    op.create_unique_constraint(None, 'customers', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='unique')
    op.drop_index(op.f('ix_customers_hash'), table_name='customers')
    op.create_index('ix_customers_hash', 'customers', ['hash'], unique=False)
    op.drop_table('opened')
    # ### end Alembic commands ###

"""empty message

Revision ID: f205d13cfa6d
Revises: 11551aecc7cb
Create Date: 2018-03-19 14:24:20.894749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f205d13cfa6d'
down_revision = '11551aecc7cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_customers_hash', table_name='customers')
    op.create_index(op.f('ix_customers_hash'), 'customers', ['hash'], unique=True)
    op.create_unique_constraint(None, 'customers', ['id'])
    op.drop_index('customer_hash', table_name='openned')
    op.drop_index('customer_id', table_name='openned')
    op.create_unique_constraint(None, 'openned', ['id'])
    op.drop_constraint('openned_ibfk_2', 'openned', type_='foreignkey')
    op.drop_constraint('openned_ibfk_1', 'openned', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('openned_ibfk_1', 'openned', 'customers', ['customer_hash'], ['hash'])
    op.create_foreign_key('openned_ibfk_2', 'openned', 'customers', ['customer_id'], ['id'])
    op.drop_constraint(None, 'openned', type_='unique')
    op.create_index('customer_id', 'openned', ['customer_id'], unique=True)
    op.create_index('customer_hash', 'openned', ['customer_hash'], unique=True)
    op.drop_constraint(None, 'customers', type_='unique')
    op.drop_index(op.f('ix_customers_hash'), table_name='customers')
    op.create_index('ix_customers_hash', 'customers', ['hash'], unique=False)
    # ### end Alembic commands ###
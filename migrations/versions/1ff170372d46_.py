"""empty message

Revision ID: 1ff170372d46
Revises: 
Create Date: 2021-04-25 22:03:46.838570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ff170372d46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('account', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('account')
    )
    op.create_index(op.f('ix_accounts_account'), 'accounts', ['account'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_accounts_account'), table_name='accounts')
    op.drop_table('accounts')
    # ### end Alembic commands ###

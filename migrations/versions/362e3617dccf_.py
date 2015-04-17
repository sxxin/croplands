"""empty message

Revision ID: 362e3617dccf
Revises: 3a16c9c72b69
Create Date: 2015-04-15 14:45:41.453715

"""

# revision identifiers, used by Alembic.
revision = '362e3617dccf'
down_revision = '3a16c9c72b69'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tile', sa.Column('x', sa.Integer(), nullable=False))
    op.add_column('tile', sa.Column('y', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tile', 'y')
    op.drop_column('tile', 'x')
    ### end Alembic commands ###
"""empty message

Revision ID: 175003d01257
Revises: a44d7cf0ded
Create Date: 2015-04-15 11:58:41.008454

"""

# revision identifiers, used by Alembic.
revision = '175003d01257'
down_revision = 'a44d7cf0ded'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tile', sa.Column('date_acquired', sa.DateTime(), nullable=True))
    op.add_column('tile', sa.Column('date_acquired_earliest', sa.DateTime(), nullable=True))
    op.add_column('tile', sa.Column('date_acquired_latest', sa.DateTime(), nullable=True))
    op.add_column('tile', sa.Column('date_modified', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tile', 'date_modified')
    op.drop_column('tile', 'date_acquired_latest')
    op.drop_column('tile', 'date_acquired_earliest')
    op.drop_column('tile', 'date_acquired')
    ### end Alembic commands ###
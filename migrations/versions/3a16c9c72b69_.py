"""empty message

Revision ID: 3a16c9c72b69
Revises: 4986e64643f4
Create Date: 2015-04-15 13:44:24.440623

"""

# revision identifiers, used by Alembic.
revision = '3a16c9c72b69'
down_revision = '4986e64643f4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tile', sa.Column('zoom', sa.Integer(), nullable=False))
    op.drop_constraint(u'tile_feature_id_key', 'tile', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'tile_feature_id_key', 'tile', ['feature_id'])
    op.drop_column('tile', 'zoom')
    ### end Alembic commands ###

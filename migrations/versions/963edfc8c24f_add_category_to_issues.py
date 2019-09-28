"""Add category to issues

Revision ID: 963edfc8c24f
Revises: 7f7d2e46c7ba
Create Date: 2019-06-30 05:17:23.141343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '963edfc8c24f'
down_revision = '7f7d2e46c7ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('catrgory', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issues', 'catrgory')
    # ### end Alembic commands ###
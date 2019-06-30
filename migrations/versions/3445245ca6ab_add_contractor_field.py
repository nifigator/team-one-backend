"""Add contractor field

Revision ID: 3445245ca6ab
Revises: 24acca22903b
Create Date: 2019-06-30 13:19:42.268015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3445245ca6ab'
down_revision = '24acca22903b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('constractor', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issues', 'constractor')
    # ### end Alembic commands ###

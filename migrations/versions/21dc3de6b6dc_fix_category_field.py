"""Fix category field

Revision ID: 21dc3de6b6dc
Revises: 963edfc8c24f
Create Date: 2019-06-30 06:31:00.421688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21dc3de6b6dc'
down_revision = '963edfc8c24f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('category', sa.String(length=128), nullable=False))
    op.drop_column('issues', 'catrgory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('catrgory', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_column('issues', 'category')
    # ### end Alembic commands ###

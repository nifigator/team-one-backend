"""Add relation issues - categories

Revision ID: 651c1ff8d8a5
Revises: 04ec85fc18d6
Create Date: 2019-09-28 17:00:00.520133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651c1ff8d8a5'
down_revision = '04ec85fc18d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('category_id', sa.Integer, nullable=True))
    op.create_foreign_key(None, 'issues', 'categories', ['category_id'], ['id'])
    op.drop_column('issues', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('category', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'issues', type_='foreignkey')
    op.drop_column('issues', 'category_id')
    # ### end Alembic commands ###

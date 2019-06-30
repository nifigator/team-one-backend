"""Add deault for status

Revision ID: e73fc220567d
Revises: 21dc3de6b6dc
Create Date: 2019-06-30 11:19:06.004396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e73fc220567d'
down_revision = '21dc3de6b6dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('issues', sa.Column('fake_filed', sa.Integer(), nullable=True))
    op.alter_column('issues', 'status', server_default='0')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('issues', 'fake_filed')
    # ### end Alembic commands ###

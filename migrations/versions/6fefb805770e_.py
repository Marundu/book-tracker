"""empty message

Revision ID: 6fefb805770e
Revises: 4f130f1d59e6
Create Date: 2019-03-14 09:37:16.973329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fefb805770e'
down_revision = '4f130f1d59e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'categories', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
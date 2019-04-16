"""empty message

Revision ID: 11b972685b8d
Revises: 641e8f4ab54d
Create Date: 2019-04-04 14:48:01.230154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b972685b8d'
down_revision = '641e8f4ab54d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('declined', sa.Boolean(), nullable=True))
    op.add_column('applications', sa.Column('waitlisted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('applications', 'waitlisted')
    op.drop_column('applications', 'declined')
    # ### end Alembic commands ###
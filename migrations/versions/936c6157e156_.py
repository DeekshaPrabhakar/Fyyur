"""empty message

Revision ID: 936c6157e156
Revises: 794adb705826
Create Date: 2020-06-21 21:51:28.313759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936c6157e156'
down_revision = '794adb705826'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###

"""inline_tags

Revision ID: a92d92aa678e
Revises: a10d1ef03050
Create Date: 2018-05-10 15:41:28.053237

"""
import re
from funcy import flatten, compact
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from redash import models

# revision identifiers, used by Alembic.
revision = 'a92d92aa678e'
down_revision = 'a10d1ef03050'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dashboards', sa.Column('tags', postgresql.ARRAY(sa.Unicode()), nullable=True))
    op.add_column('queries', sa.Column('tags', postgresql.ARRAY(sa.Unicode()), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('queries', 'tags')
    op.drop_column('dashboards', 'tags')
    # ### end Alembic commands ###

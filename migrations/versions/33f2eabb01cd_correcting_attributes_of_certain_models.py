"""Correcting attributes of certain models

Revision ID: 33f2eabb01cd
Revises: 
Create Date: 2023-07-26 13:17:15.782603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f2eabb01cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('date_birth', sa.Date(), nullable=False),
    sa.Column('type_document', sa.Enum(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('garment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=60), nullable=False),
    sa.Column('colour', sa.String(length=30), nullable=False),
    sa.Column('size', sa.String(length=3), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outfit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('occasion', sa.String(length=60), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('daily_recommendation', sa.Enum(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outfit_garment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=60), nullable=False),
    sa.Column('outfit_id', sa.Integer(), nullable=False),
    sa.Column('garment_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['garment_id'], ['garment.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['outfit_id'], ['outfit.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('outfit_garment')
    op.drop_table('outfit')
    op.drop_table('garment')
    op.drop_table('user')
    # ### end Alembic commands ###

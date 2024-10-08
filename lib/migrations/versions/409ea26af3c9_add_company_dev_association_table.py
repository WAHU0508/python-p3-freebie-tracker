"""Add company_dev Association Table

Revision ID: 409ea26af3c9
Revises: 26667fa5e020
Create Date: 2024-09-12 20:05:09.909374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '409ea26af3c9'
down_revision = '26667fa5e020'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_devs',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_company_devs_company_id_companies')),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_company_devs_dev_id_devs')),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_devs')
    # ### end Alembic commands ###

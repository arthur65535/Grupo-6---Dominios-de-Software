"""Adiciona e remove campos de MedicalBed

Revision ID: e4d92d9da534
Revises: f5da43b23880
Create Date: 2023-02-16 14:56:01.603791

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel  # Add support for SQLModel


# revision identifiers, used by Alembic.
revision = 'e4d92d9da534'
down_revision = 'f5da43b23880'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_bed', sa.Column('number', sa.Integer(), nullable=False))
    op.drop_column('medical_bed', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_bed', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('medical_bed', 'number')
    # ### end Alembic commands ###

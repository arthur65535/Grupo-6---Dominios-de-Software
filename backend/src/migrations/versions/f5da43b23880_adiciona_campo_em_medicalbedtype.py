"""Adiciona campo em MedicalBedType

Revision ID: f5da43b23880
Revises: 89ce8502827a
Create Date: 2023-02-16 14:50:07.957548

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel  # Add support for SQLModel


# revision identifiers, used by Alembic.
revision = 'f5da43b23880'
down_revision = '89ce8502827a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_bed_type', sa.Column('specialty', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('medical_bed_type', 'specialty')
    # ### end Alembic commands ###

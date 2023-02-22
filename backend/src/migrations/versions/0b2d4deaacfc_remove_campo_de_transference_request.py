"""Remove campo de transference_request

Revision ID: 0b2d4deaacfc
Revises: 46d87b732395
Create Date: 2023-02-21 15:51:43.188956

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel  # Add support for SQLModel


# revision identifiers, used by Alembic.
revision = '0b2d4deaacfc'
down_revision = '46d87b732395'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('transference_request_patient_transference_id_key', 'transference_request', type_='unique')
    op.drop_constraint('transference_request_patient_transference_id_fkey', 'transference_request', type_='foreignkey')
    op.drop_column('transference_request', 'patient_transference_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transference_request', sa.Column('patient_transference_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('transference_request_patient_transference_id_fkey', 'transference_request', 'patient_transference', ['patient_transference_id'], ['id'])
    op.create_unique_constraint('transference_request_patient_transference_id_key', 'transference_request', ['patient_transference_id'])
    # ### end Alembic commands ###
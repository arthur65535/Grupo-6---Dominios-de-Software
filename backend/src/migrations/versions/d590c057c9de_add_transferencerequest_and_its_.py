"""Add TransferenceRequest and its relationships

Revision ID: d590c057c9de
Revises: cf238366b9d7
Create Date: 2023-02-06 18:20:06.120935

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel  # Add support for SQLModel


# revision identifiers, used by Alembic.
revision = 'd590c057c9de'
down_revision = 'cf238366b9d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient_transference',
    sa.Column('authorization_datetime', sa.DateTime(), nullable=False),
    sa.Column('in_transit_datetime', sa.DateTime(), nullable=False),
    sa.Column('completed_datetime', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('AUTHORIZED', 'IN_TRANSIT', 'COMPLETED', name='patienttransferencestatus'), nullable=False),
    sa.Column('transference_request_id', sa.Integer(), nullable=False),
    sa.Column('emd_doctor_id', sa.Integer(), nullable=False),
    sa.Column('destination_hospital_id', sa.Integer(), nullable=False),
    sa.Column('receiving_doctor_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['destination_hospital_id'], ['hospital.id'], ),
    sa.ForeignKeyConstraint(['emd_doctor_id'], ['emd_doctor.id'], ),
    sa.ForeignKeyConstraint(['receiving_doctor_id'], ['doctor.id'], ),
    sa.ForeignKeyConstraint(['transference_request_id'], ['transference_request.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transference_request_id')
    )
    op.add_column('transference_request', sa.Column('requesting_hospital_id', sa.Integer(), nullable=False))
    op.add_column('transference_request', sa.Column('patient_transference_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'transference_request', ['patient_transference_id'])
    op.drop_constraint('transference_request_emd_doctor_id_fkey', 'transference_request', type_='foreignkey')
    op.create_foreign_key(None, 'transference_request', 'hospital', ['requesting_hospital_id'], ['id'])
    op.create_foreign_key(None, 'transference_request', 'patient_transference', ['patient_transference_id'], ['id'])
    op.drop_column('transference_request', 'emd_doctor_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transference_request', sa.Column('emd_doctor_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'transference_request', type_='foreignkey')
    op.drop_constraint(None, 'transference_request', type_='foreignkey')
    op.create_foreign_key('transference_request_emd_doctor_id_fkey', 'transference_request', 'emd_doctor', ['emd_doctor_id'], ['id'])
    op.drop_constraint(None, 'transference_request', type_='unique')
    op.drop_column('transference_request', 'patient_transference_id')
    op.drop_column('transference_request', 'requesting_hospital_id')
    op.drop_table('patient_transference')
    # ### end Alembic commands ###

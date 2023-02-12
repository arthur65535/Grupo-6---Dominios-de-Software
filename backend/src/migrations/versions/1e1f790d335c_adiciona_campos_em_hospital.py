"""Adiciona campos em Hospital

Revision ID: 1e1f790d335c
Revises: 0a5f183a886e
Create Date: 2023-02-11 22:19:12.924277

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.databases import postgres
import sqlmodel  # Add support for SQLModel


# revision identifiers, used by Alembic.
revision = '1e1f790d335c'
down_revision = '0a5f183a886e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    # Code snippet necessary because of Alembic bug described in
    # https://github.com/sqlalchemy/alembic/issues/278
    hospital_management = postgres.ENUM('ESTADUAL', 'MUNICIPAL', 'DUPLA',
                                        name='hospital_management')
    hospital_management_type = postgres.ENUM(
        'ADMINISTRACAL_PUBLICA', 'ENTIDADES_EMPRESARIAIS',
        'ENTIDADES_SEM_FINS_LUCRATIVOS', 'ORGANIZACOES_INTERNACIONAIS_OUTRAS',
        'PESSOAS_FISICAS', name='hospital_management_type')
    hospital_management.create(op.get_bind(), checkfirst=True)
    hospital_management_type.create(op.get_bind(), checkfirst=True)

    op.add_column('hospital', sa.Column('initials', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('CNES', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('phone_number_1', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('phone_number_2', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('hospital', sa.Column('CNPJ', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('email_address', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('hospital', sa.Column('management', hospital_management, nullable=False))
    op.add_column('hospital', sa.Column('management_type', hospital_management_type, nullable=False))
    op.create_unique_constraint(None, 'hospital', ['CNPJ'])
    op.create_unique_constraint(None, 'hospital', ['CNES'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hospital', type_='unique')
    op.drop_constraint(None, 'hospital', type_='unique')
    op.drop_column('hospital', 'management_type')
    op.drop_column('hospital', 'management')
    op.drop_column('hospital', 'email_address')
    op.drop_column('hospital', 'CNPJ')
    op.drop_column('hospital', 'is_active')
    op.drop_column('hospital', 'phone_number_2')
    op.drop_column('hospital', 'phone_number_1')
    op.drop_column('hospital', 'CNES')
    op.drop_column('hospital', 'initials')
    # ### end Alembic commands ###

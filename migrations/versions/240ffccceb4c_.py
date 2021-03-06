"""empty message

Revision ID: 240ffccceb4c
Revises: c30b47d1034d
Create Date: 2021-05-31 18:53:01.358013

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '240ffccceb4c'
down_revision = 'c30b47d1034d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_letters')
    op.add_column('letters', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'letters', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'letters', type_='foreignkey')
    op.drop_column('letters', 'user_id')
    op.create_table('users_letters',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('letter_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['letter_id'], ['letters.id'], name='users_letters_letter_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='users_letters_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_letters_pkey')
    )
    # ### end Alembic commands ###

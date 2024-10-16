"""NewModel

Revision ID: b16ea939be69
Revises: 
Create Date: 2024-10-14 15:40:25.899539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b16ea939be69'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brands',
    sa.Column('brands_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('country', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('brands_id')
    )
    op.create_table('categories',
    sa.Column('categories_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('categories_id')
    )
    op.create_table('sneakers',
    sa.Column('sneaker_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('size', sa.VARCHAR(), nullable=True),
    sa.Column('color', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('image_url', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.brands_id'], ),
    sa.ForeignKeyConstraint(['category'], ['categories.categories_id'], ),
    sa.PrimaryKeyConstraint('sneaker_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sneakers')
    op.drop_table('categories')
    op.drop_table('brands')
    # ### end Alembic commands ###

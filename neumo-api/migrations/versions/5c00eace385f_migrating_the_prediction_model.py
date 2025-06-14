"""migrating the prediction model

Revision ID: 5c00eace385f
Revises: ef1d3bef2583
Create Date: 2025-06-13 10:18:47.665787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c00eace385f'
down_revision: Union[str, None] = 'ef1d3bef2583'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('predictions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('image_filename', sa.String(), nullable=False),
    sa.Column('prediction_class', sa.String(), nullable=False),
    sa.Column('confidence_score', sa.Float(), nullable=False),
    sa.Column('inference_time_ms', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('reviewed_by_doctor', sa.Boolean(), nullable=True),
    sa.Column('doctor_notes', sa.Text(), nullable=True),
    sa.Column('doctor_diagnosis', sa.String(), nullable=True),
    sa.Column('patient_age', sa.Integer(), nullable=True),
    sa.Column('patient_gender', sa.String(), nullable=True),
    sa.Column('patient_symptoms', sa.Text(), nullable=True),
    sa.Column('is_flagged', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predictions_id'), 'predictions', ['id'], unique=False)
    op.create_index(op.f('ix_predictions_user_id'), 'predictions', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_predictions_user_id'), table_name='predictions')
    op.drop_index(op.f('ix_predictions_id'), table_name='predictions')
    op.drop_table('predictions')
    # ### end Alembic commands ###

import uuid

from django.db.models import UUIDField
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

import uuid
from datetime import timezone
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, hard_delete=False, *args, **kwargs):
        if hard_delete:
            return super().delete(*args, *kwargs)
        
        self.deleted_at = timezone.now()
        self.save()

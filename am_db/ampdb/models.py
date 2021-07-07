from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class PDBQuery(models.Model):
    query_id = models.CharField(max_length=200)
    pub_date = timezone.now()

    def __str__(self):
        return self.query_id
    

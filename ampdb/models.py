from django.db import models
from django.utils import timezone
import datetime


class PDBQuery(models.Model):
    query_id = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Proteins(models.Model):
    name = models.CharField(("Name"), max_length=255)
    sequence = models.CharField(("Sequence"), max_length=500)
    molecular_weight = models.FloatField(("MolecularMolecularWeight"))
    length = models.IntegerField(("Length"))
    charge = models.FloatField(("Charge"))
    p_i = models.FloatField(("pI"))
    a_index = models.FloatField(("AIndex"))
    instaIndex = models.FloatField(("InstaIndex"))
    BomanIndex = models.FloatField(("BomanIndex"))
    hydrophobicity = models.FloatField(("Hydrophobicity"))
    hmoment_angle = models.FloatField(("MomentAngle"))
    hmoment_2 = models.FloatField(("Moment2"))
    pdb_id = models.CharField(("PDBID"), max_length=256)

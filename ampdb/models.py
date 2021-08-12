from django.db import models
from django.utils import timezone
import datetime


class PDBQuery(models.Model):
    query_id = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Proteins(models.Model):
    name = models.CharField(("Name"), max_length=255)
    sequence = models.CharField(("Sequence"), max_length=500)
    hydrolitic_activity = models.FloatField(("HydrolyticActivity"))
    mic_value = models.FloatField(("MICValue"))
    solubility = models.CharField(("Solubility"), max_length=256)
    tiny = models.IntegerField(("Tiny"))
    small = models.IntegerField(("Small"))
    aliphatic = models.IntegerField(("Aliphatic"))
    aromatic = models.IntegerField(("Aromatic"))
    non_polar = models.IntegerField(("NonPolar"))
    polar = models.IntegerField(("Polar"))
    charged_aa = models.IntegerField(("ChargedAA"))
    basic = models.IntegerField(("Basic"))
    acidic = models.FloatField(("Acidic"))
    mol_weight_timy = models.FloatField(("MolWeightTiny"))
    mol_weight_small = models.FloatField(("MolWeightSmall"))
    mol_weight_apliphatic = models.FloatField(("MolWeightAliphatic"))
    mol_weight_aromatic = models.FloatField(("MolWeightAromatic"))
    mol_weight_non_polar = models.FloatField(("MolWeightNonPolar"))
    mol_weight_polar = models.FloatField(("MolWeightPolar"))
    mol_weight_charged = models.FloatField(("MolWeightCharged"))
    mol_weight_basic = models.FloatField(("MolWeightBasic"))
    mol_weight_acidic = models.FloatField(("MolWeightAcidic"))
    molecular_weight = models.FloatField(("MolecularWeight"))
    length = models.IntegerField(("Length"))
    charge = models.FloatField(("Charge"))
    p_i = models.FloatField(("pI"))
    a_index = models.FloatField(("AIndex"))
    instaIndex = models.FloatField(("InstaIndex"))
    BomanIndex = models.FloatField(("BomanIndex"))
    hydrophobicity = models.FloatField(("Hydrophobicity"))
    hmoment_angle = models.FloatField(("HydrophobicMoment"))
    transmembrane = models.IntegerField(("Transmembrane"))
    extracellular = models.CharField(("Extracellular"), max_length=256)
    cytoplasmic = models.CharField(("Cytoplasmic"), max_length=256)
    hydrophobic_plots = models.FloatField(("HydrophobicPlots"))
    hydropathy_plots = models.FloatField(("HydropathyPlots"))
    disulfide_end = models.CharField(("DisulfideEnd"), max_length=256)
    toxicity = models.CharField(("Toxicity"), max_length=256)
    rmsf = models.FloatField(("RMSF"))
    flexibility = models.FloatField(("Flexibility"))
    pdb_name = models.CharField(("PDBName"), max_length=256)
    links = models.CharField(("Links"), max_length=256)

    def __str__(self):
        return self.name

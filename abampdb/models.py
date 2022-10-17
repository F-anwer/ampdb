# import datetime

from django.db import models
# from django.utils import timezone


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
    mol_weight_tiny = models.FloatField(("MolWeightTiny"))
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
    extracellular = models.BooleanField(("Extracellular"))
    cytoplasmic = models.BooleanField(("Cytoplasmic"))
    hydrophobic_plots = models.FloatField(("HydrophobicPlots"))
    hydropathy_plots = models.FloatField(("HydropathyPlots"))
    disulfide_end = models.CharField(("DisulfideEnd"), max_length=256)
    toxicity = models.CharField(("Toxicity"), max_length=256)
    rmsf = models.FloatField(("RMSF"))
    flexibility = models.FloatField(("Flexibility"))
    pdb_name = models.CharField(("PDBName"), max_length=256)
    score = models.IntegerField(("Score"))
    docked = models.CharField(("Docked"), max_length=256)

    def __str__(self):
        return self.name


class Dock_Proteins(models.Model):

    pdb_name = models.ForeignKey(Proteins, on_delete=models.CASCADE)
    dock_1 = models.CharField(("dock_1"), max_length=256)
    dock_2 = models.CharField(("dock_2"), max_length=256)
    dock_3 = models.CharField(("dock_3"), max_length=256)
    dock_4 = models.CharField(("dock_4"), max_length=256)
    dock_5 = models.CharField(("dock_5"), max_length=256)
    dock_6 = models.CharField(("dock_6"), max_length=256)
    dock_7 = models.CharField(("dock_7"), max_length=256)
    dock_8 = models.CharField(("dock_8"), max_length=256)
    dock_9 = models.CharField(("dock_9"), max_length=256)
    dock_10 = models.CharField(("dock_10"), max_length=256)
    dock_11 = models.CharField(("dock_11"), max_length=256)
    dock_12 = models.CharField(("dock_12"), max_length=256)
    dock_13 = models.CharField(("dock_13"), max_length=256)
    dock_14 = models.CharField(("dock_14"), max_length=256)
    dock_15 = models.CharField(("dock_15"), max_length=256)
    dock_16 = models.CharField(("dock_16"), max_length=256)
    dock_17 = models.CharField(("dock_17"), max_length=256)
    dock_18 = models.CharField(("dock_18"), max_length=256)
    dock_19 = models.CharField(("dock_19"), max_length=256)
    dock_20 = models.CharField(("dock_20"), max_length=256)
    dock_21 = models.CharField(("dock_21"), max_length=256)
    dock_22 = models.CharField(("dock_22"), max_length=256)
    dock_23 = models.CharField(("dock_23"), max_length=256)
    dock_24 = models.CharField(("dock_24"), max_length=256)
    dock_25 = models.CharField(("dock_25"), max_length=256)
    dock_26 = models.CharField(("dock_26"), max_length=256)
    dock_27 = models.CharField(("dock_27"), max_length=256)
    dock_28 = models.CharField(("dock_28"), max_length=256)
    dock_29 = models.CharField(("dock_29"), max_length=256)
    dock_30 = models.CharField(("dock_30"), max_length=256)


def __str__(self):
    return f"Name:{self.pdb_name}"
    
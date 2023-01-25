# import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone


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
    disulfide_end = models.CharField(("disulphides"), max_length=256)
    toxicity = models.CharField(("Toxicity"), max_length=256)
    rmsf = models.FloatField(("RMSF"))
    flexibility = models.FloatField(("Flexibility"))
    score = models.IntegerField(("Score"))
    pdb_name = models.CharField(("PDBName"), max_length=256)
    


class Dock_Proteins(models.Model):
    name = models.CharField(max_length=255)
    proteins = models.ManyToManyField(Proteins, related_name='dock_protein')

class PDBSQuery(models.Model):
    query_id = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id

class Synthetic(models.Model):

    title = models.CharField(("Title"), max_length=255)
    name = models.CharField(("Name"), max_length=255)
    synthetic_Sequence = models.CharField(("Synthetic_sequence"), max_length=500)
    synthetic_Tiny = models.IntegerField(("Tiny"))
    synthetic_Small = models.IntegerField(("Small"))
    synthetic_Aliphtic = models.IntegerField(("Synthetic_aliphatic"))
    synthetic_Aromatic = models.IntegerField(("Synthetic_aromatic"))
    synthetic_non_polar = models.IntegerField(("Synthetic_Non_Polar-aa"))
    synthetic_polar = models.IntegerField(("Synthetic_Polar-aa"))
    synthetic_charged_aa = models.IntegerField(("Synthetic_Charged-aa"))
    synthetic_basic = models.IntegerField(("Synthetic_Basic-aa"))
    synthetic_acidic = models.CharField(("Synthetic_Acidic-aa"), max_length=255)
    synthetic_mol_weight_tiny = models.FloatField(("Synthetic_Mole%-Tiny_aa"), max_length=255)
    synthetic_mol_weight_small = models.FloatField(("Synthetic_Mole%-Small_aa"), max_length=255)
    synthetic_mol_weight_apliphatic = models.FloatField(("Synthetic_Mole%-Aliphtic_aa"), max_length=255)
    synthetic_mol_weight_aromatic = models.CharField(("Synthetic_Mole%-Aromatic_aa"), max_length=255)
    synthetic_mol_weight_non_polar = models.FloatField(("Synthetic_Mole%-Non_Polar_aa"), max_length=255)
    synthetic_mol_weight_polar = models.FloatField(("Synthetic_Mole%-Polar_aa"), max_length=255)
    synthetic_mol_weight_charged = models.FloatField(("Synthetic_Mole%-Charged_aa"), max_length=255)
    synthetic_mol_weight_basic = models.FloatField(("Synthetic_Mole%-Basic_aa"), max_length=255, default=None)
    synthetic_mol_weight_acidic = models.IntegerField(("Synthetic_Mole%-Acidic_aa"), default=None)
    synthetic_molecular_weight = models.FloatField(("Synthetic_mw"), max_length=255, default=None)
    synthetic_length = models.IntegerField(("Synthetic_length"), default=None)
    synthetic_charge = models.FloatField(("Synthetic_Charge"), max_length=255, default=None)
    synthetic_isolelectric_point = models.FloatField(("Synthetic_Isolelectric point"), max_length=255)
    synthetic_aliphatic_Index = models.FloatField(("Synthetic_Aliphatic Index"), max_length=255, default=None)
    synthetic_instability_Index = models.FloatField(("Synthetic_Instability Index"), max_length=255)
    synthetic_bomanIndex = models.FloatField(("Synthetic_BomanIndex"), max_length=255)
    synthetic_hydrophobicity = models.FloatField(("Synthetic_Hydrophobicity"), max_length=255)
    synthetic_hydrophobic_moment = models.FloatField(("Synthetic_Hydrophobic moment"), max_length=255)
    synthetic_toxicity = models.CharField(("Synthetic_Toxicity"), max_length=255, default=None)
    synthetic_hemolytic_activity = models.FloatField(("Synthetic_Hemolytic activity"), max_length=255)
    synthetic_score = models.IntegerField(("Synthetic_Score"), default=None)
    synthetic_pdb_name = models.CharField(("Synthetic_PDBName"), max_length=255, default=None)

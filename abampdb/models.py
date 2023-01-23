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

    def __str__(self):
        return self.name

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
    synthetic_Aromatic = models.CharField(("Synthetic_aromatic"), max_length=500)
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
    synthetic_mol_weight_acidic = models.FloatField(("Synthetic_Mole%-Acidic_aa"), max_length=255, default=None)
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

class Dock_Proteins(models.Model):
	title = models.CharField(_("title"), max_length=255)
	dock_1 = models.CharField(_("dock_1"), max_length=255)
	dock_2 = models.CharField(_("dock_2"), max_length=256)
	dock_3 = models.CharField(_("dock_3"), max_length=256)
	dock_4 = models.CharField(_("dock_4"), max_length=256)
	dock_5 = models.CharField(_("dock_5"), max_length=256)
	dock_6 = models.CharField(_("dock_6"), max_length=256)
	dock_7 = models.CharField(_("dock_7"), max_length=256)
	dock_8 = models.CharField(_("dock_8"), max_length=256)
	dock_9 = models.CharField(_("dock_9"), max_length=256)
	dock_10 = models.CharField(_("dock_10"), max_length=256)
	dock_11 = models.CharField(_("dock_11"), max_length=256)
	dock_12 = models.CharField(_("dock_12"), max_length=256)
	dock_13 = models.CharField(_("dock_13"), max_length=256)
	dock_14 = models.CharField(_("dock_14"), max_length=256)
	dock_15 = models.CharField(_("dock_15"), max_length=256)
	dock_16 = models.CharField(_("dock_16"), max_length=256)
	dock_17 = models.CharField(_("dock_17"), max_length=256)
	dock_18 = models.CharField(_("dock_18"), max_length=256)
	dock_19 = models.CharField(_("dock_19"), max_length=256)
	dock_20 = models.CharField(_("dock_20"), max_length=256)
	dock_21 = models.CharField(_("dock_21"), max_length=256)
	dock_22 = models.CharField(_("dock_22"), max_length=256)
	dock_23 = models.CharField(_("dock_23"), max_length=256)
	dock_23 = models.CharField(_("dock_23"), max_length=256)
	dock_24 = models.CharField(_("dock_24"), max_length=256)
	dock_25 = models.CharField(_("dock_25"), max_length=256)
	dock_26 = models.CharField(_("dock_26"), max_length=256)
	dock_27 = models.CharField(_("dock_27"), max_length=256)
	dock_28 = models.CharField(_("dock_28"), max_length=256)
	dock_29 = models.CharField(_("dock_29"), max_length=256)
	dock_30 = models.CharField(_("dock_30"), max_length=256)

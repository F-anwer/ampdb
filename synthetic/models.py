from django.db import models

# Create your models here.


class PDBSQuery(models.Model):
    synthetic_id = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.synthetic_id


class Synthetic(models.Model):
    title = models.CharField(("Title"), max_length=255)
    name = models.CharField(("Name"), max_length=255)
    s = models.CharField(
        ("Synthetic_sequence"), max_length=500)
    synthetic_Tiny = models.IntegerField(("Tiny"))
    synthetic_Small = models.IntegerField(("Small"))
    synthetic_Aliphtic = models.IntegerField(("Synthetic_aliphatic"))
    synthetic_Aromatic = models.IntegerField(("Synthetic_aromatic"))
    synthetic_non_polar = models.IntegerField(("Synthetic_Non_Polar-aa"))
    synthetic_polar = models.IntegerField(("Synthetic_Polar-aa"))
    synthetic_charged_aa = models.IntegerField(("Synthetic_Charged-aa"))
    synthetic_basic = models.IntegerField(("Synthetic_Basic-aa"))
    synthetic_acidic = models.CharField(
        ("Synthetic_Acidic-aa"), max_length=255)
    synthetic_mol_weight_tiny = models.FloatField(
        ("Synthetic_Mole%-Tiny_aa"), max_length=255)
    synthetic_mol_weight_small = models.FloatField(
        ("Synthetic_Mole%-Small_aa"), max_length=255)
    synthetic_mol_weight_apliphatic = models.FloatField(
        ("Synthetic_Mole%-Aliphtic_aa"), max_length=255)
    synthetic_mol_weight_aromatic = models.CharField(
        ("Synthetic_Mole%-Aromatic_aa"), max_length=255)
    synthetic_mol_weight_non_polar = models.FloatField(
        ("Synthetic_Mole%-Non_Polar_aa"), max_length=255)
    synthetic_mol_weight_polar = models.FloatField(
        ("Synthetic_Mole%-Polar_aa"), max_length=255)
    synthetic_mol_weight_charged = models.FloatField(
        ("Synthetic_Mole%-Charged_aa"), max_length=255)
    synthetic_mol_weight_basic = models.FloatField(
        ("Synthetic_Mole%-Basic_aa"), max_length=255, default=None)
    synthetic_mol_weight_acidic = models.IntegerField(
        ("Synthetic_Mole%-Acidic_aa"), default=None)
    synthetic_molecular_weight = models.FloatField(
        ("Synthetic_mw"), max_length=255, default=None)
    synthetic_length = models.IntegerField(("Synthetic_length"), default=None)
    synthetic_charge = models.FloatField(
        ("Synthetic_Charge"), max_length=255, default=None)
    synthetic_isolelectric_point = models.FloatField(
        ("Synthetic_Isolelectric point"), max_length=255)
    synthetic_aliphatic_Index = models.FloatField(
        ("Synthetic_Aliphatic Index"), max_length=255, default=None)
    synthetic_instability_Index = models.FloatField(
        ("Synthetic_Instability Index"), max_length=255)
    synthetic_bomanIndex = models.FloatField(
        ("Synthetic_BomanIndex"), max_length=255)
    synthetic_hydrophobicity = models.FloatField(
        ("Synthetic_Hydrophobicity"), max_length=255)
    synthetic_hydrophobic_moment = models.FloatField(
        ("Synthetic_Hydrophobic moment"), max_length=255)
    synthetic_toxicity = models.CharField(
        ("Synthetic_Toxicity"), max_length=255, default=None)
    synthetic_hemolytic_activity = models.FloatField(
        ("Synthetic_Hemolytic activity"), max_length=255)
    synthetic_score = models.IntegerField(("Synthetic_Score"), default=None)
    mutaions = models.CharField(
        ("Mutations"), max_length=255, default=None)
    mutaion_count = models.IntegerField(
        ("Mutation_count"), default=None)
    synthetic_pdb_name = models.CharField(
        ("Synthetic_PDBName"), max_length=255, default=None)

    def __str__(self):
        return self.title



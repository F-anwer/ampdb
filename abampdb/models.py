# import datetime

from django.db import models


class PDBTQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Targetproteins(models.Model):
    targets = models.CharField(("Targets"), max_length=1000)

    def __str__(self):
        return self.targets


class PDBQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Proteins(models.Model):
    target_protein = models.ForeignKey(
        Targetproteins, on_delete=models.SET_NULL, null=True, blank=True)
    dock = models.ManyToManyField('Docks', related_name='proteins')
    amp = models.CharField(("AMP"), max_length=1000)
    name = models.CharField(("Name"), max_length=1000)
    sequence = models.CharField(("Sequence"), max_length=1000)
    hemolytic_activity = models.CharField(("HemolyticActivity"), null=True, max_length=1000)
    mic_value = models.CharField(("MICValue"), null=True, max_length=1000)
    solubility = models.CharField(("Solubility"), max_length=1000)
    tiny = models.IntegerField(("Tiny"), null=True)
    small = models.IntegerField(("Small"), null=True)
    aliphatic = models.IntegerField(("Aliphatic"), null=True)
    aromatic = models.IntegerField(("Aromatic"), null=True)
    non_polar = models.IntegerField(("NonPolar"), null=True)
    polar = models.IntegerField(("Polar"), null=True)
    charged_aa = models.IntegerField(("ChargedAA"), null=True)
    basic = models.IntegerField(("Basic"), null=True)
    acidic = models.FloatField(("Acidic"), null=True)
    mol_weight_tiny = models.FloatField(("MolWeightTiny"), null=True)
    mol_weight_small = models.FloatField(("MolWeightSmall"), null=True)
    mol_weight_apliphatic = models.FloatField(
        ("MolWeightAliphatic"), null=True)
    mol_weight_aromatic = models.FloatField(("MolWeightAromatic"), null=True)
    mol_weight_non_polar = models.FloatField(("MolWeightNonPolar"), null=True)
    mol_weight_polar = models.FloatField(("MolWeightPolar"), null=True)
    mol_weight_charged = models.FloatField(("MolWeightCharged"), null=True)
    mol_weight_basic = models.FloatField(("MolWeightBasic"), null=True)
    mol_weight_acidic = models.FloatField(("MolWeightAcidic"), null=True)
    molecular_weight = models.FloatField(("MolecularWeight"), null=True)
    length = models.IntegerField(("Length"), null=True)
    charge = models.FloatField(("Charge"), null=True)
    p_i = models.FloatField(("pI"), null=True)
    a_index = models.FloatField(("AIndex"), null=True)
    instaIndex = models.FloatField(("InstaIndex"), null=True)
    BomanIndex = models.FloatField(("BomanIndex"), null=True)
    hydrophobicity = models.FloatField(("Hydrophobicity"), null=True)
    hmoment_angle = models.FloatField(("HydrophobicMoment"), null=True)
    extracellular = models.BooleanField(("Extracellular"), null=True)
    cytoplasmic = models.BooleanField(("Cytoplasmic"), null=True)
    toxicity = models.CharField(("Toxicity"), max_length=1000, null=True)
    rmsf = models.FloatField(("RMSF"), null=True)
    score = models.IntegerField(("Score"), null=True)
    pdb_name = models.CharField(("PDBName"), max_length=1000)

    def __str__(self):
        return self.amp


class PDBDQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Docks(models.Model):
    targets = models.ManyToManyField('Targetproteins')
    dock_1 = models.CharField(("Dock"), max_length=1000)
    image = models.CharField(("Image"), max_length=1000)
    global_energy = models.CharField(("Global_Energy"), max_length=1000)
    attr_vdw = models.CharField(("Attractive_VdW"), max_length=1000)
    repl_vdw = models.CharField(("Repulsive_VdW"), max_length=1000)
    binding_energy = models.CharField(("ACE"), max_length=1000)
    hydrogen_bonding = models.CharField(("HB"), max_length=1000)

    def __str__(self):
        return self.dock_1

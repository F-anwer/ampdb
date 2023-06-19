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
    target_protein = models.ForeignKey(Targetproteins, on_delete=models.SET_NULL, null=True, blank=True)
    dock = models.ManyToManyField('Docks', related_name='dock')
    amp = models.CharField(("AMP"), max_length=1000)
    name = models.CharField(("Name"), max_length=1000)
    sequence = models.CharField(("Sequence"), max_length=1000)
    hemolytic_activity = models.FloatField(("HemolyticActivity"), null=True)
    mic_value = models.FloatField(("MICValue"), null=True)
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
    mol_weight_apliphatic = models.FloatField(("MolWeightAliphatic"), null=True)
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
    transmembrane = models.IntegerField(("Transmembrane"), null=True)
    extracellular = models.BooleanField(("Extracellular"), null=True)
    cytoplasmic = models.BooleanField(("Cytoplasmic"), null=True)
    hydrophobic_plots = models.FloatField(("HydrophobicPlots"), null=True)
    hydropathy_plots = models.FloatField(("HydropathyPlots"), null=True)
    disulfide_end = models.CharField(("disulphides"), max_length=1000)
    toxicity = models.CharField(("Toxicity"), max_length=1000, null=True)
    rmsf = models.FloatField(("RMSF"), null=True)
    flexibility = models.FloatField(("Flexibility"), null=True)
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


class PDBSTQuery(models.Model):
    Stargetprotein_id = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.Stargetproteins_id

class Stargetproteins(models.Model):
    stargets = models.CharField(("Stargets"), max_length=1000, default=None, blank=True)

    def __str__(self):
        return self.stargets

class PDBSQuery(models.Model):
    synthetic_id = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.synthetic_id

class Synthetic(models.Model):
    starget_protein = models.ForeignKey(Stargetproteins, on_delete=models.SET_NULL, null=True, blank=True)
    sdock = models.ManyToManyField('Sdock', related_name='sdock')
    title = models.CharField(("Title"), max_length=255)
    name = models.CharField(("Name"), max_length=255)
    synthetic_Sequence = models.CharField(
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
    synthetic_pdb_name = models.CharField(
        ("Synthetic_PDBName"), max_length=255, default=None)

    def __str__(self):
        return self.title

class PDBSDQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id


class Sdock(models.Model):
    stargets = models.ManyToManyField('Stargetproteins')
    s_dock = models.CharField(("S_dock"), max_length=1000)
    image1 = models.CharField(("Image1"), max_length=1000)
    image2 = models.CharField(("Image2"), max_length=1000)
    rmsf_min = models.CharField(("RSMF_min"), max_length=1000)
    total_score_before_refinement = models.CharField(("Total_score_before_Refinement"), max_length=1000)
    i_sc_before_refinement = models.CharField(("I_sc_before_Refinement"), max_length=1000)
    bb_rmsd_before_refinement = models.CharField(("bb_RMSD_before_Refinement"), max_length=1000)
    total_score_after_refinement = models.CharField(("Total_score_after_Refinement"), max_length=1000)
    bb_rmsd_after_refinement = models.CharField(("bb_RMSD_after_Refinement"), max_length=1000)

def __str__(self):
        return self.s_dock
# Generated by Django 4.0.2 on 2023-01-22 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dock_Proteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('dock_1', models.CharField(max_length=255, verbose_name='dock_1')),
                ('dock_2', models.CharField(max_length=256, verbose_name='dock_2')),
                ('dock_3', models.CharField(max_length=256, verbose_name='dock_3')),
                ('dock_4', models.CharField(max_length=256, verbose_name='dock_4')),
                ('dock_5', models.CharField(max_length=256, verbose_name='dock_5')),
                ('dock_6', models.CharField(max_length=256, verbose_name='dock_6')),
                ('dock_7', models.CharField(max_length=256, verbose_name='dock_7')),
                ('dock_8', models.CharField(max_length=256, verbose_name='dock_8')),
                ('dock_9', models.CharField(max_length=256, verbose_name='dock_9')),
                ('dock_10', models.CharField(max_length=256, verbose_name='dock_10')),
                ('dock_11', models.CharField(max_length=256, verbose_name='dock_11')),
                ('dock_12', models.CharField(max_length=256, verbose_name='dock_12')),
                ('dock_13', models.CharField(max_length=256, verbose_name='dock_13')),
                ('dock_14', models.CharField(max_length=256, verbose_name='dock_14')),
                ('dock_15', models.CharField(max_length=256, verbose_name='dock_15')),
                ('dock_16', models.CharField(max_length=256, verbose_name='dock_16')),
                ('dock_17', models.CharField(max_length=256, verbose_name='dock_17')),
                ('dock_18', models.CharField(max_length=256, verbose_name='dock_18')),
                ('dock_19', models.CharField(max_length=256, verbose_name='dock_19')),
                ('dock_20', models.CharField(max_length=256, verbose_name='dock_20')),
                ('dock_21', models.CharField(max_length=256, verbose_name='dock_21')),
                ('dock_22', models.CharField(max_length=256, verbose_name='dock_22')),
                ('dock_23', models.CharField(max_length=256, verbose_name='dock_23')),
                ('dock_24', models.CharField(max_length=256, verbose_name='dock_24')),
                ('dock_25', models.CharField(max_length=256, verbose_name='dock_25')),
                ('dock_26', models.CharField(max_length=256, verbose_name='dock_26')),
                ('dock_27', models.CharField(max_length=256, verbose_name='dock_27')),
                ('dock_28', models.CharField(max_length=256, verbose_name='dock_28')),
                ('dock_29', models.CharField(max_length=256, verbose_name='dock_29')),
                ('dock_30', models.CharField(max_length=256, verbose_name='dock_30')),
            ],
        ),
        migrations.CreateModel(
            name='PDBQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PDBSQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('sequence', models.CharField(max_length=500, verbose_name='Sequence')),
                ('hydrolitic_activity', models.FloatField(verbose_name='HydrolyticActivity')),
                ('mic_value', models.FloatField(verbose_name='MICValue')),
                ('solubility', models.CharField(max_length=256, verbose_name='Solubility')),
                ('tiny', models.IntegerField(verbose_name='Tiny')),
                ('small', models.IntegerField(verbose_name='Small')),
                ('aliphatic', models.IntegerField(verbose_name='Aliphatic')),
                ('aromatic', models.IntegerField(verbose_name='Aromatic')),
                ('non_polar', models.IntegerField(verbose_name='NonPolar')),
                ('polar', models.IntegerField(verbose_name='Polar')),
                ('charged_aa', models.IntegerField(verbose_name='ChargedAA')),
                ('basic', models.IntegerField(verbose_name='Basic')),
                ('acidic', models.FloatField(verbose_name='Acidic')),
                ('mol_weight_tiny', models.FloatField(verbose_name='MolWeightTiny')),
                ('mol_weight_small', models.FloatField(verbose_name='MolWeightSmall')),
                ('mol_weight_apliphatic', models.FloatField(verbose_name='MolWeightAliphatic')),
                ('mol_weight_aromatic', models.FloatField(verbose_name='MolWeightAromatic')),
                ('mol_weight_non_polar', models.FloatField(verbose_name='MolWeightNonPolar')),
                ('mol_weight_polar', models.FloatField(verbose_name='MolWeightPolar')),
                ('mol_weight_charged', models.FloatField(verbose_name='MolWeightCharged')),
                ('mol_weight_basic', models.FloatField(verbose_name='MolWeightBasic')),
                ('mol_weight_acidic', models.FloatField(verbose_name='MolWeightAcidic')),
                ('molecular_weight', models.FloatField(verbose_name='MolecularWeight')),
                ('length', models.IntegerField(verbose_name='Length')),
                ('charge', models.FloatField(verbose_name='Charge')),
                ('p_i', models.FloatField(verbose_name='pI')),
                ('a_index', models.FloatField(verbose_name='AIndex')),
                ('instaIndex', models.FloatField(verbose_name='InstaIndex')),
                ('BomanIndex', models.FloatField(verbose_name='BomanIndex')),
                ('hydrophobicity', models.FloatField(verbose_name='Hydrophobicity')),
                ('hmoment_angle', models.FloatField(verbose_name='HydrophobicMoment')),
                ('transmembrane', models.IntegerField(verbose_name='Transmembrane')),
                ('extracellular', models.BooleanField(verbose_name='Extracellular')),
                ('cytoplasmic', models.BooleanField(verbose_name='Cytoplasmic')),
                ('hydrophobic_plots', models.FloatField(verbose_name='HydrophobicPlots')),
                ('hydropathy_plots', models.FloatField(verbose_name='HydropathyPlots')),
                ('disulfide_end', models.CharField(max_length=256, verbose_name='disulphides')),
                ('toxicity', models.CharField(max_length=256, verbose_name='Toxicity')),
                ('rmsf', models.FloatField(verbose_name='RMSF')),
                ('flexibility', models.FloatField(verbose_name='Flexibility')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('pdb_name', models.CharField(max_length=256, verbose_name='PDBName')),
            ],
        ),
        migrations.CreateModel(
            name='Synthetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('synthetic_Sequence', models.CharField(max_length=500, verbose_name='Synthetic_sequence')),
                ('synthetic_Tiny', models.IntegerField(verbose_name='Tiny')),
                ('synthetic_Small', models.IntegerField(verbose_name='Small')),
                ('synthetic_Aliphtic', models.IntegerField(verbose_name='Synthetic_aliphatic')),
                ('synthetic_Aromatic', models.CharField(max_length=500, verbose_name='Synthetic_aromatic')),
                ('synthetic_non_polar', models.IntegerField(verbose_name='Synthetic_Non_Polar-aa')),
                ('synthetic_polar', models.IntegerField(verbose_name='Synthetic_Polar-aa')),
                ('synthetic_charged_aa', models.IntegerField(verbose_name='Synthetic_Charged-aa')),
                ('synthetic_basic', models.IntegerField(verbose_name='Synthetic_Basic-aa')),
                ('synthetic_acidic', models.CharField(max_length=255, verbose_name='Synthetic_Acidic-aa')),
                ('synthetic_mol_weight_tiny', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Tiny_aa')),
                ('synthetic_mol_weight_small', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Small_aa')),
                ('synthetic_mol_weight_apliphatic', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Aliphtic_aa')),
                ('synthetic_mol_weight_aromatic', models.CharField(max_length=255, verbose_name='Synthetic_Mole%-Aromatic_aa')),
                ('synthetic_mol_weight_non_polar', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Non_Polar_aa')),
                ('synthetic_mol_weight_polar', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Polar_aa')),
                ('synthetic_mol_weight_charged', models.FloatField(max_length=255, verbose_name='Synthetic_Mole%-Charged_aa')),
                ('synthetic_mol_weight_basic', models.FloatField(default=None, max_length=255, verbose_name='Synthetic_Mole%-Basic_aa')),
                ('synthetic_mol_weight_acidic', models.FloatField(default=None, max_length=255, verbose_name='Synthetic_Mole%-Acidic_aa')),
                ('synthetic_molecular_weight', models.FloatField(default=None, max_length=255, verbose_name='Synthetic_mw')),
                ('synthetic_length', models.IntegerField(default=None, verbose_name='Synthetic_length')),
                ('synthetic_charge', models.FloatField(default=None, max_length=255, verbose_name='Synthetic_Charge')),
                ('synthetic_isolelectric_point', models.FloatField(max_length=255, verbose_name='Synthetic_Isolelectric point')),
                ('synthetic_aliphatic_Index', models.FloatField(default=None, max_length=255, verbose_name='Synthetic_Aliphatic Index')),
                ('synthetic_instability_Index', models.FloatField(max_length=255, verbose_name='Synthetic_Instability Index')),
                ('synthetic_bomanIndex', models.FloatField(max_length=255, verbose_name='Synthetic_BomanIndex')),
                ('synthetic_hydrophobicity', models.FloatField(max_length=255, verbose_name='Synthetic_Hydrophobicity')),
                ('synthetic_hydrophobic_moment', models.FloatField(max_length=255, verbose_name='Synthetic_Hydrophobic moment')),
                ('synthetic_toxicity', models.CharField(default=None, max_length=255, verbose_name='Synthetic_Toxicity')),
                ('synthetic_hemolytic_activity', models.FloatField(max_length=255, verbose_name='Synthetic_Hemolytic activity')),
                ('synthetic_score', models.IntegerField(default=None, verbose_name='Synthetic_Score')),
                ('synthetic_pdb_name', models.CharField(default=None, max_length=255, verbose_name='Synthetic_PDBName')),
            ],
        ),
    ]

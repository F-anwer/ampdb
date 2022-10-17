# Generated by Django 4.0.2 on 2022-10-13 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDBQuery',
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
                ('disulfide_end', models.CharField(max_length=256, verbose_name='DisulfideEnd')),
                ('toxicity', models.CharField(max_length=256, verbose_name='Toxicity')),
                ('rmsf', models.FloatField(verbose_name='RMSF')),
                ('flexibility', models.FloatField(verbose_name='Flexibility')),
                ('pdb_name', models.CharField(max_length=256, verbose_name='PDBName')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('docked', models.CharField(max_length=256, verbose_name='Docked')),
            ],
        ),
        migrations.CreateModel(
            name='Dock_Proteins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dock_1', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_1')),
                ('dock_2', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_2')),
                ('dock_3', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_3')),
                ('dock_4', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_4')),
                ('dock_5', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_5')),
                ('dock_6', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_6')),
                ('dock_7', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_7')),
                ('dock_8', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_8')),
                ('dock_9', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_9')),
                ('dock_10', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_10')),
                ('dock_11', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_11')),
                ('dock_12', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_12')),
                ('dock_13', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_13')),
                ('dock_14', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_14')),
                ('dock_15', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_15')),
                ('dock_16', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_16')),
                ('dock_17', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_17')),
                ('dock_18', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_18')),
                ('dock_19', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_19')),
                ('dock_20', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_20')),
                ('dock_21', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_21')),
                ('dock_22', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_22')),
                ('dock_23', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_23')),
                ('dock_24', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_24')),
                ('dock_25', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_25')),
                ('dock_26', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_26')),
                ('dock_27', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_27')),
                ('dock_28', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_28')),
                ('dock_29', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_29')),
                ('dock_30', models.CharField(default='SOME STRING', max_length=256, verbose_name='dock_30')),
                ('pdb_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abampdb.proteins')),
            ],
        ),
    ]

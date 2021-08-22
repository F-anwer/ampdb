from django.core.management.base import BaseCommand
from ampdb.models import Proteins

import pandas as pd

class Command(BaseCommand):
    help = "Load the data file to as a database to ampdb."

    def add_arguments(self, parser):
        parser.add_argument('csv_dir', type=str, help='Path to csv data file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_dir']

        data = pd.read_csv(csv_file)
            try:
                for index, row in data.iterrows():
                    _, created = Proteins.objects.get_or_create(
                        name=row['Name'],
                        sequence=row['Sequence'],
                        hydrolitic_activity=row['HydrolyticActivity'],
                        mic_value=row['MICValue'],
                        solubility=row['Solubility'],
                        tiny=row['Tiny'],
                        small=row['Small'],
                        aliphatic=row['Aliphatic'],
                        aromatic=row['Aromatic'],
                        non_polar=row['NonPolar'],
                        polar=row['Polar'],
                        charged_aa=row['ChargedAA'],
                        basic=row['Basic'],
                        acidic=row['Acidic'],
                        mol_weight_timy=row['MolWeightTiny'],
                        mol_weight_small=row['MolWeightSmall'],
                        mol_weight_apliphatic=row['MolWeightAliphatic'],
                        mol_weight_aromatic=row['MolWeightAromatic'],
                        mol_weight_non_polar=row['MolWeightNonPolar'],
                        mol_weight_polar=row['MolWeightPolar'],
                        mol_weight_charged=row['MolWeightCharged'],
                        mol_weight_basic=row['MolWeightBasic'],
                        mol_weight_acidic=row['MolWeightAcidic'],
                        molecular_weight=row['MolecularWeight'],
                        length=row['Length'],
                        charge=row['Charge'],
                        p_i=row['pI'],
                        a_index=row['AIndex'],
                        instaIndex=row['InstaIndex'],
                        BomanIndex=row['BomanIndex'],
                        hydrophobicity=row['Hydrophobicity'],
                        hmoment_angle=row['HydrophobicMoment'],
                        transmembrane=row['Transmembrane'],
                        extracellular=row['Extracellular'],
                        cytoplasmic=row['Cytoplasmic'],
                        hydrophobic_plots=row['HydrophobicPlots'],
                        hydropathy_plots=row['HydropathyPlots'],
                        disulfide_end=row['DisulfideEnd'],
                        toxicity=row['Toxicity'],
                        rmsf=row['RMSF'],
                        flexibility=row['Flexibility'],
                        pdb_name=row['PDBName'],
                        links=row['Links']
                    )
            except Exception as e:
                print(e)
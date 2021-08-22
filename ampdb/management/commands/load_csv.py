from django.core.management.base import BaseCommand
from ampdb.models import Proteins
import pandas as pd

class Command(BaseCommand):
    help = "Load the data file to as a database to ampdb."

    def add_arguments(self, parser):
        parser.add_argument('csv_dir', type=str, help='Path to csv data file.')

    def handle(self, *args, csv_dir=None, **kwargs):
        pd.options.display.max_rows = 100
        df = pd.read_csv(csv_dir)
        col_map = {
            'Name': 'name',
            'Sequence': 'sequence',
            'Hemolytic activity (0-1)': 'hydrolitic_activity',  # ?
            'MIC value': 'mic_value',
            'Solubility': 'solubility',
            'Tiny-aa': 'tiny',
            'Small-aa': 'small',
            'Aliphtic-aa': 'aliphatic',
            'Aromatic-aa': 'aromatic',
            'Non_Polar-aa': 'non_polar',
            'Polar-aa': 'polar',
            'Charged-aa': 'charged_aa',
            'Basic-aa': 'basic',
            'Acidic-aa': 'acidic',
            'Mole%-Tiny_aa': 'mol_weight_tiny',
            'Mole%-Small_aa': 'mol_weight_small',
            'Mole%-Aliphtic_aa': 'mol_weight_apliphatic',
            'Mole%-Aromatic_aa': 'mol_weight_aromatic',
            'Mole%-Non_Polar_aa': 'mol_weight_non_polar',
            'Mole%-Polar_aa': 'mol_weight_polar',
            'Mole%-Charged_aa': 'mol_weight_charged',
            'Mole%-Basic_aa': 'mol_weight_basic',
            'Mole%-Acidic_aa': 'mol_weight_acidic',
            'mw <10KDa': 'molecular_weight',
            'length (12-50aa)': 'length',
            'charge': 'charge',
            'Isolelectric point': 'p_i',
            'aliphatic Index': 'a_index',
            'instability Index ': 'instaIndex',
            'BomanIndex ': 'BomanIndex',
            'hydrophobicity ': 'hydrophobicity',
            'hydrophobic moment': 'hmoment_angle',
            'Transmembrane': 'transmembrane',
            'Extracellular': 'extracellular',
            'Cytoplasmic': 'cytoplasmic',
            'HydrophobicityPlot': 'hydrophobic_plots',
            'HydrophobicityPlot2': 'hydropathy_plots',
            'Presence of disulphide bridges': 'disulfide_end',
            'Toxicity': 'toxicity',
            'RMSF': 'rmsf',
            'Flexibility ': 'flexibility',
            'PDBName': 'pdb_name',
            'Links': 'links',
        }
        for i, row in df.iterrows():
            # there are more rows than there are data, stop when we reach the lines without names
            if str(row['Name']) == 'nan':
                break
            protein = Proteins()
            for df_name, orm_name in col_map.items():
                value = row[df_name]
                # these bools are encoded in varying cases, eg. TRUE, True, etc.
                # the nans need to be checked in detail
                if df_name in {'Cytoplasmic', 'Extracellular'}:
                    boolmap = {
                        'true': True,
                        'false': False,
                        'nan': None,
                    }
                    try:
                        value = boolmap[str(value).strip().lower()]
                    except Exception:
                        print('found unparseable bool:', value)
                        raise
                # print(f'{df_name} -> {orm_name}: {value}')
                setattr(protein, orm_name, value)
            protein.save()

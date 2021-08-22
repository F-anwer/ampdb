from django.core.management.base import BaseCommand
from ampdb.models import Proteins
import csv


class Command(BaseCommand):
    help = "Load the data file to as a database to ampdb."

    def add_arguments(self, parser):
        parser.add_argument('csv_dir', type=str, help='Path to csv data file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_dir']

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            try:
                for row in reader:
                    _, created = Proteins.objects.get_or_create(
                        name=row[0],
                        sequence=row[1],
                        hydrolitic_activity=row[2],
                        mic_value=row[3],
                        solubility=row[4],
                        tiny=row[5],
                        small=row[6],
                        aliphatic=row[7],
                        aromatic=row[8],
                        non_polar=row[9],
                        polar=row[10],
                        charged_aa=row[11],
                        basic=row[12],
                        acidic=row[13],
                        mol_weight_timy=row[14],
                        mol_weight_small=row[15],
                        mol_weight_apliphatic=row[16],
                        mol_weight_aromatic=row[17],
                        mol_weight_non_polar=row[18],
                        mol_weight_polar=row[19],
                        mol_weight_charged=row[20],
                        mol_weight_basic=row[21],
                        mol_weight_acidic=row[22],
                        molecular_weight=row[23],
                        length=row[24],
                        charge=row[25],
                        p_i=row[26],
                        a_index=row[27],
                        instaIndex=row[28],
                        BomanIndex=row[29],
                        hydrophobicity=row[30],
                        hmoment_angle=row[31],
                        transmembrane=row[32],
                        extracellular=row[33],
                        cytoplasmic=row[34],
                        hydrophobic_plots=row[35],
                        hydropathy_plots=row[36],
                        disulfide_end=row[37],
                        toxicity=row[38],
                        rmsf=row[39],
                        flexibility=row[40],
                        pdb_name=row[41],
                        links=row[42]
                    )
            except Exception as e:
                print(e)
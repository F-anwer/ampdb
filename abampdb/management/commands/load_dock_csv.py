import pandas as pd
from django.core.management.base import BaseCommand
from abampdb.models import Docks


class Command(BaseCommand):
    help = "Load the data file to as a database to abampdb."

    def add_arguments(self, parser):
        parser.add_argument("csv_dir", type=str, help="Path to csv data file.")

    def handle(self, *args, csv_dir=None, **kwargs):
        df = pd.read_csv(csv_dir, encoding='latin-1')
        col_map = {
            "Dock": "dock_1",
            "Image": "image",
            "Attractive_VdW": "attr_vdw",
            "Global_Energy": "global_energy",
            "Repulsive_VdW": "repl_vdw",
            "ACE": "binding_energy",
            "HB": "hydrogen_bonding",
        }
        for i, row in df.iterrows():
            # there are more rows than there are data, stop when we reach the lines without names
            if str(row["Dock"]) == "nan":
                break
            docks = Docks()
            for df_name, orm_name in col_map.items():
                value = row[df_name]
                # these bools are encoded in varying cases, eg. TRUE, True, etc.
                # the nans need to be checked in detail
                setattr(docks, orm_name, value)
            docks.save()

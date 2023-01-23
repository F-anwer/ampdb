import pandas as pd
from django.core.management.base import BaseCommand

from abampdb.models import Dock_Proteins


class Command(BaseCommand):
    help = "Load the data file to as a database to abampdb."

    def add_arguments(self, parser):
        parser.add_argument("csv_dir", type=str, help="Path to csv data file.")

    def handle(self, *args, csv_dir=None, **kwargs):
        df = pd.read_csv(csv_dir)
        col_map = {
            "Name": "name",
            "Dock_1": "dock_1",
            "Dock_2": "dock_2",
            "Dock_3": "dock_3",
            "Dock_4": "dock_4",
            "Dock_5": "dock_5",
            "Dock_6": "dock_6",   
            "Dock_7": "dock_7",           
            "Dock_8": "dock_8",           
            "Dock_9": "dock_9",           
            "Dock_10": "dock_10",           
            "Dock_11": "dock_11",           
            "Dock_12": "dock_12",           
            "Dock_13": "dock_13",           
            "Dock_14": "dock_14",           
            "Dock_15": "dock_15",           
            "Dock_16": "dock_16",        
            "Dock_17": "dock_17",        
            "Dock_18": "dock_18",        
            "Dock_19": "dock_19",     
            "Dock_20": "dock_20", 
            "Dock_21": "dock_21",
            "Dock_22": "dock_22",
            "Dock_23": "dock_23",
            "Dock_24": "dock_24",
            "Dock_25": "dock_25",
            "Dock_26": "dock_26",
            "Dock_27": "dock_27",
            "Dock_28": "dock_28",
            "Dock_29": "dock_29",
            "Dock_30": "dock_30",
        }
        for i, row in df.iterrows():
            # there are more rows than there are data, stop when we reach the lines without names
            if str(row["dock_1"]) == "nan":
                break
            dock_protein = Dock_Proteins()
            for df_name, orm_name in col_map.items():
                value = row[df_name]
                # these bools are encoded in varying cases, eg. TRUE, True, etc.
                # the nans need to be checked in detail
                setattr(dock_protein, orm_name, value)
            dock_protein.save()

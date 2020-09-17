import logging
import os

import pandas as pd
from django.core.management.base import BaseCommand

from coordinates.models import Coordinate


class Command(BaseCommand):
    help = 'Insert the absolute path for load the coordinates csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str, default=["jadjhkdsajhdashjkasd"])

    def handle(self, *args, **options):
        for file_path in options['file_path']:
            if os.path.exists(file_path):
                for row in pd.read_csv(file_path, sep=';').iterrows():
                    c = Coordinate(id=row[1].at["id"], x_axes=row[1].at["x"], y_axes=row[1].at["y"])
                    c.save()
                self.stdout.write('File successfully loaded')
            else:
                self.stdout.write(f'File does not exists, please check the file_path: {file_path}')

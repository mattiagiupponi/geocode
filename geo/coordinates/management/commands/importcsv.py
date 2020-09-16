from django.core.management.base import BaseCommand, CommandError
from coordinates.models import Coordinate
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Insert the absolute path for load the coordinates csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for file_path in options['file_path']:
            if os.path.isfile(file_path):
                for row in pd.read_csv(file_path, sep=';').iterrows():
                    c = Coordinate(id=row[1].at["id"], x_axes=row[1].at["x"], y_axes=row[1].at["y"])
                    c.save()
                self.stdout.write(self.style.SUCCESS('File successfully loaded'))
            else:
                self.stdout.write(self.style.ERROR(f'File does not exists, please check the file_path: {file_path}'))

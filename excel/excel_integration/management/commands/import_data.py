import os
import pandas as pd
from django.core.management.base import BaseCommand
from excel_integration.models import Contact
from mapbox import Geocoder
from django.conf import settings

class Command(BaseCommand):
    help = 'Import data from Excel'

    def handle(self, *args, **options):
        file_path = '/Users/jakobstinnes/Desktop/Basic.xlsx'
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File does not exist: {file_path}"))
            return

        data_frame = pd.read_excel(file_path)

        geocoder = Geocoder(access_token=settings.MAPBOX_ACCESS_TOKEN)

        for _, row in data_frame.iterrows():
            contact = Contact(
                termin=row['Termin'],
                vorname=row['Vorname'],
                name=row['Name'],
                straße=row['Straße'],
                hausnummer=row['Hausnummer'],
                plz=row['PLZ'],
                stadt=row['Stadt'],
                telefon_primär=row['Telefon (Primär)'],
                telefon_sekundär=row['Telefon (Sekundär)'],
                email=row['Email'],
                objekt=row['Objekt'],
                anlage=row['Anlage'],
                dach=row['Dach'],
                infos=row['Infos'],
                speicher=row['Speicher'],
                interesse=row['Interesse'],
                jährlicher_stromverbrauch=row['Jährlicher Stromverbrauch'],
                anfrage_über=row['Anfrage über'],
                kunden_id=row['Kunden ID'],
            )
            contact.save()

            address = f'{contact.straße} {contact.hausnummer}, {contact.plz} {contact.stadt}'
            response = geocoder.forward(address)
            if len(response.json()['features']) > 0:
                coordinates = response.json()['features'][0]['geometry']['coordinates']
                contact.latitude = coordinates[1]
                contact.longitude = coordinates[0]
                contact.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

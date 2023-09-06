import json
from django.conf import settings
from django.core.management.base import BaseCommand
from companies.models import Companies  
from companies.models import Companies, Language 


class Command(BaseCommand):
    help = 'Populate the database with dummy company data'

    def handle(self, *args, **options):
        json_file_path = settings.BASE_DIR / 'static' / 'test_companies.json'

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            for company_data in data:
                company = Companies(
                    title=company_data['fields']['title'],
                    about=company_data['fields']['about'],
                    pretest=company_data['fields']['pretest'],
                    posttest=company_data['fields']['posttest'],
                    is_id_required=company_data['fields']['is_id_required']
                )
                company.save()

                # Extract language names from the JSON data
                language_names = company_data['fields']['languages']

                # Assuming 'languages' is a ManyToManyField, add languages to the company
                for language_name in language_names:
                    language, created = Language.objects.get_or_create(name=language_name)
                    company.languages.add(language)

                self.stdout.write(self.style.SUCCESS(f'Successfully added company "{company.title}"'))

        self.stdout.write(self.style.SUCCESS('Database population completed'))

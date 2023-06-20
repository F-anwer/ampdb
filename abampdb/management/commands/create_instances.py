from django.core.management.base import BaseCommand
from abampdb.models import Targetproteins, Docks


class Command(BaseCommand):
    help = 'Creates instances for Docks model'

    def handle(self, *args, **options):
        fake = Faker()  # Optional: If you want to generate random data
        
        # Create instances of Targetproteins
        target1 = Targetproteins.objects.create(name='Target1')  # Replace 'name' with your actual field name
        target2 = Targetproteins.objects.create(name='Target2')

        # Create instances of Docks
        for i in range(10):
            dock = Docks.objects.create(
                dock_1=fake.name(),  # Replace 'dock_1' with your actual field name or provide your own values
                image=fake.image_url(),  # Replace 'image' with your actual field name or provide your own values
                global_energy=fake.random_number(),  # Replace 'global_energy' with your actual field name or provide your own values
                attr_vdw=fake.random_number(),  # Replace 'attr_vdw' with your actual field name or provide your own values
                repl_vdw=fake.random_number(),  # Replace 'repl_vdw' with your actual field name or provide your own values
                binding_energy=fake.random_number(),  # Replace 'binding_energy' with your actual field name or provide your own values
                hydrogen_bonding=fake.random_number()  # Replace 'hydrogen_bonding' with your actual field name or provide your own values
            )
            dock.targets.add(target1, target2)  # Add the Targetproteins instances to the ManyToMany field of Docks



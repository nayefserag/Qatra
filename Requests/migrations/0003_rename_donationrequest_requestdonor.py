# Generated by Django 4.2 on 2023-04-20 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0002_donationrequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonationRequest',
            new_name='RequestDonor',
        ),
    ]

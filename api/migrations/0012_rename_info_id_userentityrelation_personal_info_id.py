# Generated by Django 4.2.6 on 2024-02-07 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_infogroup_core_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userentityrelation',
            old_name='info_id',
            new_name='personal_info_id',
        ),
    ]

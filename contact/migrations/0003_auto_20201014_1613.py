# Generated by Django 3.0.8 on 2020-10-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Employed'), (2, 'Unemployed'), (3, 'self-employed')], null=True),
        ),
    ]

# Generated by Django 3.2.25 on 2024-05-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0012_alter_hrapplicant_stage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrapplicant',
            name='stage_id',
            field=models.IntegerField(blank=True, default='3', null=True),
        ),
    ]
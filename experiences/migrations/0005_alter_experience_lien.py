# Generated by Django 4.0.6 on 2022-08-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_remove_experience_picture_experience_lien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='lien',
            field=models.CharField(blank=True, max_length=2500),
        ),
    ]

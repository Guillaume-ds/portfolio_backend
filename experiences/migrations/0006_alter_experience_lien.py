# Generated by Django 4.0.6 on 2022-08-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_alter_experience_lien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='lien',
            field=models.CharField(blank=True, default='', max_length=2500, null=True),
        ),
    ]

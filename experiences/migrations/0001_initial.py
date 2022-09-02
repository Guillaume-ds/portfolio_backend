# Generated by Django 4.0.6 on 2022-08-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('date_deb', models.DateField()),
                ('date_fin', models.DateField(null=True)),
                ('description1', models.TextField()),
                ('description2', models.TextField(null=True)),
                ('description3', models.TextField(null=True)),
            ],
        ),
    ]

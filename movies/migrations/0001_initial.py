# Generated by Django 4.0.1 on 2022-01-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('release_date', models.DateField()),
                ('running_time', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]

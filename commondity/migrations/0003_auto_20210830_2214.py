# Generated by Django 2.0.1 on 2021-08-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondity', '0002_auto_20210830_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

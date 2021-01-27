# Generated by Django 3.1.2 on 2021-01-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='link',
            field=models.CharField(default='-', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paper',
            name='id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paper',
            name='name',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]

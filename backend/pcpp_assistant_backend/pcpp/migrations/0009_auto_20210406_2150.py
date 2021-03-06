# Generated by Django 3.1.7 on 2021-04-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcpp', '0008_auto_20210406_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='coreFamily',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='manufacturer',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='microarchitecture',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='socket',
            field=models.CharField(max_length=64, null=True),
        ),
    ]

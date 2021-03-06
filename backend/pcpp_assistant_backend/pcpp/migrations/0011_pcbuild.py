# Generated by Django 3.1.7 on 2021-04-19 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pcpp', '0010_auto_20210406_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='PCBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.case')),
                ('cpuLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.cpu')),
                ('gpuLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.gpu')),
                ('mboardLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.motherboard')),
                ('memoryLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.memory')),
                ('powerLink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pcpp.power')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

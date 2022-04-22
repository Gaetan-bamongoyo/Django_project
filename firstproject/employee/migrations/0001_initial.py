# Generated by Django 4.0.1 on 2022-04-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('posteId', models.AutoField(primary_key=True, serialize=False)),
                ('posteDesignation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeId', models.AutoField(primary_key=True, serialize=False)),
                ('employeNom', models.CharField(max_length=100)),
                ('employePostnom', models.CharField(max_length=100)),
                ('employeSexe', models.CharField(max_length=100)),
                ('employeAdress', models.TextField()),
                ('poste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.poste')),
            ],
        ),
    ]

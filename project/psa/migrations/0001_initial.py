# Generated by Django 3.2 on 2021-04-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kallelse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=100)),
                ('name', models.CharField(default='Okänd', max_length=150)),
                ('datum', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('ssn', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('namn', models.CharField(default='Okänd', max_length=150)),
                ('gata', models.CharField(default='Okänd', max_length=150)),
                ('postort', models.CharField(default='Okänd', max_length=150)),
                ('postnr', models.CharField(default='Okänd', max_length=150)),
                ('mail', models.CharField(default='Okänd', max_length=150)),
                ('opdate', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provsvar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('ssn', models.CharField(max_length=100)),
                ('result', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
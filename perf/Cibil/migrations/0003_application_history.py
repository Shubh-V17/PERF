# Generated by Django 2.1.2 on 2020-04-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cibil', '0002_credit_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_History',
            fields=[
                ('Application_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Application_Date', models.DateField()),
                ('Application_Type', models.CharField(default='Credit Card', max_length=30)),
                ('Status', models.CharField(max_length=30)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cibil.Personal_Information')),
            ],
        ),
    ]
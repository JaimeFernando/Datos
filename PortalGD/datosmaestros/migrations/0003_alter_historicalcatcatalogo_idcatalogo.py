# Generated by Django 4.1.7 on 2023-03-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosmaestros', '0002_alter_historicalcatcatalogo_idcategoriacatalogo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalcatcatalogo',
            name='idcatalogo',
            field=models.IntegerField(auto_created=True, db_column='idCatalogo', db_index=True),
        ),
    ]
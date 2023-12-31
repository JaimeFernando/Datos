# Generated by Django 4.1.7 on 2023-03-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosmaestros', '0007_alter_catcatalogo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalcatcatalogo',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcatcatalogo',
            name='deleted_by',
            field=models.IntegerField(db_column='deleted_by', null=True),
        ),
        migrations.AlterField(
            model_name='historicalcatcatalogo',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcatcatalogo',
            name='updated_by',
            field=models.IntegerField(db_column='updated_by', null=True),
        ),
    ]

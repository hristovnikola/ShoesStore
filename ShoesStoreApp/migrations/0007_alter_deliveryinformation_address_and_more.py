# Generated by Django 4.2.2 on 2023-07-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoesStoreApp', '0006_alter_deliveryinformation_name_on_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinformation',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinformation',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinformation',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinformation',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinformation',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinformation',
            name='surname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

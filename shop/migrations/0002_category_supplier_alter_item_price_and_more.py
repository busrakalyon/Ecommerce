# Generated by Django 5.1.4 on 2024-12-16 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('parent_id', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SellerID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('CompanyName', models.CharField(max_length=255)),
                ('AddressID', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='ProductImage_path',
            field=models.CharField(default='default_image.jpg', max_length=255),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('ReviewID', models.IntegerField(primary_key=True, serialize=False)),
                ('CustomerID', models.IntegerField(blank=True, db_column='CustomerID', null=True)),
                ('ItemID', models.IntegerField()),
                ('SellerID', models.IntegerField()),
                ('Ratings', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Review', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now=True)),
                ('auth_user', models.ForeignKey(blank=True, db_column='auth_user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
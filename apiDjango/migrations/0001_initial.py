# Generated by Django 4.2.1 on 2024-05-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('priceWithOutTaxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('createdAtArticle', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('listArticles', models.JSONField()),
                ('priceTotalWithOutTaxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('priceTotalWithTaxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('createdAtOrders', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

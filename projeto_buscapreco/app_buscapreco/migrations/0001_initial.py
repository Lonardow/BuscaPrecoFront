# Generated by Django 4.1.7 on 2023-03-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("id_produto", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField(max_length=255)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=12)),
                ("site", models.TextField(max_length=255)),
                ("data_cotacao", models.DateField()),
                (
                    "link_imagem",
                    models.TextField(
                        default="https://via.placeholder.com/150", max_length=500
                    ),
                ),
            ],
        ),
    ]

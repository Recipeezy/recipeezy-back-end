# Generated by Django 3.2 on 2021-04-20 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_ingredient_pantry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pantry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pantry'),
        ),
    ]
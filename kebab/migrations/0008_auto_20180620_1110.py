# Generated by Django 2.0.6 on 2018-06-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebab', '0007_auto_20180620_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='kebaby_dania',
            name='batter_type',
            field=models.CharField(choices=[('Tortilla', 'Tortilla'), ('Pita', 'Pita'), ('Bułka', 'Bułka')], default='Tortilla', max_length=20),
        ),
        migrations.AddField(
            model_name='kebaby_dania',
            name='meat_type',
            field=models.CharField(choices=[('Baranina', 'Baranina'), ('Baranina-Kurczak', 'Baranina-Kurczak'), ('Kurczak', 'Kurczak'), ('Wołowina', 'Wołowina'), ('Wegetariański', 'Wegetariański')], default='Baranina', max_length=20),
        ),
        migrations.AddField(
            model_name='kebaby_dania',
            name='sauce_type',
            field=models.CharField(choices=[('Ostry', 'Ostry'), ('Mieszany', 'Mieszany'), ('Lagodny', 'Lagodny'), ('Czosnkowy', 'Czosnkowy'), ('Bez sosu', 'Bez sosu')], default='Lagodny', max_length=20),
        ),
        migrations.AlterField(
            model_name='kebaby_dania',
            name='batter',
            field=models.IntegerField(choices=[(0, '1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='kebaby_dania',
            name='meat',
            field=models.IntegerField(choices=[(0, '1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='kebaby_dania',
            name='salds',
            field=models.IntegerField(choices=[(0, '1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='kebaby_dania',
            name='sauce',
            field=models.IntegerField(choices=[(0, '1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]

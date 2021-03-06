# Generated by Django 3.1.5 on 2021-01-06 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20210105_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='data',
        ),
        migrations.AddField(
            model_name='eventos',
            name='envio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tracker.envio'),
            preserve_default=False,
        ),
    ]

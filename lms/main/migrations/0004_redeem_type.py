# Generated by Django 3.2 on 2021-05-20 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210520_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='redeem',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.redeem_type'),
            preserve_default=False,
        ),
    ]
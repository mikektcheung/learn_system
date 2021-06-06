# Generated by Django 3.2 on 2021-05-16 01:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learn_eng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eng_question',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'K1'), (2, 'K2'), (3, 'K3'), (11, 'P1'), (12, 'P2'), (13, 'P3')], default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eng_quiz',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eng_question',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learn_eng.eng_quiz'),
        ),
        migrations.AlterField(
            model_name='eng_question',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learn_eng.eng_quiz_topic'),
        ),
        migrations.AlterField(
            model_name='eng_quiz',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'K1'), (2, 'K2'), (3, 'K3'), (11, 'P1'), (12, 'P2'), (13, 'P3')]),
        ),
    ]
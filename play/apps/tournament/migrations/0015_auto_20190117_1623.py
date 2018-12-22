# Generated by Django 2.0.3 on 2019-01-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0002_auto_20181213_0150'),
        ('tournament', '0014_auto_20181226_1753'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='snaketournamentbracket',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='snaketournamentbracket',
            name='snake',
        ),
        migrations.RemoveField(
            model_name='snaketournamentbracket',
            name='tournament_bracket',
        ),
        migrations.AddField(
            model_name='tournamentbracket',
            name='snakes',
            field=models.ManyToManyField(through='tournament.TournamentSnake', to='snake.Snake'),
        ),
        migrations.AlterField(
            model_name='snakeheat',
            name='snake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.TournamentBracket'),
        ),
        migrations.AlterField(
            model_name='tournamentsnake',
            name='bracket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.TournamentBracket'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentsnake',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='SnakeTournamentBracket',
        ),
    ]

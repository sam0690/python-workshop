# Generated by Django 5.2.2 on 2025-06-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_genre_alter_movie_release_date_alter_movie_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='release_year',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='poster_url',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.URLField(blank=True, help_text='URL of the movie cover image', null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Spanish', 'Spanish'), ('French', 'French'), ('German', 'German'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Other', 'Other')], default='English', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(blank=True, help_text='URL of the movie trailer', null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='video_url',
            field=models.URLField(blank=True, help_text='URL of the movie video', null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
    ]

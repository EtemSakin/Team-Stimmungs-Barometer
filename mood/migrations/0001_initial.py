from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="MoodEntry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("day", models.DateField(db_index=True)),
                ("score", models.PositiveSmallIntegerField(validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ])),
                ("daily_voter_hash", models.CharField(max_length=64)),
            ],
            options={"ordering": ["-day"]},
        ),
        migrations.AddConstraint(
            model_name="moodentry",
            constraint=models.UniqueConstraint(
                fields=("day", "daily_voter_hash"),
                name="one_vote_per_day_and_browser",
            ),
        ),
    ]

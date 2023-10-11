# Generated by Django 4.2.6 on 2023-10-11 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0002_teacher_remove_student_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="main_teacher",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="bookings.teacher",
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-07 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0003_auto_20211206_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='lectures',
            field=models.ManyToManyField(through='dbapp.LecturesAssignement', to='dbapp.Lectures'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(through='dbapp.CoursesTeacher', to='dbapp.Courses'),
        ),
        migrations.AlterField(
            model_name='coursesteacher',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.courses'),
        ),
        migrations.AlterField(
            model_name='coursesteacher',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.teacher'),
        ),
        migrations.AlterField(
            model_name='exams',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.courses'),
        ),
        migrations.AlterField(
            model_name='lectures',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.courses'),
        ),
        migrations.AlterField(
            model_name='lectures',
            name='recording',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.recordings'),
        ),
        migrations.AlterField(
            model_name='lecturesassignement',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.assignment'),
        ),
        migrations.AlterField(
            model_name='lecturesassignement',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.lectures'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.courses'),
        ),
        migrations.AlterField(
            model_name='recordings',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.lectures'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.exams'),
        ),
    ]
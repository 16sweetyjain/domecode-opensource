# Generated by Django 3.1 on 2020-08-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0013_answer_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='typeof',
            field=models.CharField(choices=[('JAVA', 'Java'), ('PYTHON', 'Python'), ('RUST', 'Rust'), ('C++', 'C++')], default='PYTHON', max_length=10),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_fish1_user_alter_fish1_user2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fish1",
            old_name="user2",
            new_name="fishermen",
        ),
        migrations.RenameField(
            model_name="fish1",
            old_name="user",
            new_name="retailers",
        ),
    ]

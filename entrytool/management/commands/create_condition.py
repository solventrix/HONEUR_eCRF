"""
Creates a new condition for the entry tool in plugins/conditions

it scaffolds out the models.py and plugin.py and creates the
static/js directory
"""

from django.core.management.base import BaseCommand
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os
import shutil

SCAFFOLD_DIRECTORY = os.path.join("entrytool", "scaffold")
CONDITIONS_DIRECTORY = os.path.join("plugins", "conditions")


def write_python_file(
    file_type, target_directory, condition_name, cleaned_condition_name
):
    """
    Writes a python file from scaffold/{{ file_type }}.jinja2
    to {{ condition_directory }}/{{ file_type }}
    """
    jinja_env = Environment(loader=FileSystemLoader(SCAFFOLD_DIRECTORY))
    template = jinja_env.get_template(f"{file_type}.jinja2")
    output = template.render(
        name=condition_name, cleaned_condition_name=cleaned_condition_name
    )
    Path(target_directory, file_type).write_text(output)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("condition_name", help="Specify the condition name")

    def handle(self, *args, **options):
        condition_name = options["condition_name"]
        cleaned_condition_name = (
            condition_name.replace(" ", "_").replace("-", "_").lower()
        )
        target_directory = Path(CONDITIONS_DIRECTORY, cleaned_condition_name)
        if target_directory.exists():
            raise ValueError(
                f"{target_directory} already exists, remove it to continue"
            )
        target_directory.mkdir()
        Path(target_directory, "__init__.py").touch()
        write_python_file(
            "models.py", target_directory, condition_name, cleaned_condition_name
        )
        write_python_file(
            "plugin.py", target_directory, condition_name, cleaned_condition_name
        )
        write_python_file(
            "episode_categories.py",
            target_directory,
            condition_name,
            cleaned_condition_name,
        )
        # create static/js/{{ condition_name }}
        Path(target_directory, "static", "js", cleaned_condition_name).mkdir(
            parents=True
        )

        # create the detail templates directory
        templates_dir = Path(target_directory, "templates", "detail")
        templates_dir.mkdir(parents=True)

        # create the condition's episode detail template
        shutil.copy(
            os.path.join(SCAFFOLD_DIRECTORY, "episode_detail.html"),
            os.path.join(templates_dir, f"{ cleaned_condition_name }.html")
        )

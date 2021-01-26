from unittest import TestCase
from entrytool.management.commands.createopalschema import Command


class TestCommand(TestCase):

    def test_handle(self):
        create_opal_schema = Command()
        create_opal_schema.handle()

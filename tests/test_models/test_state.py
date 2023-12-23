#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_create_state(self):
        """Test if create State command adds a new record in the table states"""
        initial_count = len(self.value.all())  # Get the initial count of records
        new_state = self.value(name="California")  # Execute the create State command
        final_count = len(self.value.all())  # Get the final count of records
        self.assertEqual(final_count, initial_count + 1)  # Check if the difference is +1
        

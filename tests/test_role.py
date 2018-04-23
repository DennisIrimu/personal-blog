import unittest
from app.models import Role

class TestRole(unittest.TestCase):
    '''
    Test class for roles
    '''

    def setUp(self):
        self.new_role = Role(name="dnyt")

    def test_instance(self):
        self.assertTrue( isinstance(self.new_role, Role) )

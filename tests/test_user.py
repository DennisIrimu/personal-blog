import unittest
from app.models import User,Role

class TestUser(unittest.TestCase):
    '''
    Test class for the User
    '''

    def setUp(self):
        self.user_role = Role(name="Driver")
        self.new_user = User(password='sixty-nine', role=self.user_role)

    def test_instance(self):
        self.assertTrue( isinstance(self.new_user, User) )

        

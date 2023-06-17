import os
import unittest

from tgbot.services.interact_database import DbInteraction, db_interaction


class DbInteractionTest(unittest.TestCase):
    """Test cases for database interaction class."""

    def setUp(self):
        """Setup temporary database."""
        self.db = DbInteraction(":memory:")
        self.db.create_user_table()
        self.db.add_user_to_db(1, "test", "111")

    def test_check_user_in_db_success(self):
        """Check user in db is true."""
        user_id = 1
        self.assertTrue(self.db.check_user_in_db(user_id))

    def test_test_check_user_in_db_failure(self):
        """Check user in db is false."""
        user_id = 2
        self.assertFalse(self.db.check_user_in_db(user_id))

    def test_get_username(self):
        """Check getting username in db."""
        user_id = 1
        username = self.db.get_username(user_id)
        self.assertEqual(username, "test")

    def tearDown(self) -> None:
        db_interaction.connection.close()
        try:
            os.remove("lifecell_db.db")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()

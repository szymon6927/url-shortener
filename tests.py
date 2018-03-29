import unittest
import os

from flask_testing import TestCase

from app import create_app, db
from app.models import Users, Links


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI_TEST']
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()

        # create test admin user
        admin = Users(username="admin", password="admin2018", is_admin=True)

        # create test non admin user
        user = Users(username="user2018", password="user2018")

        db.session.add(admin)
        db.session.add(user)

        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_users_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Users.query.count(), 2)

    def test_links_model(self):
        """
        Test number of records in links table
        """
        link = Links(phone="755432132", redirect_url="http://materializecss.com/preloader.html")

        # save department to database
        db.session.add(link)
        db.session.commit()

        self.assertEqual(Links.query.count(), 1)


if __name__ == '__main__':
    unittest.main()

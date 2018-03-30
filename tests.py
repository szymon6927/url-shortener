import unittest
import os

from flask import url_for
from flask_testing import TestCase

from app import create_app, db
from app.models import Users, Links, Openned

from app.utils import random_string_generator, url_checker


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

    def test_open_model(self):
        """
        Test numer of records in openned table
        """
        open_link = Openned(ga_client_id="1448460056.1521880602", ip="127.0.0.1", client_phone="666555444")

        db.session.add(open_link)
        db.session.commit()
        self.assertEqual(Openned.query.count(), 1)


class TestViews(TestBase):

    def test_opened_view(self):
        """
        Test that cutomers page is inaccessible without login
        and redirects to login page then to departments page
        """
        target_url = url_for('opened.show_opened')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_login_view(self):
        """
        Test that login page is accessible wihout login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


class TestUtils(TestBase):

    def test_random_string_generator(self):
        """
        Test that function return good string length
        """
        test_string = random_string_generator(5)
        self.assertEqual(5, len(test_string))


if __name__ == '__main__':
    unittest.main()

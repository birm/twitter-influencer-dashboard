# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_influencetags(self):
        """
        Test case for influencetags

        Determine hashtag similarity between users
        """
        response = self.client.open('/influence/hashtags/{handle}/{influencer}'.format(handle='handle_example', influencer='influencer_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_influencetags_0(self):
        """
        Test case for influencetags_0

        Determine mention similarity between users
        """
        response = self.client.open('/influence/mention/{handle}/{influencer}'.format(handle='handle_example', influencer='influencer_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_influencetime(self):
        """
        Test case for influencetime

        determines how close users tweet to each other
        """
        response = self.client.open('/influence/deltat/{handle}/{influencer}'.format(handle='handle_example', influencer='influencer_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_influencetopic(self):
        """
        Test case for influencetopic

        Determine topic similarity between users
        """
        response = self.client.open('/influence/topics/{handle}/{influencer}'.format(handle='handle_example', influencer='influencer_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usermentions(self):
        """
        Test case for usermentions

        Get users which a user has mentioned
        """
        response = self.client.open('/user/mentions/{handle}'.format(handle='handle_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_useroverview(self):
        """
        Test case for useroverview

        Get basic information about a user
        """
        response = self.client.open('/user/overview/{handle}'.format(handle='handle_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usertags(self):
        """
        Test case for usertags

        Get most common recent hashtags used by a user
        """
        response = self.client.open('/user/hashtags/{handle}'.format(handle='handle_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usertimes(self):
        """
        Test case for usertimes

        Gets a picture of when a user tweets
        """
        response = self.client.open('/user/time/{handle}'.format(handle='handle_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_usertopics(self):
        """
        Test case for usertopics

        Gets topics a user uses, grouped using word2vec
        """
        response = self.client.open('/user/topics/{handle}'.format(handle='handle_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

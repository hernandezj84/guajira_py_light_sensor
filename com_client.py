"""Communicates with http rest api"""

import os
import requests

class ComClient:
    """Provides http rest api communications methods
    """
    def __init__(self):
        """Object ComClient constructor"""
        self.base_url = os.getenv("BASE_URL", "http://localhost:5000")

    def test(self):
        """Returns json string with the results of test request

        Returns:
            str: the result of the testing method to backend
        """
        request = requests.get(self.base_url + '/test')
        return request.json()
    
    def post_change(self, device, information):
        """Post change to information to backend

        Args:
            device (str): name of device posting
            information (str): the information that will be posted

        Returns:
            str: returns json string with the backend response
        """
        request = requests.post(self.base_url + '/post_lecture/', json={"device": device, "information": information})
        return request.json()


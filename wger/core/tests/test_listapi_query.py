# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import json


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from wger.core.tests.base_testcase import WorkoutManagerTestCase
from wger.core.models import UserProfile


class ListApiTestCaseRest(WorkoutManagerTestCase):
    '''
    Class to test if we can query all users created under a profile
    '''
    def test_list_api_users(self):
        '''
        Test api-users endpoint.
        '''
        url = '/api/v2/register/'
        url2 = '/api/v2/api-users/'

        # Test for the unauthorized user
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        registration_data = {'username': 'test1',
                             'password1': 'test_pass',
                             'password2': 'test_pass',
                             'email': 'my.email1@example.com',
                             'g-recaptcha-response': 'PASSED', }
        self.client.post(
            reverse('core:user:registration'), registration_data)

        user = User.objects.get(username="test1")
        user_profile = UserProfile.objects.get(user=user)
        user_profile.can_add_user = True
        user_profile.save()

        reg_data = dict(username='test_user',
                        password='test_password', email='test@mail.com')

        # Test register via Rest API
        self.new_user_login()  # this user's flag can_add_user is set to True
        response = self.client.post(url, data=reg_data)

        response = self.client.get(url2)
        reply = json.loads(response.content.decode('utf-8'))
        self.assertEqual(reply['count'], 1, msg="No profiles found")

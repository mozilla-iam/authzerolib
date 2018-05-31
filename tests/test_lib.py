#!/usr/bin/env python

import json
import unittest
import os
import time

from unittest.mock import patch
from authzero import AuthZero


class AuthZeroLibTest(unittest.TestCase):
    def setUp(self):
        pass

    @patch.object(AuthZero, "_request")
    def test_get_rules(self, mock_request):
        fix_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/get_rules.json')
        with open(fix_path) as fd:
            fix = json.load(fd)

        mock_request.return_value = fix
        config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
        az = AuthZero(config)

        ret = az.get_rules()
        assert(isinstance(ret, list))
        assert(len(ret)) == 2
        assert(isinstance(ret[0], dict))
        assert(ret[0].get('id') is not None)
        assert(ret[0].get('script') is not None)
        assert(ret[0].get('enabled') is True)

    def test_get_bad_access_token(self):
        config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
        az = AuthZero(config)
        az.access_token = {}
        with self.assertRaises(Exception) as context:
            az._authorize(az.default_headers)
        assert('InvalidAccessToken' == str(context.exception))

    @patch.object(AuthZero, "get_access_token")
    def test_get_good_access_token(self, mock_get_access_token):
        fix_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/access_token.json')
        with open(fix_path) as fd:
            fix = json.load(fd)

        mock_get_access_token.return_value = fix
        config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
        az = AuthZero(config)
        az.access_token = az.get_access_token()
        az.access_token_valid_until = time.time() + az.access_token.get('expires_in')
        az._authorize(az.default_headers)

    @patch.object(AuthZero, "get_access_token")
    def test_get_auto_renew_access_token(self, mock_get_access_token):
        fix_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/access_token.json')
        with open(fix_path) as fd:
            fix = json.load(fd)

        mock_get_access_token.return_value = fix
        config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
        az = AuthZero(config)
        az.access_token = az.get_access_token()
        az.access_token_valid_until = 0
        az.access_token_auto_renew = True
        az._authorize(az.default_headers)

    @patch.object(AuthZero, "get_access_token")
    def test_expired_access_token(self, mock_get_access_token):
        fix_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/access_token.json')
        with open(fix_path) as fd:
            fix = json.load(fd)

        mock_get_access_token.return_value = fix
        config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
        az = AuthZero(config)
        az.access_token = az.get_access_token()
        az.access_token_valid_until = 0
        az.access_token_auto_renew = False
        with self.assertRaises(Exception) as context:
            az._authorize(az.default_headers)
        assert("('InvalidAccessToken', 'The access token has expired')" == str(context.exception))

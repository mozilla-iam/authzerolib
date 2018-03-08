#!/usr/bin/env python

import json
import unittest
import os
import sys

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
        assert(ret[0].get('id') != None)
        assert(ret[0].get('script') != None)
        assert(ret[0].get('enabled') == True)

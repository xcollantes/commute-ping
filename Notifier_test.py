# Lint as: python3
"""Tests for Notifier."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import Notifier
from unittest.mock import patch


class NotifierTest(unittest.TestCase):

  def setUp(self):
    self.home = '7904 Dublin Blvd, Dublin, CA 94568'
    self.work = '2000 Charleston Rd, Mountain View, CA 94043'


  @unittest.skip('Not sure how to best test Requests.')
  @patch('requests.get')
  def test_maps_scrape(self, mock_requests_get):
    res = Notifier.CallGoogleMaps(self.home, self.work)


  def test_parser(self):
    map_data = ''
    with open('test_data/google_maps_test.html') as test_html:
      map_data = Notifier._parse_maps(test_html.read())
    print(map_data)
    #self.assertEqual(map_data, '35 min')


if __name__ == '__main__':
  unittest.main()

"""Desktop notification system for commuters.

TODO(xcollantes): DO NOT SUBMIT without a detailed description of Notifier.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import subprocess
import requests
from typing import List
from bs4 import BeautifulSoup as bs4


def CallGoogleMaps(home: str, work: str) -> str:
  """Make HTTP request for Maps data.

  Args:
    home: Home address as string.
    work: Work address as string.

  Returns:
    Raw HTML data.

  Raises:
    Connection Error.
  """
  host = 'https://google.com/maps/dir'
  url = host + '/' + home + '/' + work

  response = requests.get(url)
  response.raise_for_status()

  return response.content



def _parse_maps(html:str):
  """Extract useful data from HTML."""
  soupy = bs4(html, 'lxml')
  first_drive_time = soupy.select("html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]")
  #first_drive_time = soupy.select("#section-directions-trip-0 > div.section-directions-trip-description > div:nth-child(1) > div.section-directions-trip-numbers > div.section-directions-trip-duration.delay-medium > span:nth-child(1)")
  return first_drive_time


def _format_message(maps_data:List) -> None:
  pass


def SendNote(message: str) -> None:
  """Runs the message on desktop, keeps visible for 10 seconds."""
  subprocess.run(['notify-send', '--expire-time', '10000', f'{message}'])



def main():
  home = ''
  work = ''

  html_response = CallGoogleMaps(home, work)
  print(html_response)
  #dict_map_data = _parse_maps(html_response)


  SendNote("Test Message.")

main()


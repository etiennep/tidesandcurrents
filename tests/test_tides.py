from unittest import TestCase
from tidesandcurrents import tides
from tidesandcurrents.tides import Tides
import datetime


class TidesTest(TestCase):

    def setUp(self):
        pass

    def test_load(self):
        tides_obj = tides.query_tides(datetime.date.today())
        assert tides_obj.data is not None

    def test_constructor(self):
        data = '2:43 AM|1.5|low\n' \
               '9:16 AM|5.7|high\n' \
               '3:34 PM|0.6|low\n' \
               '10:02 PM|4.6|high\n' \
               '3:34 PM|low\n'
        tides_obj = Tides(datetime.date.today(), data)
        assert tides_obj.data == data
        assert len(tides_obj.tides_table) == 4

    def test_str(self):
        data = '2:43 AM|1.5|low\n' \
               '9:16 AM|5.7|high\n' \
               '3:34 PM|0.6|low\n' \
               '10:02 PM|4.6|high\n' \
               '3:34 PM|low\n'
        tides_obj = Tides(datetime.date.today(), data)
        expected_str = '02:43 1.5 low\n' \
                       '09:16 5.7 high\n' \
                       '15:34 0.6 low\n' \
                       '22:02 4.6 high\n'

        assert str(tides_obj) == expected_str

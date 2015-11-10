from unittest import TestCase
from tidesandcurrents import currents
from tidesandcurrents.currents import Currents
import datetime


class CurrentsTest(TestCase):

    def setUp(self):
        pass

    def test_load(self):
        currents_obj = currents.query(datetime.date.today())
        assert currents_obj.data is not None
        print(str(currents_obj))

    # def test_constructor(self):
    #     data = '2:43 AM|1.5|low\n' \
    #            '9:16 AM|5.7|high\n' \
    #            '3:34 PM|0.6|low\n' \
    #            '10:02 PM|4.6|high\n' \
    #            '3:34 PM|low\n'
    #     tides_obj = Tides(datetime.date.today(), data)
    #     assert tides_obj.data == data
    #     assert len(tides_obj.tides_table) == 4
    #
    # def test_str(self):
    #     data = '2:43 AM|1.5|low\n' \
    #            '9:16 AM|5.7|high\n' \
    #            '3:34 PM|0.6|low\n' \
    #            '10:02 PM|4.6|high\n' \
    #            '3:34 PM|low\n'
    #     tides_obj = Tides(datetime.date.today(), data)
    #     expected_str = '2:43 AM|1.5|low\n' \
    #                    '9:16 AM|5.7|high\n' \
    #                    '3:34 PM|0.6|low\n' \
    #                    '10:02 PM|4.6|high\n'
    #
    #     assert str(tides_obj) == expected_str

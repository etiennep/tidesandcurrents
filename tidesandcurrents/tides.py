import requests
import datetime

def query_tides(date):
    tides_query = 'http://tidesandcurrents.noaa.gov/noaatidepredictions/StationTideInfo.jsp' \
              '?Stationid=9414290&timeZone=1{}'.format(date.strftime("&bmon=%m&bday=%d&byear=%Y"))
    r = requests.get(tides_query)
    return Tides(date, r.text)


class Tides:

    def __init__(self, date, data):
        self.date = date
        self.data = data
        self.tides_table = []
        self.parse_data(data)

    def parse_data(self, data_str):
        for line in data_str.strip().split('\n'):
            self.tides_table.append(line.split('|'))
        self.tides_table.pop()

    def __str__(self):
        ret_str = ''
        for item in self.tides_table:
            item_time = datetime.datetime.strptime(item[0], '%I:%M %p')
            ret_str += '{} {} {}\n'.format(item_time.time().strftime('%H:%M'), item[1], item[2])
        return ret_str

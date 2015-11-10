import requests
import datetime
from xml.etree import ElementTree


def query_currents(date):

    currents_query = 'http://tidesandcurrents.noaa.gov/noaacurrents/DownloadPredictions?fmt=xml&i=&r=1' \
                     '&tz=LST%2fLDT&u=1&id=SFB1203_18&t=am%2fpm&i=&threshold=&thresholdvalue=&d={}'.format(date.strftime("%Y-%m-%d"))
    r = requests.get(currents_query)
    return Currents(date, r.text)


class Currents:

    def __init__(self, date, data):
        self.date = date
        self.data = data
        self.tree = ElementTree.fromstring(data.encode('utf-8'))

    def __str__(self):
        ret_str = ''
        for item in self.tree.findall('./data/item'):
            for child in item:
                if child.tag == 'dateTime':
                    item_date_time = datetime.datetime.strptime(child.text, '%Y-%m-%d %H:%M')
                    if item_date_time.date() > self.date:
                        return ret_str
                    ret_str += item_date_time.time().strftime('%H:%M') + ' '
                elif child.tag == 'slack':
                    ret_str += 'slack\n'
                elif child.tag == 'ebb':
                    ret_str += child.text + "E\n"
                elif child.tag == 'flood':
                    ret_str += child.text + "F\n"
        return ret_str

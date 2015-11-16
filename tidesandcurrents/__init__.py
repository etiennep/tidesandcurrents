import tidesandcurrents.tides
import tidesandcurrents.currents


media_link = "http://livecams.ocscsailing.com/camera1.php"


def query_tides(date):
    return tides.query(date)


def query_currents(date):
    return currents.query(date)


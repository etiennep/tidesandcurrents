from __future__ import print_function
from flask import Flask, request
import twilio.twiml
import datetime
import tidesandcurrents

app = Flask(__name__)


def parse_date(date_str):
    clean_date_str = date_str.strip().lower()
    today = datetime.date.today()
    if clean_date_str == 'today':
        return today
    elif clean_date_str == 'tomorrow':
        return today + datetime.timedelta(days=1)
    else:
        try:
            ret = datetime.datetime.strptime(clean_date_str, '%m/%d/%Y').date()
            return ret if ret >= today else None
        except ValueError:
            return None


@app.route("/", methods=['GET', 'POST'])
def tides_and_currents():
    """Send the daily tide and current predictions"""

    request_message = request.values.get('Body', None)
    query_date = parse_date(request_message)
    resp = twilio.twiml.Response()

    if query_date is None:
        resp.message("Invalid request. Please send the words 'today', 'tomorrow', or a date (mm/dd/yyyy) to obtain "
                     "tide and current predictions.")
        return str(resp)

    try:
        tides = tidesandcurrents.query_tides(query_date)
        currents = tidesandcurrents.query_currents(query_date)
        message = 'Tide and current predictions for {}\nTides:\n{}\nCurrents:\n{}'.format(query_date.strftime('%m/%d/%Y'),
                                                                                          tides, currents)
        resp.message(message).media(tidesandcurrents.media_link)
    except:
        resp.message("Error trying to retrieve tide and current predictions. Please try again later.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

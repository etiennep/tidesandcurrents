from __future__ import print_function
from flask import Flask, request, redirect
import twilio.twiml
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    #&bmon=11&bday=09&byear=2015
    r = requests.get('http://tidesandcurrents.noaa.gov/noaatidepredictions/StationTideInfo.jsp?Stationid=9414290&timeZone=1')
    from_number = request.values.get('From', None)

    message = 'Tides for today\n' + r.text

    resp = twilio.twiml.Response()
    resp.message(message, media_url="http://livecams.ocscsailing.com/camera1.php")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
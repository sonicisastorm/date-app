from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

TIMEZONE = pytz.timezone('Asia/Baku')

@app.route('/date')
def date():
    now = datetime.now(TIMEZONE)
    current_time = now.strftime("%H:%M:%S")
    seconds = now.second
    parity = "EVEN" if seconds % 2 == 0 else "ODD"
    return f"{current_time} {parity}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

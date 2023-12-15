
from flask import Flask, render_template, send_file
import pandas as pd
from datetime import datetime
import os

from sqlalchemy import create_engine
oracle_connection_string = f"{database}+{connector}://{user}:{password}@{host}:{port}/{SID}"
oracle_engine = create_engine(oracle_connection_string)

tarih = None
df = None
    
app = Flask(__name__)

@app.route('/download')
def download():
    global tarih
    global df
    tarih = datetime.today().strftime('%d-%m-%Y')
    path = "./ReportLog/"
    file = f"gunluk_rapor_{tarih}.csv"
    
    if os.path.isdir(path):
        os.chdir(path)
        df.to_csv(file, index=False)
    else:
        os.mkdir(path)
        os.chdir(path)
        df.to_csv(file, index=False)
        
    return send_file(path+file, as_attachment=True)

@app.route("/")
def rapor():
    global df
    with oracle_engine.connect() as oracle_connection:
        tablename = "TABLE NAME"
        query = f"""SELECT COL1, SUM(COL2) AMOUNT FROM {tablename}
                    WHERE DATECOLUMN > TRUNC(CURRENT_DATE) - 2 AND
                    DATECOLUMN < TRUNC(CURRENT_DATE)
                    GROUP BY COLUMN"""
        df = pd.read_sql(query, oracle_connection)
    # Convert the dataframe to HTML
    table = df.to_html(index=False)
    
    # Render a template with the table
    return render_template('index.html', table=table)

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
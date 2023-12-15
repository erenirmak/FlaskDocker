
from flask import Flask, render_template, send_file
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import os

# Connection String & Database Engine
oracle_connection_string = f"{database}+{connector}://{user}:{password}@{host}:{port}/{SID}"
oracle_engine = create_engine(oracle_connection_string)

# Variables
today_date = None
df = None

# Flask App
app = Flask(__name__)

# /download route:
@app.route('/download')
def download():
    global today_date
    global df
    # Get today date:
    today_date = datetime.today().strftime('%d-%m-%Y')

    # Save location & File name
    path = "./ReportLog/"
    file = f"daily_report_{today_date}.csv"

    # File creation
    if os.path.isdir(path):
        os.chdir(path)
        df.to_csv(file, index=False)
    else:
        os.mkdir(path)
        os.chdir(path)
        df.to_csv(file, index=False)
    
    os.chdir("..")
    # Download file
    return send_file(path+file, as_attachment=True)

# index route:
@app.route("/")
def rapor():
    global df
    # Connect to the database
    with oracle_engine.connect() as oracle_connection:
        # Query construction
        tablename = "TABLE NAME"
        query = f"""SELECT COL1, SUM(COL2) AMOUNT FROM {tablename}
                    WHERE DATECOLUMN > TRUNC(CURRENT_DATE) - 2 AND
                    DATECOLUMN < TRUNC(CURRENT_DATE)
                    GROUP BY COLUMN"""
        # Load query result as Pandas DataFrame
        df = pd.read_sql(query, oracle_connection)
        
    # Convert the dataframe to HTML
    table = df.to_html(index=False)
    
    # Render a template with the table
    return render_template('index.html', table=table)

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    


from flask import Flask, render_template, send_file
from sqlalchemy import create_engine
import pandas as pd
import os

sqlsrv_connection_string = "mssql+pymssql://sa:e1r2e3n4@localhost:1433/Psychology"
sqlsrv_engine = create_engine(sqlsrv_connection_string)
with sqlsrv_engine.connect() as sqlsrv_connection:
    tablename = "client_id_info"
    query = f"""SELECT * FROM {tablename}"""
    df = pd.read_sql(query, sqlsrv_connection)
    
app = Flask(__name__)

@app.route('/download')
def download():    
    path = "C:/FlaskDownloads/"
    file = "myfile.csv"
    
    if os.path.isdir(path):
        os.chdir(path)
        df.to_csv(file)
    else:
        os.mkdir(path)
        os.chdir(path)
        df.to_csv(file)
        
    return send_file(path+file, as_attachment=True)

@app.route("/")
def rapor():    
    # Convert the dataframe to HTML
    table = df.to_html()
    
    # Render a template with the table
    return render_template('index.html', table=table)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    

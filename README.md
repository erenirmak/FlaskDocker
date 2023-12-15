# FlaskDocker

- Connect to your database (**enter your own credentials in corresponding areas before running the app**)
- Get your reports (**enter your own SQL query in corresponding area**)
- Integrated into Flask
- Deploy on Docker (run: > docker build && docker run)
- You can get your live reports and even download as CSV file (Pre-created CSV files are stored in ReportLog folder)

IMPORTANT: Depending on your database, you may need connectors; i.e. Oracle Data Access Client (ODAC) for Oracle, ODBC drivers, etc..

The main app is FlaskDocker.py. test.py was for experimenting some different approaches.
If you don't want to deploy on Docker, just run:
> python -m FlaskDocker

If you want to deploy on Docker, run:
> docker build --tag flask_daily_report .

> docker run -d -p 5000:5000 flask_daily_report

In both options, you should be able to see the queried table at:
http://localhost:5000/
or
http://127.0.0.1:5000/

The queried table as CSV file is saved to /ReportLog folder when you click 'Download File' link. Otherwise, it is not generated automatically.

I know that the UI is pretty raw. This is my first experiment with Flask and still learning. :)

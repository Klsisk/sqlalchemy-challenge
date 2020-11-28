import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import datetime as dt

from flask import Flask, jsonify

################################################
#Database Setup
################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database 
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
#Create application variable
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
#Create route for Home Page
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
        
    )


#Create route for precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Convert the query results to a dictionary using date as the key and prcp as the value"""
    # Query using date as the key and prcp as the value
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    year_precip = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).all()

    # Close session
    session.close()

    # Dict with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in year_precip}

    return jsonify(precip)


#Create route for stations
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()
    
    # Close session
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    
    return jsonify(all_stations)


#Create route for tobs
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the last 12 months of temperature observation data 
    tobs = session.query(Measurement.tobs).filter(Measurement.date >= one_year_ago).all()
    
    # Close session
    session.close()

    # Convert list of tuples into normal list on the temperature observations (TOBS) for the previous year
    tobs_list = list(np.ravel(tobs))

    return jsonify(tobs_list)

#Create routes start date of trip and start,end
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return TMIN, TAVG, TMAX."""

    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
    # calculate TMIN, TAVG, TMAX for dates greater than start & use np.ravel to get the results into a variable called "temps"
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    
    # If end is specified, the interpreter will jump here
    # calculate TMIN, TAVG, TMAX with start and stop
    results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

    # calculate TMIN, TAVG, TMAX for dates greater than end & use np.ravel to get the results into a variable called "temps=temps"
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == "__main__":
    app.run(debug=True)
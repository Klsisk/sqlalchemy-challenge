# SQLAlchemy :  Surfs Up!

## Background
Climate Analysis and Data Exploration of Climate Database Using Python (Pandas, Matplotlib), SQLAlchemy (ORM Queries) and Flask

## Objectives

### Step 1 - Climate Analysis and Exploration
Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy, Pandas, and Matplotlib.

### Precipitation Analysis
- Design a query to retrieve the last 12 months of precipitation data.
- Select only the date and prcp values.
- Load the query results into a Pandas DataFrame and set the index to the date column.
- Sort the DataFrame values by date.
- Plot the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/69765842/103467831-25e5aa80-4d21-11eb-9b51-0d218db23b9d.png)

### Station Analysis
- Design a query to calculate the total number of stations.
- Design a query to find the most active stations.
  - List the stations and observation counts in descending order.
  - Which station has the highest number of observations?
- Design a query to retrieve the last 12 months of temperature observation data (TOBS).
  - Filter by the station with the highest number of observations.
  - Plot the results as a histogram with bins=12.
  
![image](https://user-images.githubusercontent.com/69765842/103467838-3007a900-4d21-11eb-9ad3-3a8008ca940c.png)

### Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
-Use Flask to create your routes.

### Routes
- /
  - Home page.
  - List all routes that are available.
  
![image](https://user-images.githubusercontent.com/69765842/103468914-2fc0db00-4d2c-11eb-8bcd-2dfc6ac69c51.png)

- /api/v1.0/precipitation
  - Convert the query results to a dictionary using date as the key and prcp as the value.
  - Return the JSON representation of your dictionary.

![image](https://user-images.githubusercontent.com/69765842/103468917-3d766080-4d2c-11eb-9dbc-6d3b5b13bd44.png)
  
- /api/v1.0/stations
  - Return a JSON list of stations from the dataset.

![image](https://user-images.githubusercontent.com/69765842/103468919-45ce9b80-4d2c-11eb-8ff7-7eaa60db0a15.png)
  
- /api/v1.0/tobs
  - Query the dates and temperature observations of the most active station for the last year of data.
  - Return a JSON list of temperature observations (TOBS) for the previous year.
  
![image](https://user-images.githubusercontent.com/69765842/103468924-4ff09a00-4d2c-11eb-9b06-58e73d32a152.png)
  
- /api/v1.0/<start> and /api/v1.0/<start>/<end>
  - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
   
![image](https://user-images.githubusercontent.com/69765842/103468930-5717a800-4d2c-11eb-959e-398e6bdb535c.png)

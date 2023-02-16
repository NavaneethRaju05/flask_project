# flask_project
a simple web api to search for houses based on search parameters provided by user.

 

Endpoint Definition: GET <URL>/search

Inputs:

price: If a user gives price as 221900, houses with prices <=221900 only will be displayed.

sqft_living: User can give range from-to to filter values. If from=700 and to=2000, only house having sqft_living >= from and <= to should be displayed.

bedrooms: If user give bedrooms as 2, then only houses with 2 bedrooms should be displayed.

 

Any combination of above can also happen.

 

Outputs:

All fields for each house.

 

Programming Language:Python

Web Framework: Flask

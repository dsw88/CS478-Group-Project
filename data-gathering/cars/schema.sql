CREATE TABLE car (
    listing_id VARCHAR(50) PRIMARY KEY,
    vin VARCHAR(50),
    price REAL,
    fuel_type VARCHAR(50),
    mpg_city INTEGER,
    mpg_highway INTEGER,
    exterior_color VARCHAR(50),
    interior_color VARCHAR(50),
    engine VARCHAR(200),
    mileage INTEGER,
    advanced_details JSONB
);
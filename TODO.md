# TODO 
1. DB User Auth and role based $
2. Assets Setup DB $
3. Improve Unittest Setup $
4. Deploy to Google Cloud - See how DB will be deployed.
5. Create user interface. %
6. Create validations on UI
7. Maybe Change email, role and password

## DB Schema Below

1. Admin and Users Table 1 
Field Name | Data Type | Description
user_id | UUID / INT | Unique identifier for the user
first_name | VARCHAR | User’s first name
last_name | VARCHAR | User’s last name
email | VARCHAR (unique) | User's email address (used for login)
password_hash | TEXT | Hashed password for authentication
role | ENUM / VARCHAR | Role of the user (e.g., 'admin', 'user')
department | VARCHAR | Department user belongs to (optional)
phone_number | VARCHAR | Contact number
status | VARCHAR | Account status (e.g., 'active', 'inactive', 'suspended')
last_login | TIMESTAMP | Timestamp of the user's last login
created_at | TIMESTAMP | When the user record was created
updated_at | TIMESTAMP | When the user record was last updated

2. Assets Table 2
asset_id	UUID / INT	Unique identifier for the asset
asset_name	VARCHAR	Name or title of the asset
description	TEXT	Detailed description of the asset
category	VARCHAR	Category/type of asset (e.g., IT, Vehicle, Equipment)
serial_number	VARCHAR	Manufacturer's serial number
purchase_date	DATE	Date the asset was purchased
purchase_cost	DECIMAL(10,2)	Cost of the asset at time of purchase
vendor	VARCHAR	Supplier or vendor of the asset
location	VARCHAR	Physical or assigned location of the asset
assigned_to	VARCHAR / UUID	User or department assigned to the asset
status	VARCHAR	Current status (e.g., Active, In Maintenance, Retired)
warranty_expiry	DATE	Expiration date of the warranty
last_maintenance	DATE	Date of last maintenance activity
next_maintenance	DATE	Scheduled next maintenance date
depreciation_method	VARCHAR	Method used for depreciation (e.g., Straight-line)
useful_life_years	INT	Expected useful life in years
current_value	DECIMAL(10,2)	Current book value of the asset
image_url	VARCHAR / TEXT	URL or path to image of the asset
created_at	TIMESTAMP	Record creation timestamp
updated_at	TIMESTAMP	Record last update timestamp

3. Possibly think what 3 table may be for 
-- User Asset View Permission Table 3. -  user_id | asset_id
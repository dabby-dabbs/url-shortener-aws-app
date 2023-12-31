# url-shortener-aws-app

# Flask QR Code Generator

This is a Flask application that generates QR codes from URLs and provides a short URL for easy sharing. Users can register an account, log in, and track the number of clicks on their generated QR codes.

<img width="1118" alt="Screenshot 2023-07-14 at 10 19 26 AM" src="https://github.com/dabby-dabbs/url-shortener-aws-app/assets/93348569/5e343fec-528a-4bc8-a970-01e44ea99f89">


## Prerequisites

Before running the application, make sure you have the following:

- Python 3.6 or higher installed
- `pymysql`, `hashids`, `Flask`, `plotly`, `gradio_client`, `boto3`, and `botocore` Python packages installed
- Access to a MySQL database
- AWS S3 bucket credentials

## Configuration

1. Create a file named `config.json` in the same directory as the application file (`app.py`).
2. In `config.json`, add the following keys and provide the corresponding values:

```json
{
  "aws_access_key_id": "YOUR_AWS_ACCESS_KEY_ID",
  "aws_secret_access_key": "YOUR_AWS_SECRET_ACCESS_KEY",
  "bucket_name": "YOUR_BUCKET_NAME",
  "db_host": "YOUR_DATABASE_HOST",
  "db_port": "YOUR_DATABASE_PORT",
  "db_user": "YOUR_DATABASE_USERNAME",
  "db_password": "YOUR_DATABASE_PASSWORD",
  "db_database": "YOUR_DATABASE_NAME"
}

```

# QR Code Generator

This application allows you to generate QR codes and track clicks.

## Installation

1. Install the required Python packages by running the following command in your terminal:

`pip install pymysql hashids Flask plotly gradio_client boto3 botocore`

2. Make sure your MySQL database server is running.
3. Start the application by running the following command in your terminal:

`python app.py`

<img width="478" alt="image" src="https://github.com/dabby-dabbs/url-shortener-aws-app/assets/93348569/5eb2009d-9202-4007-89b4-b0699988d0ec">

<img width="480" alt="image" src="https://github.com/dabby-dabbs/url-shortener-aws-app/assets/93348569/60ff0b1e-2320-496f-a9f8-d8e37a72dd04">

<img width="481" alt="image" src="https://github.com/dabby-dabbs/url-shortener-aws-app/assets/93348569/e1bdfaaa-9918-4e52-9826-44a5b6a9c447">



# Usage
Open your web browser and access the application at http://localhost:5000.
Click on the "Register" link to create a new account.
Enter a username and password in the registration form.
Click the "Register" button.
After logging in, you will be redirected to the main page.
Enter a URL in the input field.
Optionally, enter an image description.
Click the "Generate QR Code" button.
The generated QR code will be displayed on the page.
The short URL for the generated QR code will also be shown.
Click on the "Stats" link to view click statistics for your generated QR codes.
The page will display a bar graph showing the number of clicks per URL and a pie chart showing the distribution of clicks among URLs.
Click on the "Logout" link to log out of your account.

# Features
Generate QR codes for any URL.
Track clicks on your generated QR codes.
View click statistics for your generated QR codes.

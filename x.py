from flask import request, make_response
import mysql.connector
import re #Regular expressions - Regex
from functools import wraps

##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view

##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password",
            database = "2026_travel"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)


##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
REGEX_USER_FIRST_NAME = f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()  
    if not re.match(REGEX_USER_FIRST_NAME, user_first_name):
        raise Exception(f"company_exception user_first_name")    

    return user_first_name

##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
REGEX_USER_LAST_NAME = f"^.{{{USER_LAST_NAME_MIN},{USER_LAST_NAME_MAX}}}$"
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name", "").strip()  
    if not re.match(REGEX_USER_LAST_NAME, user_last_name):
        raise Exception(f"company_exception user_last_name")    

    return user_last_name


##############################
REGEX_USER_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    user_email = request.form.get("user_email", "").strip()
    if not re.match(REGEX_USER_EMAIL, user_email):
        raise Exception("company_exception user_email")
    return user_email

##############################
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD= f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()  
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception(f"company_exception user_password")    

    return user_password


##############################
DESTINATION_NAME_MIN = 2
DESTINATION_NAME_MAX = 50
REGEX_DESTINATION_NAME= f"^.{{{DESTINATION_NAME_MIN},{DESTINATION_NAME_MAX}}}$"
def validate_destination_name():
    destination_name = request.form.get("destination_name", "").strip()  
    if not re.match(REGEX_DESTINATION_NAME, destination_name):
        raise Exception(f"company_exception destination_name")    

    return destination_name

##############################
DESTINATION_DESCRIPTION_MIN = 2
DESTINATION_DESCRIPTION_MAX = 255
REGEX_DESTINATION_DESCRIPTION= f"^.{{{DESTINATION_DESCRIPTION_MIN},{DESTINATION_DESCRIPTION_MAX}}}$"
def validate_destination_description():
    destination_description = request.form.get("destination_description", "").strip()  
    if not re.match(REGEX_DESTINATION_DESCRIPTION, destination_description):
        raise Exception(f"company_exception destination_description")    

    return destination_description

##############################
DESTINATION_CITY_MIN = 2
DESTINATION_CITY_MAX = 40
REGEX_DESTINATION_CITY= f"^.{{{DESTINATION_CITY_MIN},{DESTINATION_CITY_MAX}}}$"
def validate_destination_city():
    destination_city = request.form.get("destination_city", "").strip()  
    if not re.match(REGEX_DESTINATION_CITY, destination_city):
        raise Exception(f"company_exception destination_city")    

    return destination_city

##############################
DESTINATION_COUNTRY_MIN = 2
DESTINATION_COUNTRY_MAX = 40
REGEX_DESTINATION_COUNTRY= f"^.{{{DESTINATION_COUNTRY_MIN},{DESTINATION_COUNTRY_MAX}}}$"
def validate_destination_country():
    destination_country = request.form.get("destination_country", "").strip()  
    if not re.match(REGEX_DESTINATION_COUNTRY, destination_country):
        raise Exception(f"company_exception destination_country")    

    return destination_country




from flask import Flask, render_template, request, jsonify, session, redirect
import x
import uuid
import time
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.get("/profile")
@x.no_cache
def show_profile():
    try:
        user = session.get("user", "")
        if not user: return redirect("/login")
        user_firstname = session["user"]["user_first_name"]
        user_lastname = session["user"]["user_last_name"]
        return render_template("page_profile.html", user=user, x=x, title=f"{user_firstname} {user_lastname}")
    except Exception as ex:
        ic(ex)
        return str(ex)

####################################
@app.get("/signup")
@x.no_cache
def show_signup():
    try:
        user = session.get("user", "")
        if user: return redirect("/profile")
        return render_template("page_signup.html", user=user, x=x, title="Signup")
    except Exception as ex:
        ic(ex)
        return str(ex)
    
####################################
@app.post("/api-create-user")
def create_user():
    try:
        user_first_name = x.validate_user_first_name()
        user_last_name = x.validate_user_last_name()
        user_email=x.validate_user_email()
        user_password=x.validate_user_password()
        user_hashed_password = generate_password_hash(user_password)
        user_pk = uuid.uuid4().hex
        user_created_at = int(time.time())
        
        db, cursor = x.db()
        q = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_pk, user_first_name, user_last_name, user_email, user_hashed_password, user_created_at))
        db.commit()

        form_signup = render_template("___form_signup.html", x=x)

        return f"""
        <browser mix-replace="form">{form_signup}</browser>
        <browser mix-redirect="/login"></browser>
        """
    
    except Exception as ex:
         ic(ex)
         if "company_exception user_first_name" in str(ex):
            error_message = f"user first name {x.USER_FIRST_NAME_MIN} to {x.USER_FIRST_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>,""", 400
         
         if "company_exception user_last_name" in str(ex):
            error_message = f"user last name {x.USER_LAST_NAME_MIN} to {x.USER_LAST_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "company_exception user_email" in str(ex):
            error_message = f"user email invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "company_exception user_password" in str(ex):
            error_message = f"user password {x.USER_PASSWORD_MIN} to {x.USER_PASSWORD_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "Duplicate entry" in str(ex) and "user_email" in str(ex):
            error_message = "Email already exists"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         #Worst case
         error_message = "System under maintenance"
         ___tip = render_template("___tip.html", status="error", message=error_message)
         return f"""
        <browser mix-after-begin="#tooltip">{___tip}</browser>""", 500
    finally:

        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

####################################
@app.get("/login")
@x.no_cache
def show_login():
    try:
        user = session.get("user", "")
        if user: return redirect("/profile")
        return render_template("page_login.html", user=user, x=x, title="Login")
        
    except Exception as ex:
        ic(ex)
        return "ups"

####################################   
@app.post("/api-login")
def login():
    try:
        user_email=x.validate_user_email()
        user_password=x.validate_user_password()
        
        db, cursor = x.db()
        q = "SELECT * FROM users WHERE user_email = %s"
        cursor.execute(q, (user_email,))
        user = cursor.fetchone()
        if not user:
            error_message = "Invalid credentials 1"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
        
        if not check_password_hash(user["user_password"], user_password):
            error_message = "Invalid credentials 2"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
        
        user.pop("user_password")
        session["user"] = user
        ic(user)
        

        """
        q = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_pk, user_first_name, user_last_name, user_email, user_hashed_password, user_created_at))
        db.commit()"""
        return f"""<browser mix-redirect="/profile"></browser>"""
    
    except Exception as ex:
         ic(ex)
         if "company_exception user_email" in str(ex):
            error_message = f"user email invalid"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "company_exception user_password" in str(ex):
            error_message = f"user password {x.USER_PASSWORD_MIN} to {x.USER_PASSWORD_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         #Worst case
         error_message = "System under maintenance"
         ___tip = render_template("___tip.html", status="error", message=error_message)
         return f"""
        <browser mix-after-begin="#tooltip">{___tip}</browser>""", 500
    finally:

        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
    
####################################
@app.get("/logout")
@x.no_cache
def logout():
    try:
        session.clear()
        return redirect("/login")
    except Exception as ex:
        ic(ex)
        return str(ex)
    
####################################
@app.post("/api-create-destination")
def create_destination():
    try:
        destination_name = x.validate_destination_name()
        destination_description = x.validate_destination_description()
        destination_city = x.validate_destination_city()
        destination_country = x.validate_destination_country()
        destination_pk = uuid.uuid4().hex
        user_pk = session["user"]["user_pk"]
        

        db, cursor = x.db()
        q = "INSERT INTO destinations VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (destination_pk, destination_name, destination_description, destination_city, destination_country, user_pk))
        db.commit()

        return f"""
        <browser mix-redirect="/destinations"></browser>
        """
    
    except Exception as ex:
         ic(ex)
         if "company_exception destination_name" in str(ex):
            error_message = f"destination name {x.DESTINATION_NAME_MIN} to {x.DESTINATION_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>,""", 400
         
         if "company_exception destination_description" in str(ex):
            error_message = f"destination description {x.DESTINATION_DESCRIPTION_MIN} to {x.DESTINATION_DESCRIPTION_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "company_exception destination_city" in str(ex):
            error_message = f"destination city {x.DESTINATION_CITY_MIN} to {x.DESTINATION_CITY_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         
         if "company_exception destination_country" in str(ex):
            error_message = f"destination country {x.DESTINATION_COUNTRY_MIN} to {x.DESTINATION_COUNTRY_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         #Worst case
         error_message = "System under maintenance"
         ___tip = render_template("___tip.html", status="error", message=error_message)
         return f"""
        <browser mix-after-begin="#tooltip">{___tip}</browser>""", 500
    finally:

        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

####################################
@app.get("/create-destination")
@x.no_cache
def show_create_destination():
    try:
        user = session.get("user", "")
        return render_template("page_create_destination.html", user=user, x=x)
    except Exception as ex:
        ic(ex)
        return f"{ex}", 500

####################################
@app.get("/destinations")
@x.no_cache
def show_destinations():
    try:
        db, cursor = x.db()
        q = "SELECT * FROM destinations"
        cursor.execute(q)
        destinations = cursor.fetchall()
        user = session.get("user", "")
        return render_template("page_destinations.html", destinations=destinations, user=user, x=x, title="Destinations")
    except Exception as ex:
        ic(ex)
        return str(ex)
    finally:

        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

####################################
@app.get("/update-destination/<destination_pk>")
@x.no_cache
def show_update_destination(destination_pk):
    try:
        db, cursor = x.db()
        q = "SELECT * FROM destinations where destination_pk = %s"
        cursor.execute(q, (destination_pk, ))
        destination = cursor.fetchone()
        user = session.get("user", "")
        return render_template("page_update_destination.html", destination=destination, user=user, x=x, title="Update")
    except Exception as ex:
        ic(ex)
        return str(ex)
    finally:

        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.patch("/api-update-destination/<destination_pk>")
def update_destination(destination_pk):
    try:

        parts = []
        values = []

        destination_name = x.validate_destination_name()
        if destination_name:
            parts.append("destination_name = %s")
            values.append(destination_name)

        destination_description = x.validate_destination_description()
        if destination_description:
            parts.append("destination_description = %s")
            values.append(destination_description)

        destination_city = x.validate_destination_city()
        if destination_city:
            parts.append("destination_city = %s")
            values.append(destination_city)

        destination_country = x.validate_destination_country()
        if destination_country:
            parts.append("destination_country = %s")
            values.append(destination_country)


        if not destination_name and not destination_description and not destination_city and not destination_country: return "nothing to update", 400
        # Convert the list to a string with a comma in between
        partial_query = ", ".join(parts)

        values.append(destination_pk)

        print(parts, flush=True)
        print(values, flush=True)
        print(partial_query, flush=True)

        q = f"""
            UPDATE destinations
            SET	{partial_query}
            WHERE destination_pk = %s
        """
        print(q, flush=True)

        db, cursor = x.db()
        cursor.execute(q, values)
        db.commit()
        return f"""
        <browser mix-redirect="/destinations"></browser>
        """


    except Exception as ex:
         ic(ex)
         if "company_exception destination_name" in str(ex):
            error_message = f"destination name {x.DESTINATION_NAME_MIN} to {x.DESTINATION_NAME_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>,""", 400
         
         if "company_exception destination_description" in str(ex):
            error_message = f"destination description {x.DESTINATION_DESCRIPTION_MIN} to {x.DESTINATION_DESCRIPTION_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         if "company_exception destination_city" in str(ex):
            error_message = f"destination city {x.DESTINATION_CITY_MIN} to {x.DESTINATION_CITY_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         
         if "company_exception destination_country" in str(ex):
            error_message = f"destination country {x.DESTINATION_COUNTRY_MIN} to {x.DESTINATION_COUNTRY_MAX} characters"
            ___tip = render_template("___tip.html", status="error", message=error_message)
            return f"""
            <browser mix-after-begin="#tooltip">{___tip}</browser>""", 400
         
         #Worst case
         error_message = "System under maintenance"
         ___tip = render_template("___tip.html", status="error", message=error_message)
         return f"""
        <browser mix-after-begin="#tooltip">{___tip}</browser>""", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.delete("/api-delete-destination/<destination_pk>")
def delete_destination(destination_pk):
    try:
        db, cursor = x.db()
        q = "DELETE FROM destinations WHERE destination_pk = %s"
        cursor.execute(q, (destination_pk,))
        db.commit()
        return f"""
        <browser mix-redirect="/destinations"></browser>
        """
    except Exception as ex:
        pass
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
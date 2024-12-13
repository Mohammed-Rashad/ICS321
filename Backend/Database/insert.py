import mysql.connector

myHost = "localhost"
myUser = "root"
myPassword = "password"
myDatabase = "TRAIN_MANAGEMENT_SYSTEM"

def connectToDatabase():    # Establishes a connection and returns the connector object used by other functions
                            # Use at the start of the program running
    try:
        conn = mysql.connector.connect(
            host=myHost,
            user=myUser,
            password=myPassword,
            database=myDatabase
        )
        return conn

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def closeConnection(conn):      # Closes the connection
                                # Use at the end of he program running
    if conn.is_connected():
        conn.close()
        

# The database connection is the first argument of every function in this file

def insertTrain(number, maxPassengers):
    
    try:
        conn = connectToDatabase()
        cur = conn.cursor()
        query = "INSERT INTO train (trainNumber,maxPassenger) VALUES (%s,%s)"

        # Input validation
        if maxPassengers <= 0:
            raise ValueError("MaxPassengers cannot be less than or equal to zero")

        cur.execute(query, (number, maxPassengers))
        conn.commit()
        cur.close()

        print("Inserted train successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def insertPassenger(conn, id, name, balance):

    # Input validation
    if balance < 0:
        raise ValueError("Balance cannot be less than zero")

    cur = conn.cursor()
    query = "INSERT INTO passenger (ID, Name, Balance) VALUES (%s, %s, %s)"

    try:
        cur.execute(query, (id, name, balance))
        conn.commit()
        print("Inserted passenger successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Dependent function
def insertDependent(conn, id, name, guardianID):
    cur = conn.cursor()

    # Check if the guardian exists
    query = "SELECT ID FROM passenger WHERE ID = %s"
    cur.execute(query, (guardianID,))
    if not cur.fetchone():
        cur.close()
        raise ValueError("Guardian does not exist")

    query = "INSERT INTO dependent (ID, Name, GuardianID) VALUES (%s, %s, %s)"

    try:
        cur.execute(query, (id, name, guardianID))
        conn.commit()
        print("Inserted dependent successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Station function
def insertStation(conn, name, city):
    cur = conn.cursor()

    query = "INSERT INTO station (Name, City) VALUES (%s, %s)"
    try:
        cur.execute(query, (name, city))
        conn.commit()
        print("Inserted station successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


def insertTrip(conn, tripNumber, date, trainNumber):
    cur = conn.cursor()

    check_train_query = "SELECT COUNT(*) FROM train WHERE TrainNumber = %s"
    insert_query = "INSERT INTO trip (TripNumber, Date, TrainNumber) VALUES (%s, %s, %s)"

    # Validate trainNumber exists
    cur.execute(check_train_query, (trainNumber,))
    train_exists = cur.fetchone()[0]

    if train_exists == 0:
        cur.close()
        raise ValueError(f"TrainNumber {trainNumber} does not exist in the train table.")

    try:

        # Proceed with the insertion
        cur.execute(insert_query, (tripNumber, date, trainNumber))
        conn.commit()
        print("Inserted trip successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()



def insertTripStop(conn, tripNumber, date, stopOrder, stationName):     # Seats available is set to number of seats by default
    cur = conn.cursor()

    # Query to get MaxPassenger from the train table
    get_max_passenger_query = """
        SELECT t.MaxPassenger
        FROM train t
        JOIN trip tr ON t.TrainNumber = tr.TrainNumber
        WHERE tr.TripNumber = %s AND tr.Date = %s
    """

    # Query to insert data into trip_stop table
    insert_query = """
        INSERT INTO trip_stop (TripNumber, Date, StopOrder, StationName, SeatsAvailable) 
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        # Fetch MaxPassenger
        cur.execute(get_max_passenger_query, (tripNumber, date))
        result = cur.fetchone()

        if not result:
            cur.close()
            raise ValueError(f"No matching trip found for TripNumber {tripNumber} on Date {date}")

        max_passengers = result[0]

        # Proceed with the insertion
        cur.execute(insert_query, (tripNumber, date, stopOrder, stationName, max_passengers))
        conn.commit()
        print("Inserted trip stop successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Reservation function
def insertReservation(conn, passengerID, tripNumber, date, firstStation, lastStation, seatNumber):
    cur = conn.cursor()

    query = "INSERT INTO reservation (PassengerID, TripNumber, Date, FirstStation, LastStation, SeatNumber) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation, seatNumber))
        conn.commit()
        print("Inserted reservation successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Waitlist function
def insertWaitlist(conn, passengerID, tripNumber, date, firstStation, lastStation):
    cur = conn.cursor()

    query = "INSERT INTO waitlist (PassengerID, TripNumber, Date, FirstStation, LastStation) VALUES (%s, %s, %s, %s, %s)"
    try:
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        conn.commit()
        print("Inserted waitlist entry successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()

# // a function to check username and password in the database admin table using 'with' keyword for better data handling //this comment is not chatgpted

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
def checkAdmin(email, password):
    try:
        conn = connectToDatabase()  # Assuming this function provides a valid DB connection
        cur = conn.cursor()
        query = "SELECT email, password FROM admin WHERE email = %s"
        cur.execute(query, (email,))
        result = cur.fetchone()

        # Check if user was found
        if result:
            # The result contains (username, hashed_password)
            stored_username, stored_hashed_password = result

            # Check if the password matches the stored hashed password
            if check_password_hash(stored_hashed_password, password):
                return True  # Admin credentials are valid
            else:
                return False  # Incorrect password
        else:
            return False  # No such admin user found

    except mysql.connector.Error as e:
        print(f"Error checking admin credentials: {e}")
        return False  # Return False on error, you might want to log the error elsewhere

    finally:
        # Ensure resources are cleaned up properly
        if cur:
            cur.close()
        if conn:
            conn.commit()
            
# admin schema
# CREATE TABLE admin (
#     ID INT AUTO_INCREMENT NOT NULL,           -- Automatically incremented primary key
#     email VARCHAR(100) NOT NULL,              -- Email cannot be null
#     password VARCHAR(255) NOT NULL,           -- Sufficient space for hashed passwords
#     Name VARCHAR(30) NOT NULL,                -- Name of the admin, cannot be null
#     Salary DECIMAL(10, 2),                    -- Salary with 2 decimal places
#     PRIMARY KEY (ID),                        -- Primary key on ID
#     UNIQUE (email)                           -- Ensure email is unique across all records
# );
# a function that created a new admin user
def addAdmin(email, password, name, salary):
    try:
        conn = connectToDatabase()  # Assuming this function provides a valid DB connection
        cur = conn.cursor()
        query = "INSERT INTO admin (email, password, Name, Salary) VALUES (%s, %s, %s, %s)"
        hashed_password = generate_password_hash(password)  # Hash the password before storing
        cur.execute(query, (email, hashed_password, name, salary))
        conn.commit()
        return True  # Admin user added successfully

    except mysql.connector.Error as e:
        print(f"Error adding admin user: {e}")
        conn.rollback()
        return False  # Return False on error, you might want to log the error elsewhere

    finally:
        # Ensure resources are cleaned up properly
        if cur:
            cur.close()
        if conn:
            conn.commit()

# print(addAdmin("mo@gmail.com", "password", "Mo", 1000.00))
# print(checkAdmin("mo@gmail.com", "password"))
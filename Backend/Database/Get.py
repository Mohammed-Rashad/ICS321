import mysql.connector
from . import Connect


def getAllTrains():
    conn = Connect.getConnection()
    cur = conn.cursor()
    query = "SELECT * FROM train"
    try:
        cur.execute(query)
        result = cur.fetchall()
        if result:
            print(f"Train details: {result}")
            return result
        else:
            print(f"No trains found.")
            return None
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        cur.close()
    
    
    
def getTrain(trainNumber):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get a train by its TrainNumber
    query = "SELECT * FROM train WHERE TrainNumber = %s"

    try:
        # Execute the select query
        cur.execute(query, (trainNumber,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Train details for TrainNumber {trainNumber}: {result}")
            return result
        else:
            print(f"No train found with TrainNumber = {trainNumber}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()


def getAdmin(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get an admin by its ID
    query = "SELECT * FROM admin WHERE ID = %s"

    try:
        # Execute the select query
        cur.execute(query, (id,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Admin details for ID {id}: {result}")
            return result
        else:
            print(f"No admin found with ID = {id}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()


def getEmployee(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get an employee by its ID
    query = "SELECT * FROM employee WHERE id = %s"

    try:
        # Execute the select query
        cur.execute(query, (id,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Employee details for ID {id}: {result}")
            return result
        else:
            print(f"No employee found with ID = {id}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()


def getPassenger(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get a passenger by their ID
    query = "SELECT * FROM passenger WHERE ID = %s"

    try:
        # Execute the select query
        cur.execute(query, (id,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Passenger details for ID {id}: {result}")
            return result
        else:
            print(f"No passenger found with ID = {id}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()


def getDependent(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get a dependent by their ID
    query = "SELECT * FROM dependent WHERE ID = %s"

    try:
        # Execute the select query
        cur.execute(query, (id,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Dependent details for ID {id}: {result}")
            return result
        else:
            print(f"No dependent found with ID = {id}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()


def getStation(name):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = "SELECT * FROM station WHERE Name = %s"

    try:
        cur.execute(query, (name,))
        result = cur.fetchone()

        if result:
            print(f"Station details for {name}: {result}")
            return result
        else:
            print(f"No station found with the name {name}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()


def getTrip(tripNumber, date):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = "SELECT * FROM trip WHERE TripNumber = %s AND Date = %s"

    try:
        cur.execute(query, (tripNumber, date))
        result = cur.fetchone()

        if result:
            print(f"Trip details for TripNumber {tripNumber} on {date}: {result}")
            return result
        else:
            print(f"No trip found with TripNumber {tripNumber} on {date}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()


def getTripStop(number, date, time):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = "SELECT * FROM trip_stop WHERE TripNumber = %s AND Date = %s AND time = %s"

    try:
        cur.execute(query, (number, date, time))
        result = cur.fetchone()

        if result:
            print(f"Trip Stop details for TripNumber {number}, Date {date}, time {time}: {result}")
            return result
        else:
            print(f"No trip stop found for TripNumber {number}, Date {date}, time {time}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()

def getAllTrainStopsForTrip(number, date):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = "SELECT * FROM trip_stop WHERE TripNumber = %s AND Date = %s Order by Time"

    try:
        cur.execute(query, (number, date))
        result = cur.fetchall()

        if result:
            print(f"Trip Stop details for TripNumber {number}, Date {date}: {result}")
            return result
        else:
            print(f"No trip stop found for TripNumber {number}, Date {date}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()

def getReservation(passengerID, tripNumber, date, firstStation, lastStation):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = """SELECT * FROM reservation 
               WHERE PassengerID = %s AND TripNumber = %s AND Date = %s 
               AND FirstStation = %s AND LastStation = %s"""

    try:
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        result = cur.fetchone()

        if result:
            print(f"Reservation details for PassengerID {passengerID}, TripNumber {tripNumber}, Date {date}: {result}")
            return result
        else:
            print(f"No reservation found for PassengerID {passengerID}, TripNumber {tripNumber}, Date {date}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()


def getWaitlist(passengerID, tripNumber, date, firstStation, lastStation):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = """SELECT * FROM waitlist 
               WHERE PassengerID = %s AND TripNumber = %s AND Date = %s 
               AND FirstStation = %s AND LastStation = %s"""

    try:
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        result = cur.fetchone()

        if result:
            print(f"Waitlist details for PassengerID {passengerID}, TripNumber {tripNumber}, Date {date}: {result}")
            return result
        else:
            print(f"No waitlist found for PassengerID {passengerID}, TripNumber {tripNumber}, Date {date}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error retrieving data: {e}")
        return None

    finally:
        cur.close()



from werkzeug.security import check_password_hash
def checkAdmin(email, password):
    try:
        conn = Connect.getConnection()  # Assuming this function provides a valid DB connection
        cur = conn.cursor()
        query = "SELECT ID, email, password FROM admin WHERE email = %s"
        cur.execute(query, (email,))
        result = cur.fetchone()

        # Check if user was found
        if result:
            # The result contains (username, hashed_password)
            id, stored_username, stored_password = result

            # Check if the password matches the stored hashed password
            if stored_password == password:
                return result  # Admin credentials are valid
            else:
                return None  # Incorrect password
        else:
            return None  # No such admin user found

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


# CREATE TABLE `passenger` (
#   `ID` int NOT NULL,
#   `Name` varchar(30) NOT NULL,
#   `Balance` int NOT NULL,
#   `password` varchar(255) NOT NULL,
#   `email` varchar(50) NOT NULL,
#   `phone` varchar(14) NOT NULL,
#   PRIMARY KEY (`ID`)
# )

# check if passenger exists with email and password

def checkUser(email, password):
    try:
        conn = Connect.getConnection()  # Assuming this function provides a valid DB connection
        cur = conn.cursor()
        query = "SELECT ID, email, password, Name FROM passenger WHERE email = %s"
        cur.execute(query, (email,))
        result = cur.fetchone()
        # Check if user was found
        if result:
            # The result contains (username, hashed_password)
            id, stored_username, stored_password, name = result

            # Check if the password matches the stored hashed password
            # for my future me. Plese forgive me for this. I am sorry. 
            # I had to do this
            if stored_password == password:
                return result  # Passenger credentials are valid
            else:
                return None  # Incorrect password
        else:
            return None  # No such passenger user found

    except mysql.connector.Error as e:
        print(f"Error checking passenger credentials: {e}")
        return False  # Return False on error, you might want to log the error elsewhere

    finally:
        # Ensure resources are cleaned up properly
        if cur:
            cur.close()
        if conn:
            conn.commit()
            


#  get passenger by email (check email used)
def getPassengerByEmail(email):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to get a passenger by their email
    query = "SELECT * FROM passenger WHERE email = %s"

    try:
        # Execute the select query
        cur.execute(query, (email,))

        # Fetch the result
        result = cur.fetchone()

        if result:
            print(f"Passenger details for email {email}: {result}")
            return result
        else:
            print(f"No passenger found with email = {email}.")
            return None

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None

    finally:
        cur.close()




def getAllTrips(date):
    conn = Connect.getConnection()
    cur = conn.cursor()
    query = "SELECT * FROM trip t JOIN trip_stop s ON t.TripNumber=s.TripNumber and t.Date = s.Date WHERE t.date >= %s order by t.Date, t.TripNumber, s.Time"
    try:
        cur.execute(query, (date,))
        result = cur.fetchall()
        if result:
            # print(f"Trip details: {result}")
            trainsList = []
            trainDic = {}
            # the result is originally a join of trip and trip_stop, I want to get a list of dictionary with trainNumber, date, time, list of station Names
            for trip in result:
                tripNumber, date, trainNumber, tripNumber2, date2, stationName, time = trip
                if not (tripNumber, date) in trainDic:
                    trainDic[(tripNumber, date)] = {"tripNumber": tripNumber,"trainNumber": trainNumber, "date": date, "stations": [stationName], "times": [time]}
                else:
                    trainDic[(tripNumber, date)]["stations"].append(stationName)
                    trainDic[(tripNumber, date)]["times"].append(time)
            return trainDic
        else:
            print(f"No trips found.")
            return {}
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        cur.close()
        

    
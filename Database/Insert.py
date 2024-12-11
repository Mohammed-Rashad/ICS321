import mysql.connector


# The database connection is the first argument of every function in this file

def insertTrain(conn, number, maxPassengers):
    cur = conn.cursor()
    query = "INSERT INTO train (trainNumber,maxPassenger) VALUES (%s,%s)"

    # Input validation
    if maxPassengers <= 0:
        raise ValueError("MaxPassengers cannot be less than or equal to zero")

    try:
        cur.execute(query, (number, maxPassengers))
        conn.commit()
        cur.close()

        print("Inserted train successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


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

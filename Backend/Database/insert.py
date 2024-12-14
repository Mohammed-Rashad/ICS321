import mysql.connector
from . import Connect

# The database connection is the first argument of every function in this file

def insertTrain(number, maxPassengers, cost):
    conn = Connect.getConnection()
    cur = conn.cursor()
    query = "INSERT INTO train (trainNumber, maxPassenger, cost) VALUES (%s,%s,%s)"

    # Input validation
    if maxPassengers <= 0:
        raise ValueError("MaxPassengers cannot be less than or equal to zero")

    try:
        cur.execute(query, (number, maxPassengers, cost))
        conn.commit()
        cur.close()

        print("Inserted train successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


def insertPassenger(id, name, balance, password, email, phone):
    conn = Connect.getConnection()

    # Input validation for balance
    if balance < 0:
        raise ValueError("Balance cannot be less than zero")

    cur = conn.cursor()
    query = "INSERT INTO passenger (ID, Name, Balance, Password, Email, Phone) VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cur.execute(query, (id, name, balance, password, email, phone))
        conn.commit()
        print("Inserted passenger successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Dependent function
def insertDependent(id, name, guardianID):
    conn = Connect.getConnection()

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
def insertStation(name, city):
    conn = Connect.getConnection()

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


def insertTrip(tripNumber, date, trainNumber):
    conn = Connect.getConnection()

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


def insertTripStop(tripNumber, date, time, stationName):
    conn = Connect.getConnection()
    cur = conn.cursor()

    try:
        # Get the current stop order based on time
        query = """
        SELECT COUNT(*)
        FROM trip_stop
        WHERE TripNumber = %s
        AND Date = %s
        AND Time < %s
        """
        cur.execute(query, (tripNumber, date, time))
        stopOrder = cur.fetchone()[0] + 1  # +1 to place it after existing earlier stops

        # Shift all future stops forward
        query = """
        UPDATE trip_stop
        SET StopOrder = StopOrder + 1
        WHERE TripNumber = %s
        AND Date = %s
        AND StopOrder >= %s
        """
        cur.execute(query, (tripNumber, date, stopOrder))

        # Insert the new stop
        query = """
        INSERT INTO trip_stop (TripNumber, Date, StopOrder, StationName, Time) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (tripNumber, date, stopOrder, stationName, time))
        conn.commit()
        print("Inserted trip stop successfully")

    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

    finally:
        cur.close()


# Insert Reservation function
def insertReservation(passengerID, tripNumber, date, firstStation, lastStation, seatNumber):
    conn = Connect.getConnection()

    cur = conn.cursor()

    query = "INSERT INTO reservation (PassengerID, TripNumber, Date, FirstStation, LastStation, SeatNumber, hasPaid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation, seatNumber, 0))   #default is hasn't paid
        conn.commit()
        print("Inserted reservation successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


# Insert Waitlist function
def insertWaitlist(passengerID, tripNumber, date, firstStation, lastStation):
    conn = Connect.getConnection()

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


def insertAdmin(id, email, password, name, salary):
    conn = Connect.getConnection()

    cur = conn.cursor()
    query = "INSERT INTO admin (ID, Email, Password, Name, Salary) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(query, (id, email, password, name, salary))
        conn.commit()
        print("Inserted admin successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


def insertEmployee(id, email, password, name, salary):
    conn = Connect.getConnection()

    cur = conn.cursor()
    query = "INSERT INTO Employee (id, email, password, Name, Salary) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(query, (id, email, password, name, salary))
        conn.commit()
        print("Inserted employee successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()


def insertAssigned(id, date, number):
    conn = Connect.getConnection()
    cur = conn.cursor()
    query = "INSERT INTO Assigned (employeeId, Date, trainNumber) VALUES (%s, %s, %s)"

    try:
        cur.execute(query, (id, date, number))
        conn.commit()
        print("Inserted assigned successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cur.close()
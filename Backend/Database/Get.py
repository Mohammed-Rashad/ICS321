import mysql.connector
from . import Connect


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


def getTripStop(number, date, stopOrder):
    conn = Connect.getConnection()  # Assuming getConnection() gives you the active connection
    cur = conn.cursor()

    query = "SELECT * FROM trip_stop WHERE TripNumber = %s AND Date = %s AND StopOrder = %s"

    try:
        cur.execute(query, (number, date, stopOrder))
        result = cur.fetchone()

        if result:
            print(f"Trip Stop details for TripNumber {number}, Date {date}, StopOrder {stopOrder}: {result}")
            return result
        else:
            print(f"No trip stop found for TripNumber {number}, Date {date}, StopOrder {stopOrder}.")
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

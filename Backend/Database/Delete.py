import mysql.connector
from . import Connect


def deleteTrain(number):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a train by its TrainNumber
    query = "DELETE FROM train WHERE TrainNumber = %s"

    try:
        # Execute the delete query
        cur.execute(query, (number,))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted train with TrainNumber = {number}.")
            return True
        else:
            print(f"No train found with TrainNumber = {number}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteStation(name):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a station by its Name
    query = "DELETE FROM station WHERE Name = %s"

    try:
        # Execute the delete query
        cur.execute(query, (name,))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted station with Name = {name}.")
            return True
        else:
            print(f"No station found with Name = {name}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteAdmin(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete an admin by its ID
    query = "DELETE FROM admin WHERE ID = %s"

    try:
        # Execute the delete query
        cur.execute(query, (id,))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted admin with ID = {id}.")
            return True
        else:
            print(f"No admin found with ID = {id}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deletePassenger(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a passenger by its ID
    query = "DELETE FROM passenger WHERE ID = %s"

    try:
        # Execute the delete query
        cur.execute(query, (id,))

        count = cur.rowcount

        query = """
                DELETE FROM person WHERE ID = %s
                """

        cur.execute(query, (id,))

        conn.commit()

        # Check if a row was deleted
        if count > 0:
            print(f"Deleted passenger with ID = {id}.")
            return True
        else:
            print(f"No passenger found with ID = {id}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteEmployee(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete an employee by its ID
    query = "DELETE FROM employee WHERE id = %s"

    try:
        # Execute the delete query
        cur.execute(query, (id,))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted employee with ID = {id}.")
            return True
        else:
            print(f"No employee found with ID = {id}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteDependent(id):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a dependent by its ID
    query = "DELETE FROM dependent WHERE ID = %s"

    try:
        # Execute the delete query
        cur.execute(query, (id,))
        count = cur.rowcount

        query = """
                DELETE FROM person WHERE ID = %s
                """

        cur.execute(query, (id,))

        conn.commit()

        # Check if a row was deleted
        if count > 0:
            print(f"Deleted dependent with ID = {id}.")
            return True
        else:
            print(f"No dependent found with ID = {id}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteTrip(tripNumber, date):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a trip by its TripNumber and Date
    query = "DELETE FROM trip WHERE TripNumber = %s AND Date = %s"

    try:
        # Execute the delete query
        cur.execute(query, (tripNumber, date))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted trip with TripNumber = {tripNumber} and Date = {date}.")
            return True
        else:
            print(f"No trip found with TripNumber = {tripNumber} and Date = {date}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteTripStop(tripNumber, date, time):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a trip stop by its TripNumber, Date, and time
    query = "DELETE FROM trip_stop WHERE TripNumber = %s AND Date = %s AND time = %s"

    try:
        # Execute the delete query
        cur.execute(query, (tripNumber, date, time))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted trip stop with TripNumber = {tripNumber}, Date = {date}, and time = {time}.")
            return True
        else:
            print(f"No trip stop found with TripNumber = {tripNumber}, Date = {date}, and time = {time}.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteReservation(passengerID, tripNumber, date):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a reservation by its passengerID, tripNumber, date, firstStation, and lastStation
    query = """
        DELETE FROM reservation 
        WHERE PassengerID = %s AND TripNumber = %s AND Date = %s 
    """

    try:
        # Execute the delete query
        cur.execute(query, (passengerID, tripNumber, date))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted reservation for PassengerID = {passengerID}, TripNumber = {tripNumber}, Date = {date}.")
            return True
        else:
            print(f"No reservation found with the given parameters.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteWaitlist(passengerID, tripNumber, date, firstStation, lastStation):
    conn = Connect.getConnection()
    cur = conn.cursor()

    # Query to delete a waitlist entry by its passengerID, tripNumber, date, firstStation, and lastStation
    query = """
        DELETE FROM waitlist 
        WHERE PassengerID = %s AND TripNumber = %s AND Date = %s 
        AND FirstStation = %s AND LastStation = %s
    """

    try:
        # Execute the delete query
        cur.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        conn.commit()

        # Check if a row was deleted
        if cur.rowcount > 0:
            print(f"Deleted waitlist entry for PassengerID = {passengerID}, TripNumber = {tripNumber}, Date = {date}, FirstStation = {firstStation}, LastStation = {lastStation}.")
            return True
        else:
            print(f"No waitlist entry found with the given parameters.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()


def deleteAssigned(id, date):
    conn = Connect.getConnection()
    cur = conn.cursor()
    query = """
    DELETE FROM assigned
    WHERE employeeID = %s AND Date = %s
    """

    try:
        cur.execute(query, (id, date))
        conn.commit()

        if cur.rowcount > 0:
            print(f"Deleted assigned entry for employeeID = {id}, Date = {date}.")
            return True
        else:
            print(f"No assigned entry found with the given parameters.")
            return False

    except mysql.connector.Error as e:
        print(f"Error deleting data: {e}")
        conn.rollback()
        return False

    finally:
        cur.close()
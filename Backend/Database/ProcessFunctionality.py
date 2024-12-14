from . import Connect
from . import insert
from . import Delete
from . import Get
import mysql.connector


#Functions of a passenger
#Search for trains

#Returns a list of trip numbers that go from initial to final on a specific date
def searchForTrain(initialStation, finalStation, date):
    conn = Connect.getConnection()

    cursor = conn.cursor()

    query = """
    SELECT initial.TripNumber
    FROM trip_stop AS initial
    JOIN trip_stop AS final
    ON initial.TripNumber = final.TripNumber
       AND initial.Date = final.Date
       AND initial.time < final.time
    WHERE initial.StationName = '%s'
      AND final.StationName = '%s'
      AND initial.Date = '%s';
    """

    try:
        cursor.execute(query, (initialStation, finalStation, date))
        return cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Error searching for trips: {err}")
        return None

    finally:
        cursor.close()


#Book seats

#Returns a sorted list of available seats
def availableSeats(tripNumber, date, initialStation, finalStation):     #use initial & final station numbers from the trip stop table
    conn = Connect.getConnection()
    cursor = conn.cursor()

    query = """     
    SELECT SeatNumber
    FROM reservation
    WHERE TripNumber = '%s'
    AND Date = %s
    AND LastStation > '%s'
    AND FirstStation < '%s'
    """     #All taken seat numbers

    try:
        cursor.execute(query, (tripNumber, date, initialStation, finalStation))
        takenSeats = cursor.fetchall()
        takenSeats = [i[0] for i in takenSeats]

        #getting the max number of seats
        query = """
        SELECT maxPassenger
        FROM train
        JOIN trip
        ON train.TrainNumber = trip.TrainNumber
        WHERE trip.TripNumber = '%s'
        AND trip.Date = '%s'
        """

        cursor.execute(query, (tripNumber, date))
        maxSeats = cursor.fetchall()
        maxSeats = maxSeats[0][0]

        allSeats = set(range(1, maxSeats + 1))

        availableSeats = allSeats - set(takenSeats)
        return sorted(list(availableSeats))

    except mysql.connector.Error as err:
        print(f"Error searching for seats: {err}")
        return None

    finally:
        cursor.close()


#Takes a list of ids and a train number and returns if it is possible for all listed people to board the train
def canAfford(idList, trainNumber):
    conn = Connect.getConnection()
    cursor = conn.cursor()

    query = """
    SELECT Cost
    FROM train
    WHERE TrainNumber = '%s'
    """

    try:
        cursor.execute(query, (trainNumber,))
        cost = cursor.fetchall()[0][0]
        payment = {}
        for id in idList:
            query = """
            SELECT *
            FROM passenger
            WHERE id = '%s'
            """
            cursor.execute(query, (id,))
            if cursor.rowcount:
                payment[id] = payment.get(id, 0) + cost
            else:
                query = """
                SELECT GuardianID
                FROM dependent
                WHERE id = '%s'
                """
                cursor.execute(query, (id,))
                guardian = cursor.fetchall()[0][0]
                payment[guardian] = payment.get(guardian, 0) + cost

        for id in idList:
            query = """
            SELECT Balance
            FROM passenger
            WHERE id = '%s'
            """
            cursor.execute(query, (id,))
            balance = cursor.fetchall()[0][0]
            if balance < payment[id]:
                return False

        return True

    except mysql.connector.Error as err:
        print(f"Error while calculating cost: {err}")
        return False
    finally:
        cursor.close()


#createReservation already exists in 'Insert.py'
#createWaitlist also exists in 'Insert.py'

#Complete payment

#pay for a reservation
#Note: returns true if paid successfully or if already paid before
def pay(passengerID, tripNumber, date, firstStation, lastStation):
    conn = Connect.getConnection()
    cursor = conn.cursor()

    query = """
    SELECT cost
    FROM train
    JOIN trip
    ON train.TrainNumber = trip.TrainNumber
    WHERE TripNumber = '%s'
    and Date = '%s'
    """

    try:
        cursor.execute(query, (tripNumber, date))
        cost = cursor.fetchall()[0][0]

        query = """
        SELECT hasPaid
        FROM reservation
        WHERE PassengerID = '%s'
        AND TripNumber = '%s'
        AND Date = '%s'
        AND FirstStation = '%s'
        AND LastStation = '%s'
        """

        cursor.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        hasPaid = cursor.fetchall()[0][0]

        if hasPaid:
            return True

        if not canAfford([passengerID], tripNumber):
            return False

        query = """
        UPDATE Passenger
        SET Balance = Balance - '%s'
        WHERE ID = '%s'
        """

        cursor.execute(query, (cost, id))

        query = """
        UPDATE reservation
        SET hasPaid = 1
        WHERE PassengerID = '%s'
        AND TripNumber = '%s'
        AND Date = '%s'
        AND FirstStation = '%s'
        AND LastStation = '%s'
        """

        cursor.execute(query, (passengerID, tripNumber, date, firstStation, lastStation))
        conn.commit()

        return True
    except mysql.connector.Error as err:
        print(f"Error while paying: {err}")
        conn.rollback()
        return False
    finally:
        cursor.close()


#Functions of Staff/Admin

#Add/Edit/Cancel reservation/ticket
#Add and cancel already exist
#For edit just remove and add again (don't forget to check the valid seat numbers for the adjusted trip and the cost and everything)
#You will probably need this
#Search for all reservations of a given id
def getAllReservations(passengerId):
    conn = Connect.getConnection()
    cursor = conn.cursor()
    query = """
    SELECT *
    FROM reservation
    WHERE PassengerID = '%s'
    """

    try:
        cursor.execute(query, (passengerId,))
        reservations = cursor.fetchall()
        return reservations

    except mysql.connector.Error as err:
        print(f"Error searching for reservations: {err}")
        return None

    finally:
        cursor.close()

#Assign staff to a train for a given date
#(insert/delete/get)Assigned were added

#Promote a waitlisted passenger
#You can just removeWaitlist(...) and insertReservation(...)
#You will also probably need this
#Search for all waitlistings of a given id
def getAllWaitlists(passengerId):
    conn = Connect.getConnection()
    cursor = conn.cursor()
    query = """
    SELECT *
    FROM waitlist
    WHERE PassengerID = '%s'
    """

    try:
        cursor.execute(query, (passengerId,))
        waitlists = cursor.fetchall()
        return waitlists

    except mysql.connector.Error as err:
        print(f"Error searching for waitlists: {err}")
        return None

    finally:
        cursor.close()


#Functions of System

#Send email reminders to passengers who did not pay

#Get id of all passengers travelling a certain day who haven't paid yet
def getHaventPaid(date):
    conn = Connect.getConnection()
    cursor = conn.cursor()

    query = """
    SELECT PassengerID
    FROM reservation
    WHERE Date = '%s'
    AND HasPaid = 0
    """

    try:
        cursor.execute(query, (date,))
        reservations = cursor.fetchall()
        return [i[0] for i in reservations]

    except mysql.connector.Error as err:
        print(f"Error searching for reservations who haven't paid: {err}")
        return None

    finally:
        cursor.close()


#Using a trigger send a message to a passenger 3 hours before the departure of his train

#This is what I can do I guess
#Get id of all passengers leaving from a certain station at a certain trip on a certain day
def getStationPassengers(tripNumber, date, stationName):
    conn = Connect.getConnection()
    cursor = conn.cursor()

    query = """
    SELECT PassengerID
    FROM reservation
    JOIN trip_stop
    ON reservation.TripNumber = trip_stop.TripNumber
    AND reservation.Date = trip_stop.Date
    AND reservation.FirstStation = trip_stop.time
    WHERE reservation.TripNumber = '%s'
    AND reservation.Date = '%s'
    AND trip_stop.StationName = '%s'
    """

    try:
        cursor.execute(query, (stationName, date))
        reservations = cursor.fetchall()
        return [i[0] for i in reservations]

    except mysql.connector.Error as err:
        print(f"Error searching for reservations leaving from a station: {err}")

#General Function

#Login and logout
#getPassenger, getEmployee, getAdmin is all you need from me :)


#Generate Reports

#Current active trains that are on their way today

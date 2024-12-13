import Connect
import Insert
import Delete
import Get
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
       AND initial.StopOrder < final.StopOrder
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

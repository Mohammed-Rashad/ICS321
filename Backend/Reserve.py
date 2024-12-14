from Database import ProcessFunctionality
from Database import Insert


#Takes trip details and completes reservation
#firstStation and lastStation are of type TIME
def reserve(id, tripNumber, date, firstStation, lastStation):
    seats = ProcessFunctionality.availableSeats(tripNumber, date, firstStation, lastStation)
    if not seats:
        return False

    seat = seats[0]

    return Insert.insertReservation(id, tripNumber, date, firstStation, lastStation, seat)

import Connect
from Insert import insertTrain

con = Connect.connectToDatabase()
insertTrain(con, 1234, 20)
Connect.closeConnection(con)

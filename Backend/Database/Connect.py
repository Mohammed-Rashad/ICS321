import mysql.connector

# Replace username and password
myHost = "localhost"
myUser = "root"
myPassword = "FreeSyria:)"
myDatabase = "TRAIN_MANAGEMENT_SYSTEM"

connection = None


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


def getConnection():
    global connection
    if not connection:
        connection = connectToDatabase()
        print("connection established")
    return connection


def closeConnection(conn):      # Closes the connection
                                # Use at the end of the program running
    if conn.is_connected():
        conn.close()

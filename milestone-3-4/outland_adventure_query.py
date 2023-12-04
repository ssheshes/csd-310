import operator
import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "user": "outland_user",
    "password": "adventure",
    "host": "localhost",
    "database": "Outland Adventures",  # Corrected database name
    "raise_on_warnings": True
}

try:
    # Establishing a connection to the database
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))
    input("\n\n Press enter to continue...\n")

    cursor = db.cursor()

    #QUERY FOR PERCENTAGE OF BOOKINGS FOR EACH DESTINATION
    cursor.execute("select name as 'Name', continent as 'Destination' from customer INNER JOIN destination ON customer.destination=destination.destinationID;")
    
    #turns the table into a dictionary, named customers
    desc = cursor.description
    column_names = [col[0] for col in desc]
    customers = [dict(zip(column_names, row))
                 for row in cursor.fetchall()]
    #displays the dictionary
    print("==DISPLAYING CUSTOMERS AND THEIR BOOKED DESTINATIONS==")
    print(customers)

    #converts the destinations of the dictionary into a list to count values
    destinations = [i["Destination"] for i in customers]
    #print(destinations)

    #initialize total number of customers
    total_bookings = (len(customers))

    #count number of bookings for each country and turns that result into a percentage
    afr = destinations.count("Africa")
    asia = destinations.count("Asia")
    eur = destinations.count("Europe")
    percentAfr = '{0:.2f}'.format((afr/total_bookings) * 100)
    percentAsia = '{0:.2f}'.format((asia/total_bookings) * 100)
    percentEur = '{0:.2f}'.format((eur/total_bookings) * 100)
    print("The percentage of bookings for Africa is {}%." .format(percentAfr))
    print("The percentage of bookings for Asia is {}%." .format(percentAsia))
    print("The percentage of bookings for Europe is {}%." .format(percentEur))
    print()

    #QUERYING FOR PERCENTAGE OF EQUIPMENT PURCHASE VS RENTAL
    cursor.execute("SELECT name as 'Name', equipStatus as 'Status' FROM customer")
    desc2 = cursor.description
    column_names2 = [col[0] for col in desc2]
    equipStatus = [dict(zip(column_names2, row))
                 for row in cursor.fetchall()]
    
    print("==DISPLAYING CUSTOMERS AND THEIR EQUIPMENT STATUS==")
    print(equipStatus)

    #initialize total number of customers
    total_customers = (len(equipStatus))

    #converts the status of the dictionary into a list to count values
    status = [i["Status"] for i in equipStatus]
    #print(status)

    #count number of rentals for each customer and turns that result into a percentage
    purchase = status.count("Purchase")
    rental = status.count("Rental")
    percentPurchase = '{0:.2f}'.format((purchase/total_customers) * 100)
    percentRent = '{0:.2f}'.format((rental/total_customers) * 100)
    print("{}% of customers have purchased equipment." .format(percentPurchase))
    print("{}% of customers have rented equipment." .format(percentRent))
    print()
    
    #QUERY FOR ITEMS OVER 5 YEARS OLD
    cursor.execute("SELECT equipmentName as 'Equipment', acquisitionDate as 'Acquired' FROM equipment")
    desc3 = cursor.description
    column_names3 = [col[0] for col in desc3]
    equipDate = [dict(zip(column_names3, row))
                 for row in cursor.fetchall()]
    
    print("==DISPLAYING EQUIPMENT AND THEIR ACQUISITION DATE==")
    print(equipDate)

    ###Not sure how to continue this one, we can filter out the equipment with dates that make it older than 5 years, 
    ###if anyone wants to have a go at it.


    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

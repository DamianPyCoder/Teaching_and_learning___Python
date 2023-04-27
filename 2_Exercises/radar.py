def checkSpeed(distance, maxSpeed, time):

    #velocitat mitjana del cotxe en Km/h
    avgSpeed = (distance*3600) /(1000*time)
    #print("avgSpeed:",avgSpeed)

    if (avgSpeed <= maxSpeed):
        return "OK"
    elif (avgSpeed > maxSpeed and avgSpeed <= maxSpeed*1.2):
        return "Multa"
    else:
        return "Punts"

    
distance = int(input("Escriu la distancia entre els radars (metres): "));
maxSpeed = int(input("Escriu la velocitat maxima (Km/h): "));
time = int(input("Temps que ha trigat un cotxe a recórrer el tram (segons): "));

print(checkSpeed(distance, maxSpeed, time))

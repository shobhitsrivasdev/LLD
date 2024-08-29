Core Classes:

Vehicle: Represents vehicles with license plate and type
ParkingSpot: Manages individual parking spaces
ParkingTicket: Tracks parking sessions
ParkingLot: Main class orchestrating the entire system


Enums:

VehicleType: Different types of vehicles (Motorcycle, Car, Bus, Truck)
ParkingSpotType: Different types of parking spots (Motorcycle, Compact, Large)


Key Features:

Flexible spot allocation strategy
Time-based fee calculation
Support for different vehicle types
Ticket-based tracking system


Design Patterns Used:

Strategy Pattern: For parking fee calculation
Factory Pattern: For creating parking spots
Singleton Pattern: Could be applied to ParkingLot class
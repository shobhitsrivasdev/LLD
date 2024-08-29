from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
  def __init__(self, spot_number:int):
    self.spot_number = spot_number
    self.vehicle_type = VehicleType.Car
    self.parked_vehicle = None
    
  def is_available(self):
    if self.parked_vehicle is None:
      return True
    return False
  
  def park_vehicle(self, vehicle:Vehicle):
    if self.parked_vehicle is None and self.vehicle_type == vehicle.get_type():
      self.parked_vehicle = vehicle
    else:
      raise ValueError("Vehicle Already parked")
    
  def unpark_vehicle(self):
    self.parked_vehicle = None
    
  def get_vehicle_type(self):
    return self.vehicle_type
  
  def get_parked_vehicle(self):
    return self.parked_vehicle
  
  def get_spot_number(self):
    return self.spot_number
    
  
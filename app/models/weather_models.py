from pydantic import BaseModel
from typing import Optional, List

class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    condition: str

class AQIData(BaseModel):
    city: str
    aqi: int

class AlertData(BaseModel):
    city: str
    alerts: List[str] = []

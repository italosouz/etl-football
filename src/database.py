from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clima = Column(String, nullable=False)
    clima_detail = Column(String, nullable=False)
    temp = Column(Float, nullable=False)
    sensacao_termica = Column(Float, nullable=False)
    temp_min = Column(Float, nullable=False)
    temp_max = Column(Float, nullable=False)
    pressao_atm = Column(Integer, nullable=False)
    umidade = Column(Integer, nullable=False)
    visibilidade = Column(Integer, nullable=False)
    velocidade_vento = Column(Float, nullable=False)
    direcao_vento = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now)   
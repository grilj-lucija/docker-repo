# uporabimo python sliko
FROM python:3.11-slim   

#nastavimo delovno mapo
WORKDIR /app

#kopiramo kodo v zabojnik
COPY run.py .

#ob zagonu zabojnika zaženemo run.py
CMD ["python", "run.py"]
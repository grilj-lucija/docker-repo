import subprocess

def test_izpis():
    #pozenemo run.py in preverimo, da se izpise "Hello, Lucija!"
    rezultat = subprocess.run (
        ["python", "run.py"], 
        capture_output =True, 
        text = True
    )
    
    assert "Hello Lucija! (python)" in rezultat.stdout  # preverimo ali se tekst v izpisu ujema s pricakovanim besedilom
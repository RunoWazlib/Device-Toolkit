import os

def test_DriverExists():
    # Check if driver.py exists
    assert os.path.isfile("driver.py"), "[!] driver.py file is missing"

def test_DriverRuns():
    # Attempt to run driver.py and capture output
    try:
        output = os.popen("python3 driver.py").read()
        assert "[*] Static Information:" in output, "[!] driver.py did not run as expected"
    except Exception as e:
        assert False, f"[!] Error running driver.py: {e}"
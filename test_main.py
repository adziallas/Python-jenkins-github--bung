import main

def test_credentials():
    username, password = main.load_credentials("secrets.yaml")
    assert username == "admin"
    assert password == "pass123"

import yaml

def load_credentials(path="secrets.yaml"):
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        return data.get("username"), data.get("password")

def main():
    username, password = load_credentials()
    print(f"Authentifizierung erfolgreich für Benutzer: {username}")

if __name__ == "__main__":
    main()

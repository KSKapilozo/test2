import requests

def get_random_quote():
    try:
        response = requests.get("https//api.quotable.io")
        if response.status_code == 200:
            data = response.json()
            return data["content"]
        else:
            return f"{response.status_code}"
    except Exception as error:
        return f"{error}"

if __name__ == "__main__":
    print("zmiana")
    print(get_random_quote())

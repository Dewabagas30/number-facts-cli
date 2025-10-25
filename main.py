import requests

def get_number_fact(number: str):
    url = f"http://numbersapi.com/{number}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(f"🔢 {response.text}")
    except requests.RequestException as e:
        print(f"❌ Error fetching fact: {e}")

if __name__ == "__main__":
    number = input("Enter a number (or 'random'): ").strip() or "random"
    get_number_fact(number)

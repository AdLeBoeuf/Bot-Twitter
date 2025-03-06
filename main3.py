from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle
from CompteASuivre import USERNAME

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

url = f"https://twitter.com/{USERNAME}"
dernier_tweet = None

driver.get(url)
time.sleep(25)

cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)

print("Cookies enregistrés, tu peux maintenant redémarrer le script.")

driver.quit()

driver = webdriver.Chrome(options=options)
driver.get("https://twitter.com")

with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)


driver.refresh()
time.sleep(3)

while True:
    try:
        driver.get(url) 
        time.sleep(3)

        tweets = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweetText']")
        
        if tweets:
            tweet_text = tweets[0].text.strip()
            if tweet_text != dernier_tweet:
                print(f"Nouveau tweet détecté : {tweet_text}")
                dernier_tweet = tweet_text
            else:
                print("Aucun nouveau tweet.")
        else:
            print("Aucun tweet trouvé.")

        time.sleep(1)

    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)

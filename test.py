from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def get_last_posts(username):
    url = f"https://www.instagram.com/{username}/"
    
    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    
    # Esperar a que la página cargue completamente
    time.sleep(10)
    
    # Intentar encontrar los elementos con la clase especificada
    clases = [
        "x1i10hfl",
        "xjbqb8w",
        "x1ejq31n",
        "xd10rxx",
        "x1sy0etr",
        "x17r0tee",
        "x972fbf",
        "xcfux6l",
        "x1qhh985",
        "xm0m39n",
        "x9f619",
        "x1ypdohk",
        "xt0psk2",
        "xe8uvvx",
        "xdj266r",
        "x11i5rnm",
        "xat24cr",
        "x1mh8g0r",
        "xexx8yu",
        "x4uap5",
        "x18d9i69",
        "xkhd6sd",
        "x16tdsg8",
        "x1hl2dhg",
        "xggy1nq",
        "x1a2a7pz",
        "_a6hd",
    ]
    clase_list = ".".join(clases)
    elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"a.{clase_list}"))
    )
    
    if not elements:
        print(f"No se encontraron elementos con la clase '{clase_list}'. Es posible que la página no se haya cargado correctamente.")
        return []

    all_urls = [element.get_attribute('href') for element in elements]
    urls = []
    for url in all_urls:
        options = [f"https://www.instagram.com/{username}/reel/", f"https://www.instagram.com/{username}/p/"]
        if any(option in url for option in options):
            urls.append(url)
    driver.quit()
    return urls
    try:
        pass
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        return []
    finally:
        driver.quit()

def main():
    username = "twicetagram"
    urls = get_last_posts(username)
    print(urls)

if __name__ == "__main__":
    main()


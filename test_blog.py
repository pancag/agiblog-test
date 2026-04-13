import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def test_search_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://blogdoagi.com.br/")
    
    search_box = driver.find_element(By.NAME, "s")  # Localiza a caixa de pesquisa
    search_box.send_keys("tecnologia")  # Insira uma palavra-chave válida
    search_box.send_keys(Keys.RETURN)  # Pressiona Enter
    
    time.sleep(2)  # Aguarde os resultados carregarem
    assert "Resultados da pesquisa" in driver.page_source  # Verifica se a página contém a frase esperada
    driver.quit()

def test_search_invalid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://blogdoagi.com.br/")
    
    search_box = driver.find_element(By.NAME, "s")  # Localiza a caixa de pesquisa
    search_box.send_keys("xyz123")  # Insira uma palavra-chave inválida
    search_box.send_keys(Keys.RETURN)  # Pressiona Enter
    
    time.sleep(2)  # Aguarde os resultados carregarem
    assert "Nenhum resultado encontrado" in driver.page_source  # Verifica se a página contém a frase esperada
    driver.quit()

if __name__ == "__main__":
    test_search_valid_keyword()
    test_search_invalid_keyword()
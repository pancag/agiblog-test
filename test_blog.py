from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_search_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://blogdoagi.com.br/")
    
    search_box = driver.find_element(By.NAME, "s")  
    search_box.send_keys("tecnologia")  
    search_box.send_keys(Keys.RETURN)  
    
    time.sleep(2)  
    assert "Resultados da pesquisa" in driver.page_source  esperada
    driver.quit()

def test_search_invalid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://blogdoagi.com.br/")
    
    search_box = driver.find_element(By.NAME, "s")  
    search_box.send_keys("xyz123")  
    search_box.send_keys(Keys.RETURN)  
    
    time.sleep(2) 
    assert "Nenhum resultado encontrado" in driver.page_source  
    driver.quit()

if __name__ == "__main__":
    test_search_valid_keyword()
    test_search_invalid_keyword()
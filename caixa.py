import undetected_chromedriver as uc
import time
import json

info = ''
with open("dados.json", "r") as file:
    info = json.load(file)

while True:

    driver = uc.Chrome()
    
    try:
        driver.get("https://internetbanking.caixa.gov.br/sinbc/#!nb/login")

        time.sleep(4)

        driver.find_element_by_id("btnAdesao").click()

        time.sleep(2)

        driver.find_element_by_id("liAceitoRegulamento").click()
        driver.find_element_by_id("btnConcordar").click()

        time.sleep(3)

        driver.find_element_by_id("nome").send_keys(info["nome"])

        time.sleep(2)

        driver.find_element_by_id("cpf").send_keys(info["cpf"])

        time.sleep(2)

        driver.find_element_by_id("dataNascimento").send_keys(info["dtaNascimento"])

        driver.find_element_by_id("btnContinuar").click()

        time.sleep(3)

        driver.find_element_by_xpath("//select[@id='tipoContaDestino']/option[text()='Conta Corrente PF 001']").click()
        driver.find_element_by_id("agencia").send_keys(info["agencia"])
        driver.find_element_by_id("conta").send_keys(info["conta"])
        driver.find_element_by_id("digito").send_keys(info["digito-conta"])

        for digito in info["senha"]:
            driver.find_element_by_xpath("//li[text()='{}']".format(digito)).click()

        driver.find_element_by_id("btnConfirmar").click()

        time.sleep(20)

        driver.quit()
        
    except Exception as error:
        print(str(error))
        driver.quit()
        time.sleep(2)
        continue

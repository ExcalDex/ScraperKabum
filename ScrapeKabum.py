from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ScraperKabum():

    def __init__(self, produto:str) -> None:
        self.__produto: str = produto
        self.__data: dict[str, str | float] = {}
        self.chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.chrome_service)
        self.driver.get(f'https://www.kabum.com.br/busca/{self.__produto.replace(" ", "-")}')

    def get_all_pages(self) -> list[str]:
        """
        Returns:
            list[str]: list with all of the links which contain the desired product.
        """
        links: list[str] = list()
        j: int = 2
        times_ten_correction = 0
        while True:
            try:
                element = self.driver.find_element('xpath', '//*[@id="listingEmpty"]/b')
                if element.text == "Lamentamos, nenhum produto encontrado com esse critério de pesquisa.":
                    break
            except:
                ...
            for i in range(1, 21):
                try:
                    links.append(self.driver.find_element('xpath', f'//*[@id="listing"]/div[3]/div/div/div[2]/div[1]/main/div[{i}]/a').get_attribute('href'))
                except:
                    ...
            try:
                if(j != 2):
                    vaux = f"?&page_number={j}"
                    self.driver.get(f"{self.driver.current_url[:-len(vaux)+times_ten_correction]}?&page_number={j}")
                    if j == 9 or j == 99 or j == 999:
                        times_ten_correction = 1
                    elif times_ten_correction != 0:
                        times_ten_correction = 0
                else:
                    self.driver.get(f"{self.driver.current_url}?&page_number=2")
            except:
                ...
            j += 1
        
        return links

    def get_page_contents(self, links: list[str]) -> dict[str, list[str | float]]:
        data: dict[str, list[str | float]] = {'Nome' : [], 'Valor' : [], 'Link': []}
        contador: int = 0
        for link in links:
            try:
                self.driver.get(link)
                data['Link'].append(link)
                try:
                    element = self.driver.find_element('xpath', '//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1')
                    print(link)
                    data['Nome'].append(element.text)
                    try:
                        element = self.driver.find_element('xpath', '//*[@id="blocoValores"]/div[2]/div[1]/div/h4')
                        print(data['Nome'][-1])
                        data['Valor'].append(element.text)
                        print(element.text)
                    except:
                        del data['Link'][-1]
                        del data['Nome'][-1]
                        contador += 1
                        if contador == 30:
                            break
                        print("100 preco")
                except:
                    del data['Link'][-1]
                    print("100 nome")
            except:
                print("100 link")
        return data
    

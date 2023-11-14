import requests
from lxml import html

class ScraperKabum():
    def __init__(self, produto:str) -> None:
        self.__produto: str = produto
        self.__data: dict[str, list[str]] = {'Nome' : [], 'Valor' : [], 'Link': []}
    
    def get_all_pages(self) -> list[str]:
        links: list[str] = list()
        j: int = 2
        times_ten_correction = 0
        page = requests.get(f'https://www.kabum.com.br/busca/{self.__produto.replace(" ", "-")}')
        while True:
            titulo_acabou = html.fromstring(page.content).xpath('//*[@id="listingEmpty"]/b')
            if len(titulo_acabou) > 0:
                break
            for i in range(1, 21):
                link = html.fromstring(page.content).xpath(f'//*[@id="listing"]/div[3]/div/div/div[2]/div[1]/main/div[{i}]/a/@href')
                if len(link) != 0:
                    print(link)
                    links.append(f'https://www.kabum.com.br{link}'.replace('[', "").replace("]", "").replace(r"'", ""))
                else:
                    break
            if(j != 2):
                vaux = f"?&page_number={j}"
                page = requests.get(f"{page.url[:-len(vaux)+times_ten_correction]}?&page_number={j}")
                if j == 9 or j == 99 or j == 999:
                    times_ten_correction = 1
                elif times_ten_correction != 0:
                    times_ten_correction = 0
            else:
                page = requests.get(f"{page.url}?&page_number=2")
            j += 1

        return links

    def get_pages_contents(self, links: list[str]) -> dict:
        contador: int = 0
        for link in links:
            if link == '':
                break
            page = requests.get(link)
            tree = html.fromstring(page.content)
            nome: str = tree.xpath('//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1/text()')
            if len(nome) == 0:
                nome = tree.xpath('//*[@id="__next"]/main/article/section/div[2]/div[1]/div/h1/text()')
                if len(nome) != 0:
                    valor: str = tree.xpath('//*[@id="blocoValores"]/div[2]/div[1]/div/h4/text()')
                    if len(valor) != 0:
                        self.__data['Nome'].append(nome)
                        self.__data['Valor'].append(valor)
                        self.__data['Link'].append(link)
                        print(nome)
                    else:
                        contador += 1
                        if contador >= 30:
                            break

        return self.__data
    

from ScrapeKabum import scraper_kabum
import json

def str_to_float(s: str) -> float:
    final_s = s.replace("R$\\xa0", "").replace(".", "").replace(",", ".").replace(r"'", "").replace("[", "").replace("]", "")
    return float(final_s)

if __name__ == '__main__':
    s: scraper_kabum = scraper_kabum("Product_Name")
    links: list[str] = s.get_all_pages()
    # links: list[str] = list() 
    # with open('links_PRODUCT_NAME_Kabum.txt', 'r') as f:
        # links = (f.read()).split('\n')
# Tire os comentários se você já tem um arquivo com os links^
    with open('links_PRODUCT_NAME_Kabum.txt', 'w') as f:
       for link in links:
            f.write(f'{link}\n')
#Coloque comentários nas linhas 15, 16 e 17 se você já tem um arquivo com os links^


            
    data: dict[str, list[str | float]] =  s.get_pages_contents(links)
    for i in range(len(data['Valor'])):
          data['Valor'][i] = str_to_float(str(data['Valor'][i]))
          data['Nome'][i] = str(data['Nome'][i]).replace(r"'", "").replace("[", "").replace("]", "")
          data['Link'][i] = str(data['Link'][i]).replace(r"'", "").replace("[", "").replace("]", "")
    with open('product_name_kabum.json', 'w') as f:
                f.write(json.dumps(data))
    
    

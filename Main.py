from ScrapeKabum import ScraperKabum
import json

def str_to_float(s: str) -> float:
    final_s = s.replace("R$\\xa0", "").replace(".", "").replace(",", ".").replace(r"'", "").replace("[", "").replace("]", "")
    return float(final_s)

if __name__ == '__main__':
    s: ScraperKabum = ScraperKabum("Product_Name")
    links: list[str] = s.get_all_pages() #Comment this if you have a links file already
    # links: list[str] = list() 
    # with open('links_PRODUCT_NAME_Kabum.txt', 'r') as f:
        # links = (f.read()).split('\n')
# Uncomment to run a file that already has all the links you want ^
    with open('links_PRODUCT_NAME_Kabum.txt', 'w') as f:#Comment this if you have a links file already
       for link in links: #Comment this if you have a links file already
            f.write(f'{link}\n') #Comment this if you have a links file already


            
    data: dict[str, list[str | float]] =  s.get_pages_contents(links)
    for i in range(len(data['Valor'])):
          data['Valor'][i] = str_to_float(str(data['Valor'][i]))
          data['Nome'][i] = str(data['Nome'][i]).replace(r"'", "").replace("[", "").replace("]", "")
          data['Link'][i] = str(data['Link'][i]).replace(r"'", "").replace("[", "").replace("]", "")
    with open('product_name_kabum.json', 'w') as f:
                f.write(json.dumps(data))
    
    

from ScrapeKabum import ScraperKabum
import json

if __name__ == '__main__':
    s: ScraperKabum = ScraperKabum("placa-de-video", multiprocessing=False)
    links: list[str] = s.get_all_pages() #Comment this if you have a links file already
    # links: list[str] = list() 
    # with open('links_GPU_Kabum.txt', 'r') as f:
        # links = (f.read()).split('\n')
# Uncomment to run a file that already has all the links you want ^
    with open('links_GPU_Kabum.txt', 'w') as f:#Comment this if you have a links file already
        for link in links: #Comment this if you have a links file already
            f.write(f'{link}\n') #Comment this if you have a links file already
            
    data: dict[str, list[str | float]] =  s.get_page_contents(links)
    with open('gpu_kabum.json', 'w') as f:
                f.write(json.dumps(data))
    

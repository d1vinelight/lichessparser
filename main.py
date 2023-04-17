import requests
from bs4 import BeautifulSoup as bs
import os

a = [] #преобразовать данные из цикла ниже в список чтобы получить упорядоченные строки
url = 'https://lichess.org/tournament' #источник данных


def tournaments_name():
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    tournaments = soup.find_all('span', class_ = 'name') 
    for i in tournaments:
        a.append(i.text + '\n')
        
    
        
           
    with open("tournamentsname.txt", "w", encoding = 'utf-8') as file:   #работа с файлом: открытие, запись данных, закрытие
        file.write(''.join(a))
    file.close()
    
    
    os.startfile('C:\\Users\\1\\venv\\tournamentsname.txt')


    
def main():
    tournaments_name()
   
    
if __name__ == '__main__':
    main()

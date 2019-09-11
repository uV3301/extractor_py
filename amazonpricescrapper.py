import pyperclip, bs4, requests

def getprice(url):
    res = requests.get(url)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #tprice = soup.select('#soldByThirdParty > span')
    oprice = soup.select('#priceblock_ourprice')
    
    #final_1 = tprice[0].text.strip()
    final_2 = oprice[0].text.strip()
    
    return final_2
    #if final_1 and final_2:
    #    return final_1+ '\n'+final_2
    #elif final_1 or final_2:
    #    return final_2
    
url = pyperclip.paste()
print('The price is : ',getprice(url))
print()

    

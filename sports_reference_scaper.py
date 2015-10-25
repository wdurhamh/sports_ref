import requests
import sys
from parser import SportsRefParser

base_url = "http://sports-reference.com/cbb/players/"

def get_web_page(url):
	response = requests.get(url)
	return response

def get_possible_urls(name):
	#try variationson the base
	possible_urls = []
        possible_urls.append( base_url + name + "-1.html" )
        return possible_urls
"""Takes a response object as defined by the 'requests' import"""
def parse_page(response):
    parser = SportsRefParser(response)
    


if __name__ == "__main__":
    print sys.argv
    player_name = "-".join(sys.argv[1:])
    print player_name
    possible_urls = get_possible_urls(player_name)
    for url in possible_urls:
        response = get_web_page(url)
        if response.status_code == 200:
            parse_page(response) 

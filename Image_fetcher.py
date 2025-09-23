import requests
import os
from urllib.parse import urlparse


def download(url):
    try:
        #Creating a directory where the downloaded images will be saved in the local storage.
        os.makedirs('Downloaded', exist_ok = True)
        
        #Fetching the images from the web
        response = requests.get(url, timeout = 10)
        
        #raise exception for bad image url
        response.raise_for_status()
        
        #Extract file name from the downloaded image
        url_parse = urlparse(url)
        filename = os.path.basename(url_parse.path)
        
        #attach name if the download image  does not have a name
        if not filename:
            filename = 'downloaded_image'
           
         #save the file 
        filepath = os.path.join('Downloaded', filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print('fSuccessfully fetched {filename}.')
            print(f'Image saved to {filepath}')
            print('\n Connection strengthened. Community enriched.')
            
    except requests.exceptions.RequestException as e:
        print(f'Connection error: {e}')  
        
    except Exception as e:
        print(f'An error occurred: {e}')
       
       
def main():
    #Welcome messages
    print('Welcome to the Ubuntu Image Fetcher.')
    print('A tool for mindfully collecting images from the web \n')
    
    #prompting the user for urls separated by comma
    urls = input('Enter url separated by comma. \n').split(' , ')
    
    #Looping through the urls entered byvthe user and passing them to the download function
    for url in urls:
        download(url.strip())
        
        
if __name__ == '__main__':
    main()
    
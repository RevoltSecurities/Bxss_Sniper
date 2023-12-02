#!/usr/bin/python3
import httpx 
import os  
from colorama import Fore,Back,Style
import argparse
import concurrent.futures 
import requests
import logging 
import time as t
import random
import yaml
import sys 



"""
MIT License

Copyright (c) 2023 Sanjai kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)

payloads = []

urls_list = []

requests.packages.urllib3.disable_warnings()


logging.basicConfig(level=logging.INFO, format="%(message)s")

logging.getLogger("httpx").setLevel(logging.WARNING)

logging.getLogger("requests").setLevel(logging.WARNING)



banner = f"""{bold}{random_color} 

    ____                    _____       _ ____           
   / __ )_  ____________   / ___/____  (_) __ \___  _____
  / __  | |/_/ ___/ ___/   \__ \/ __ \/ / /_/ / _ \/ ___/
 / /_/ />  <(__  |__  )   ___/ / / / / / ____/  __/ /    
/_____/_/|_/____/____/   /____/_/ /_/_/_/    \___/_/     
                                                         
  
{reset} 
 
            {bold}{white}Author : D.Sanjai Kumar @CyberRevoltSecurities{reset}
            
            {bold}{white}Source Idea: Jerry {reset} """
            


parser = argparse.ArgumentParser(description=f"[{bold}{blue}DESCRIPTION{reset}]: {bold}{white}Bxss Sniper: A web application penetration testing tool for Blind XSS detection")

parser.add_argument("-uf", "--urls-file", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}A file that contains list of url to test for blind cross site scripting{reset}", type=str)

parser.add_argument("-u", "--url", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}A single url to test for blind cross site scripting ", type=str )

parser.add_argument("-s", "--silent", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Silently print only output and not print the banner and version", action="store_true")

parser.add_argument("-o", "--output", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Filename to write the output ", type=str)

parser.add_argument("-px", "--proxy", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Switiching proxy will send request to your configured proxy (eg: BURPSUITE)", type=str)

parser.add_argument("-to", "--time-out", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Switiching timeout will requests till for your timeout and also for BURPSUITE", type=int)

parser.add_argument("-c", "--concurrency", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Concurrency level for Multiple process {reset}", type=int, default=10)

args = parser.parse_args()






def get_version():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Bxss_Sniper/releases/latest"
    
    try:
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                message = "latest"
                
                logging.info(f"[{blue}Version{reset}]: {bold}{white}Bxss Sniper current version {version} ({green}{message}{reset}){reset}")
                
                t.sleep(1)
                
            else:
                
                message ="outdated"
                
                logging.info(f"[{blue}Version{reset}]: {bold}{white}Bxss Sniper  current version {version} ({red}{message}{reset}){reset}")
                
                t.sleep(1)
                
        else:
            
            pass
        
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass 
    
def check_config_file():
    
    filename = "bxss-config.yaml"
    
    path = "/"
    
    for root,dirs,files in os.walk(path):
        
        if filename in files:
            
            file_path = os.path.join(root, filename)
            
            logging.info(f"[{bold}{blue}INFO{reset}]: {bold}{white}Loading the configuration file from {file_path}{reset}")
            
            return file_path
        
    logging.info(f"[{bold}{red}ALERT{reset}]: {bold}{white}Configuration Payloads File not found please kindly install the  {filename} file{reset}")
    
    exit()
    

    
def read_keys(filename) :
    
    try: 
        
        
        
        with open(filename, "r") as keys:
            
            data = yaml.safe_load(keys)
            
                
        temp_payloads = data.get("BlindXSS-Payloads", [])
        
        if temp_payloads is not None:
        
        
            for payload in temp_payloads:
            
                payloads.append(payload)
                
        else:
            
            logging.info(f"[{bold}{blue}INFO{reset}]: {bold}{white}Please atleast provide 1 payload{reset}")
            
            exit()
        
    
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass
        
def IShowSpeed():
    
    
    
    try:
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            
            futures = [executor.submit(bxss, url) for url in urls_list]
            
        concurrent.futures.wait(futures)
        
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass  
        
def bxss(url) :
    
    try: 
        
        
        
        
        proxies = {
            
            "http": f"{args.proxy}",
            "https": f"{args.proxy}"
        } if args.proxy else None
        
        timeout = args.time_out if args.time_out else 10
        
        url = f"https://{url}" if not url.startswith("https://")  and  not url.startswith("http://") else url
        
        for payload in payloads:
            
            referer = payload
            
            user_agent = payload
            
            x_forwarded_for = payload
            
            accept = payload
                    
                
            headers = {
                        "Referer": referer,
                        "User-agent": user_agent,
                        "X-forwarded-for": x_forwarded_for,
                        "Accept": accept
                    }

        
            
            
            response = requests.get(url, headers=headers, timeout=timeout, proxies=proxies, verify=False)
                
            
            if response.status_code is not None:
            
                logging.info(f"[{bold}{green}INFO{reset}]: {bold}{cyan}REQUEST{reset}: {bold}{white}Success |{reset} {bold}{blue}URL{reset}: {bold}{white}{url}  |{reset} {bold}{green}CODE{reset}: {bold}{white}{response.status_code}{reset}")
                
                save(url, response.status_code)
    
    except httpx.exceptions.TimeoutException:
        
        logging.info(f"time out")
           
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass
        
def save(url, code):
    
    try:
    
        if args.output:
            
            if os.path.isfile(args.output):
                
                filename = args.output
                
            elif os.path.isdir(args.output):
                
                filename = os.path.join(args.output, f"Bxss-Sniper_results.txt")
                
            else:
                
                filename = args.output
                
        if not args.output:
            
            filename = f"Bxss-Sniper_results.txt"
            
        
        with open(filename, "a") as w:
            
            w.write(f" {url} : {code} " + '\n')
            
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass
        
        
def main():
    
    try:
        
        if not args.silent:
    
            logging.info(banner)
    
            get_version()
    
        if args.url:
        
            filename = check_config_file()
        
            read_keys(filename)
        
            bxss(args.url)
        
        if args.urls_file:
            
            try:
                
                filename = check_config_file()
                
                read_keys(filename)
                
                file = args.urls_file
                
                with open(file, "r") as data:
                    
                    urls = data.read().splitlines()
                    
                for url in urls:
                    
                    urls_list.append(url)
                    
                IShowSpeed()
                
                    
            except KeyboardInterrupt as e:
        
                logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
                exit()
                
            except FileNotFoundError as e:
                
                logging.info(f"[{blue}INFO{reset}]: {bold}{white}Please check the given file {file} exists{reset}")
                
                exit()
        
                
            except Exception as e:
        
                logging.info(f"[{bold}{red}ERROR{reset}]: {bold}{white}Bxss Sniper met with error due to: {e}{reset}")
            
            
        if not args.url and not args.urls_file:
            
            try:
                
                filename = check_config_file()
                
                read_keys(filename)
                
                for line in sys.stdin:
                      
                      url = line.strip()
                      
                      if url.startswith("https://") or url.startswith("http://"):
                          
                             urls_list.append(url)
                      else:
                         
                          new_url = f"https://{url}"
                          
                          new_http = f"http://{url}"
                          
                          urls_list.append(new_url)
                          
                          urls_list.append(new_http)
                          
                IShowSpeed()
                          
            except KeyboardInterrupt as e:
        
                logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
                exit()
        
                
            except Exception as e:
        
                pass
                          
            
    except KeyboardInterrupt as e:
        
        logging.info(f"[{blue}INFO{reset}]: {bold}{white}Bxss Sniper says BYE!{reset}")
        
        exit()
        
                
    except Exception as e:
        
        pass
        
if __name__ == "__main__" :
    
    main()
        
        
        
        
        
        
        


    







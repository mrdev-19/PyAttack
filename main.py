version="1.0"
title=f"""
ooooooooo.                     .o.           .       .                       oooo        
`888   `Y88.                  .888.        .o8     .o8                       `888        
 888   .d88' oooo    ooo     .8"888.     .o888oo .o888oo  .oooo.    .ooooo.   888  oooo  
 888ooo88P'   `88.  .8'     .8' `888.      888     888   `P  )88b  d88' `"Y8  888 .8P'   
 888           `88..8'     .88ooo8888.     888     888    .oP"888  888        888888.    
 888            `888'     .8'     `888.    888 .   888 . d8(  888  888   .o8  888 `88b.  
o888o            .8'     o88o     o8888o   "888"   "888" `Y888""8o `Y8bod8P' o888o o888o 
             .o..P'                                                                      
             `Y8P'                                                                       
Python Ddos Script
Made with ❤️  by Dev
Github: https://github.com/mrdev-19/PyAttack
version : {version}
"""

from argparse import ArgumentParser,RawTextHelpFormatter
import requests,colorama
from termcolor import colored,cprint

def main():
    parser=ArgumentParser(
        usage='./(prog)s -t [target] -p [port] -t [threads]',
        formatter_class=RawTextHelpFormatter,
        prog='pyattack',
        description=cprint(title,'cyan',attrs=['bold']),
        epilog='''
    ./%(prog)s -d www.example.com -p 80 -T 2000 -Pyslow
    ./%(prog)s -d www.domain.com -s 100 -Request
    ./%(prog)s -d www.google.com -Synflood -T 5000 -t 10.0
'''
    )

if __name__=="__main__":
    main()
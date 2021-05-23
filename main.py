# Imports
import webbrowser
from time import sleep

print("""
\n
 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗  
██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗
 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
\n                                            
""")
# Execute
while True:
    query = input("Enter your query :\n")
    url = (f"https://www.google.com/search?q={query}")
    webbrowser.open(url)


# End

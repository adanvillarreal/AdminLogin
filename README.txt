This script gets as argument the name of the file which contains the url's/ip's to scan.
It has a list of paths which have a high probability of being the admin path. In case a path responds with a 2xx code, it will be printed in the terminal and in a .txt file named results and the date/hour of the scan. 
In case a ip/url gets stuck (happens when 5xx errors occur) and you want to finish that ip, you can CTRL^C to skip the current ip/url.

By Adan Villarreal.

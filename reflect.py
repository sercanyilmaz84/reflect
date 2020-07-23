import urllib.request, urllib.error, urllib.parse, optparse, os

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-u", "--url", dest="website_url", help= "Enter a url")
    parse_object.add_option("-n", "--name", dest="website_name", help= "Enter a name")
    options = parse_object.parse_args()[0]
    if not options.website_url:
        print("-u, you must enter an url")
    if not options.website_name:
        print("-n, you must enter a name")
    return options
 
site_info = user_input()
url = site_info.website_url
name = site_info.website_name


def clone_page():
	file = f"mkdir {name}"
	makedir = os.popen(file)
	response = urllib.request.urlopen(url)
	webContent = response.read()
	f = open(f'{name}\\{name}.html', 'wb')
	f.write(webContent)
	f.close()

if __name__ == '__main__':
	clone_page()

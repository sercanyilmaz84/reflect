import urllib.request, urllib.error, urllib.parse

menu = """

1) Facebook
2) Trendyol
3) Gmail
4) LinkedIn
5) Github
6) n11.com
7) Spotify

"""

print(menu)

m = input("Choose a page: ")


def facebook():
	response = urllib.request.urlopen('http://facebook.com')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\facebook\\facebook.html', 'wb')
	f.write(webContent)
	f.close

def trendyol():
	response = urllib.request.urlopen('http://trendyol.com/login')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\trendyol\\trendyol.html', 'wb')
	f.write(webContent)
	f.close

def gmail():
	response = urllib.request.urlopen('http://gmail.com')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\gmail\\gmail.html', 'wb')
	f.write(webContent)
	f.close

def linkedin():
	response = urllib.request.urlopen('http://linkedin.com')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\linkedin\\linkedin.html', 'wb')
	f.write(webContent)
	f.close

def github():
	response = urllib.request.urlopen('http://github.com/login')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\github\\github.html', 'wb')
	f.write(webContent)
	f.close

def n11():
	response = urllib.request.urlopen('http://www.n11.com/giris-yap')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\n11\\n11.html', 'wb')
	f.write(webContent)
	f.close

def spotify():
	response = urllib.request.urlopen('http://accounts.spotify.com/tr/login')
	webContent = response.read()
	f = open('C:\\Users\\Sercan YILMAZ\\Desktop\\reflect\\spotify\\spotify.html', 'wb')
	f.write(webContent)
	f.close






if m == "1":
	facebook()
elif m == "2":
	trendyol()
elif m == "3":
	gmail()
elif m == "4":
	linkedin()
elif m == "5":
	github()
elif m == "6":
	n11()
elif m == "7":
	spotify()
else:
	print("Incorrect input!!!")
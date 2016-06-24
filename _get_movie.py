import requests
from movie import _movie
f = open("movie.txt","w")
for line in _movie:
	data = line.split('\"')
	title = data[1]
	index1 = data[2].find('(')
	index2 = data[2].find(')')
	year = data[2][index1+1:index2]
	
	params = {"t":title,"y":year}
	r = requests.get("http://www.omdbapi.com/?",params = params)
	f.write(r.text.encode('utf-8'))



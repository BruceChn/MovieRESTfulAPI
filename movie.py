##load movie title & year from movies.list
import re
import requests
_movie = []
with open("movies.list","r") as f:
	for line in f:
		res = re.findall("\".+\"\s\([0-9]+\)",line)
		if len(res) != 0:
			if len(_movie) == 0 or res[0] != _movie[-1]:
				_movie.append(res[0])




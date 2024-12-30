def tour(x):
	x2 = x*7+1
	x2 = x2*7-4
	return x2

def dix_tour(x):
	return tour(tour(tour(tour(tour(tour(tour(tour(tour(tour(x))))))))))

def itour(x):
	x2 = (x+4)/7
	x2 = (x2-1)/7
	return x2

def idix_tour(x):
	return itour(itour(itour(itour(itour(itour(itour(itour(itour(itour(x))))))))))
from math import sqrt

a = [0.00456703785903, 0.280007197012, 0.37518855383, 0.521976363726, 0.544473640615, 0.630810250115, 0.640421131161, 0.655661125564, 0.679855573868, 0.687560912338, 0.694223076919, 0.734565579714, 0.775292787906, 0.781918967685, 0.782764505781, 0.790847226334, 0.829771608862, 0.886514211629, 0.919523867511, 0.935381274266]
b = []
for x in a:
	p = x
	q = 1-p
	b.append(2.0*q*p)
p = ""
for x in b:
	p += str(x) + " "
print(p)
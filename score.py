import os
import csv
import math
def rootcenter(csvfileinput):
	with open(csvfileinput) as csvfile:
		coord_array = []
		coord_reader = list(csv.DictReader(csvfile))
		for c in coord_reader:
			for  key,value in c.items():
				c[key] = float(c[key])
				if not key=='thorax_x' and not key=='thorax_y':
					if key[-1]=='x':
						c[key]-=float(c['thorax_x'])
					if key[-1]=='y':
						c[key]-=float(c['thorax_y'])
		return(coord_reader)
def scorevid(source,target):
	c = ["left_shoulder","right_shoulder"]
	s_coord = rootcenter(source)
	t_coord = rootcenter(target)
	t_dist = math.sqrt( (t_coord[0][c[0]+"_x"] - t_coord[0][c[1]+"_x"])**2 + (t_coord[0][c[0]+"_y"] - t_coord[0][c[1]+"_y"])**2 )
	s_dist = math.sqrt( (s_coord[0][c[0]+"_x"] - s_coord[0][c[1]+"_x"])**2 + (s_coord[0][c[0]+"_y"] - s_coord[0][c[1]+"_y"])**2 )
	print('t',t_dist,'s',s_dist)
	scalar = t_dist/s_dist
	print('scalar',scalar)
	diff_total = 0
	for t in range(len(t_coord)):
		for item in t_coord[t].items():
			if any([True for name in ["wrist","elbow","pelvis","ankle"] if name in item[0]]):
				diff_total += abs(item[1]-scalar*s_coord[t][item[0]])
	return(diff_total)

import matplotlib.pyplot as plt 

fig, ax = plt.subplots()

ax.set_xlim((0, 4000000))
ax.set_ylim((0, 4000000))
mylist = [((325337,2568863), 1412861), 
	((3988825,837820), 1606121), 
	((1611311,2053174), 1689579), 
	((101890,3940049), 1336117), 
	((3962702,2558425), 310580), 
	((2957890,2160813), 711967), 
	((3907456,3325610), 310472), 
	((3354177,3435919), 551590), 
	((3997379,3071868), 455663), 
	((145143,1714962), 948842), 
	((611563,3148864), 652559), 
	((3080405,3904777), 1294220), 
	((644383,10732), 585057), 
	((3229566,1694167), 516997), 
	((1600637,3984884), 1172535), 
	((2959765,2820860), 545279), 
	((2235330,3427797), 786093), 
	((2428996,210881), 1766859), 
	((369661,687805), 987408), 
	((3558476,2123614), 750676), 
	((3551529,2825104), 545961), 
	((64895,3577), 597894), 
	((3079531,1538659), 293156)]

# mylist = [((2,18), 7), 
# 			((9,16), 1), 	
# 			((13,2), 3), 
# 			((12,14), 4), 
# 			((10,20), 4), 
# 			((14,17), 5), 
# 			((8,7), 9), 
# 			((2,0), 10), 
# 			((0,11), 3), 
# 			((20,14), 8), 
# 			((17,20), 6), 
# 			((16,7), 5), 
# 			((14,3), 1), 
# 			((20,1), 7)]
# ax.set_xlim((0, 20))
# ax.set_ylim((0, 20))


colors = ['b', 'g', 'y', 'r', 'c', 'm', 'k']
for index, row in enumerate(mylist):
	print(row)
	(i, j), distance = row
	point1 = [i+distance, j]
	point2 = [i, j+distance]
	point3 = [i-distance, j]
	point4 = [i, j-distance]
	x_values = [point1[0], point2[0], point3[0], point4[0], point1[0]]
	y_values = [point1[1], point2[1], point3[1], point4[1], point1[1]]
	plt.plot(x_values, y_values, colors[index % len(colors)], linestyle="--")


# ax.add_artist(circle)
# circle = plt.Circle((3988825,837820), 1606121, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((1611311,2053174), 1689579, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((101890,3940049), 1336117, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3962702,2558425), 310580, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((2957890,2160813), 711967, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3907456,3325610), 310472, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3354177,3435919), 551590, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3997379,3071868), 455663, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((145143,1714962), 948842, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((611563,3148864), 652559, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3080405,3904777), 1294220, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((644383,10732), 585057, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3229566,1694167), 516997, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((1600637,3984884), 1172535, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((2959765,2820860), 545279, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((2235330,3427797), 786093, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((2428996,210881), 1766859, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((369661,687805), 987408, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3558476,2123614), 750676, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3551529,2825104), 545961, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((64895,3577), 597894, color='b', fill=False)
# ax.add_artist(circle)
# circle = plt.Circle((3079531,1538659), 293156, color='b', fill=False)
# ax.add_artist(circle)



# # circle = plt.Circle((2,18), 7, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((9,16), 1, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((13,2), 3, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((12,14), 4, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((10,20), 4, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((14,17), 5, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((8,7), 9, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((2,0), 10, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((0,11), 3, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((20,14), 8, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((17,20), 6, color='b', fill=False)
# # ax.add_artist(circle) 
# # circle = plt.Circle((16,7), 5, color='b', fill=False)
# ax.add_artist(circle) 
# circle = plt.Circle((14,3), 1, color='b', fill=False)
# ax.add_artist(circle) 
# circle = plt.Circle((20,1), 7, color='b', fill=False)
# ax.add_artist(circle) 



# circle1 = plt.Circle((2, 18), 7, color='b', fill=False)
# circle1 = plt.Circle((x0, y0), r0, color='b', fill=False)
# circle2 = plt.Circle((x1, y1), r1, color='b', fill=False)
# circle3 = plt.Circle((x2, y2), r2, color='b', fill=False)

# ax.add_artist(circle1)
# ax.add_artist(circle2)
# ax.add_artist(circle3)

# intersections = get_intersections(x0, y0, r0, x1, y1, r1)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections 
#     plt.plot([i_x3, i_x4, [i_y3, i_y4, '.', color='r')
    
# intersections = get_intersections(x0, y0, r0, x2, y2, r2)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections 
#     plt.plot([i_x3, i_x4], [i_y3, i_y4], '.', color='r')

# intersections = get_intersections(x1, y1, r1, x2, y2, r2)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections 
#     plt.plot([i_x3, i_x4], [i_y3, i_y4], '.', color='r')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
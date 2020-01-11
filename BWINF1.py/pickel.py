import pickle
the_line = []
with open('/Users/alexgalkin/Documents/competitive/BWINF1.py/banner.p' ,'rb') as pickle_file:
    new_data = pickle.load(pickle_file)
#print(new_data)
for row in new_data:
    the_line = []
    for pos in row:
        the_line.append(pos[0]*pos[1])
    print("".join(the_line))

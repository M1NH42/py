# ABOUT : This program deals with the writing of the .csv files using
#         python 3 code as shown

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

out_file = open("reduced_olympics.csv", "w")

# output the header row
out_file.write('Name, Age, Sport')

out_file.write('\n')

# output each row of the file
for olympian in olympians :
    row_string = '{}, {}, {}'.format(olympians[0], olympians[1], olympians[2])
    #row_string = ','.join([olympians[0], olympians[1], olympians[2]])
    out_file.write(row_string)
    out_file.write('\n')
#print(out_file)

out_file.close()
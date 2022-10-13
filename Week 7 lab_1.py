#Lucas Riebe
#CS101L
#section 4
#lab 7
#10/12/22

#function to write to output file
def print_to_file(year, make, model, mpg):

    out_file = open('output.txt', 'w')
#loop to write each line to output file    
    for i in range(len(year)):
        #print("{:>5}{:>10}".format(year,make))
        #print(year[i],make[i],model[i],mpg[i])
        out_file.write("{:<6}{:<10}{:<20}{:>4}\n".format(year[i],make[i],model[i],mpg[i]))
        out_file.close


#initilizing lists  
year = []
make = []
model = []
mpg = []

#loop to validate user min mpg entry
while True:
#try and except block to take care of valueError
    try:
        mpg_thresh = input('Enter in a minimum mpg\n')

       
        if int(mpg_thresh) < 0 or int(mpg_thresh) > 100:
            raise ValueError('Invalid MPG. Please enter a number between 0 and 100')
        else:
            break
    except ValueError as excpt:
        print(excpt)
#loop and try except block to validate user entry for input file
while True:
    try:
        in_file = input('Enter name of input vehicle file\n')
        if open(in_file) == FileNotFoundError:
            raise FileNotFoundError('Please enter a valid file name')
        else:
            break
    except FileNotFoundError as excpt:
            print(excpt)

   
#try block to validate combndmpg value can be converted to int
try:
    myfile = open(in_file)
    f = myfile.readlines()
    for i in range(len(f)):
        if i != 0:
            q = f[i].split('\t')
            if int(q[7]) > int(mpg_thresh):
                year.append(q[0])
                make.append(q[1])
                model.append(q[2])
                mpg.append(q[7])
    
except ValueError:
    print(f'Could not convert value invalid for vehicle {q[0]} {q[1]} {q[2]}')        

#call to fxn to print to output file
print_to_file(year, make, model, mpg)
myfile.close()

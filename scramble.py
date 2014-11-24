def file_length(in_filename):
    '''
    (file) -> integer

    the function takes a file input 'in_filename' and returns

    an integer 'count' which is the number of lines in the file
    '''
    
    file_object = open(in_filename)
    count = 0

    for line in file_object:
        count += 1

    file_object.close()

    return count


def scramble(in_filename, out_filename):
    '''
    (file,file) 

    the function takes an input file 'in_filename' and output filename

    'out_filename' and writes a scrambled version of 'in_filename' to the

    output file with original line numbers appened to the front of each line.
    '''

    import linecache
    import random

    size = file_length(in_filename)
    file_object_in = open(in_filename)
    file_object_out = open(out_filename, "w")
    rand_num = [0] * size

    for k in range(size):  # makes a list of length of file (lines)
        rand_num[k] = k + 1

    random.shuffle(rand_num)  # shuffles list (random)

    for i in range(size):  # for loop for writing to output file
        file_object_out.write(str(rand_num[i]) + ":")
        file_object_out.write(linecache.getline(in_filename, rand_num[i]))

    file_object_in.close()
    file_object_out.close()

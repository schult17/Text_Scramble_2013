def file_length(in_filename):
    '''
    (file) -> integer

    the function takes a file input 'in_filename' and returns an integer

    'count' which is the number of lines in the file
    '''

    file_object = open(in_filename)
    count = 0

    for line in file_object:
        count += 1

    file_object.close()

    return count


def descramble(in_filename, out_filename):
    '''
    (file,file) 

    the function takes an input file 'in_filename' and output filename

    'out_filename'. The function descrambles the 'in_filename' and writes

    the descrambled version to 'out_filename'
    '''
    
    import linecache
    
    file_object_in = open(in_filename)
    file_object_out = open(out_filename, "w")
    size = file_length(in_filename)
    scram_list = []

    for line in file_object_in:  # for loop to make list of scrambled order
        a = int(line.split(":")[0])
        scram_list.append(a)

    order_list = [0]*max(scram_list)

    for k in range(0, max(scram_list)):
        order_list[k] = k + 1

    for i in range(size):  # for for writing lines to output file 
        if order_list[i - 1] in scram_list:  # if number is in both list do code
            line_index = scram_list.index(order_list[i]) + 1
            write = linecache.getline(in_filename, line_index)
            write2 = write.split(":")[1]
            file_object_out.write(write2)
    
        file_object_out.write("\n")

    file_object_in.close()
    file_object_out.close()

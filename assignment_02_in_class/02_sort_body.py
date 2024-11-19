def sort_lines(input_file, output_file):
    # open the input file and read all lines
    with open(input_file, 'r') as f:
        lines=f.readlines()

    # seperate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[:2]
    body = lines[2:]

    # sort the remaining lines by the first character if 0 (case-insensitive)
    sorted_body = sorted(body, key=lambda line: line[0].lower(), reverse=True)

    # you want to sort the file not reversed, just delete the ', reverse=True' ^

    # combine the header and sorted body
    sorted_lines = header + sorted_body

    # write the result to the output file
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# specify input and output file names
input_file='markdown_list_unsorted.md'
output_file = '02_results.md'

#call the function to sort lines
sort_lines(input_file, output_file)
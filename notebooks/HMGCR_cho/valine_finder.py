import json

def get_valine_header(header_line):
    sections = header_line.split('|')
    return sections[2]

def get_family_string(header_line):
    sections = header_line.split('|')
    family_string = sections[3]
    return family_string.replace('.','')

def get_valine_positions(sequence_line, positions):
    valine_positions = []
    for position in positions:
        if len(sequence_line) > position:
            valine_positions.append(sequence_line[position])
        else:
            valine_positions.append('-')
    return valine_positions

def valine_finder(fileObj, positions):
    valines=[]
    for count, line in enumerate(fileObj, start=1):
        if count % 2 == 0:
            valines.append({ f"{get_valine_header(prev_line)}": {"lineage": get_family_string(prev_line), "notible_valines": get_valine_positions(line, positions)}})
        else:
            prev_line = line
    return valines


if __name__ == "__main__":
    default_positions= [17, 22, 91, 96, 585, 590, 740, 745]
    input_file = open("HMGCRCTERM-aligned_processed.fasta", "r")
    valines = valine_finder(input_file, default_positions)
    output_file = open("HMGCRCTERM-notible-valines.csv", "w")
    output_file.write("Common Name, Lineage")
    for position in default_positions:
        output_file.write(f",Notible Valine at Postition {position}")
    output_file.write('\n')
    for valine in valines:
        keys = list(valine.keys())
        common_name = keys[0]
        nested_obj = valine.get(common_name)
        lineage = nested_obj.get('lineage').replace(",", "->").strip("\n")
        output_file.write(f"{common_name}, {lineage},{','.join(nested_obj.get('notible_valines'))}")
        output_file.write('\n')
    input_file.close()
    output_file.close()
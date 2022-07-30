import argparse

parser = argparse.ArgumentParser(description='Split provided file into sequence and idlist files')
parser.add_argument('input', type=str,
                    help='absolute or local path to input file')
parser.add_argument('id_output', type=str,
                    help='absolute or local path to output idlist file')
parser.add_argument('seq_output', type=str,
                    help='absolute or local path to output sequence file')
parser.add_argument(
    "-i",
    "--input_delimiter",
    dest="input_delimiter",
    default=">",
    help="delimiter for fields in provided input files. Expected at the beginning of each id/seq block",
)
parser.add_argument(
    "-o",
    "--output_delimiter",
    dest="output_delimiter",
    default="\n",
    help="delimiter for fields for generated output files.",
)

args = parser.parse_args()

id_list = []
seq_list = []
with open(args.input, 'rt') as input_file:
    input_text = input_file.read()

id_seq_list = input_text.split(args.input_delimiter)
id_seq_list.pop(0) #remove the first entry as it is always empty
for id_seq in id_seq_list:
    curr_id_seq_lines = id_seq.splitlines()
    id_list.append(curr_id_seq_lines[0].split()[0])
    seq_list.append(''.join(curr_id_seq_lines[1:]))

with open(args.id_output, 'wt') as output_id_file:
    output_id_file.write(args.output_delimiter.join(id_list))

with open(args.seq_output, 'wt') as output_seq_file:
    output_seq_file.write(args.output_delimiter.join(seq_list))
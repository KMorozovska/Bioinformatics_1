import sys
from prepare_files import *
from NeddlemanWunschMatrix import *

if len(sys.argv) < 5:
    print("Please add necessary path arguments (seq_1.txt, seq_2.txt, config.txt, output.txt")


seq_1_path = sys.argv[1]
seq_2_path = sys.argv[2]
config_path = sys.argv[3]
output_path = sys.argv[4]

config = import_config(config_path)
seq_1, seq_2 = import_sequences(seq_1_path, seq_2_path, int(config['max_seq_length']))

NW_table = NeedlemanWunschMatrix(config, seq_1, seq_2)

create_output(NW_table, output_path)

print("Done")



import sys
from import_files import *
from nw_algorithm import *

seq_1_path = sys.argv[1]
seq_2_path = sys.argv[2]
config_path = sys.argv[3]

config = import_config(config_path)
seq_1, seq_2 = import_sequences(seq_1_path, seq_2_path)


fill_table(config['GAP'], config['SAME'], config['DIFF'], seq_1, seq_2)



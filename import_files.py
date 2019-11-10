def import_config(filepath):
    config_content = {}

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            config_content[line.split("=", 1)[0].strip()] = line.split("=", 1)[1].strip()
            line = fp.readline()

    # add verification

    return config_content


def import_sequences(seq_1_path, seq_2_path):
    with open(seq_1_path, "r") as text_file:
        seq_1 = text_file.read()

    with open(seq_2_path, "r") as text_file:
        seq_2 = text_file.read()

    seq_1 = seq_1.replace('\n', '')
    seq_2 = seq_2.replace('\n', '')

    return seq_1, seq_2


def create_output(NW_table, path):
    pass

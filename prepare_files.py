import sys

def import_config(filepath):
    config_content = {}

    with open(filepath) as fp:
        line = fp.readline().lower()
        while line:
            config_content[line.split("=", 1)[0].strip()] = line.split("=", 1)[1].strip()
            line = fp.readline().lower()

    validate_config('same', config_content)
    validate_config('diff', config_content)
    validate_config('gap', config_content)
    validate_config('max_seq_length', config_content)
    validate_config('max_number_paths', config_content)

    return config_content


def validate_config(str_, dict_):
    if str_ not in dict_:
        print("Missing argument in config_content: " + str_)
        sys.exit()


def validate_seq(str_, condition, id):
    if len(str_) > condition:
        print("Sequence too long! seq_" + id)
        sys.exit()


def import_sequences(seq_1_path, seq_2_path, cond):
    with open(seq_1_path, "r") as text_file:
        seq_1 = text_file.read()

    with open(seq_2_path, "r") as text_file:
        seq_2 = text_file.read()

    validate_seq(seq_1, cond, "1")
    validate_seq(seq_2, cond, "2")

    seq_1 = seq_1.replace('\n', '')
    seq_2 = seq_2.replace('\n', '')

    return seq_1, seq_2


def create_output(NW_table, path):
    print("Writing results to file..")

    with open(path, "w") as text_file:
        text_file.write("SCORE = " + str(NW_table.final_score))
        text_file.write("\n\n")
        text_file.write(NW_table.output)


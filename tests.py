from import_files import *
from needlemanwunsch import *


def test_import_config(filename):
    # given

    # when
    result = import_config(filename)
    # then
    if len(result) == 5:
        return "Ok"
    else:
        return "Error reading config file"



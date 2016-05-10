and_dict = {}
or_dict = {}
not_dict = {}
impl_dict = {}

def initialize_logic(filenames):
    """
        Creates logical functions that use a dictionary
        The functions read the desirable logical rules from supplied
        filenames and create key value pairs "bool1bool2" : "desiredresult"
        for each possible combination of input logical values

        For example if in a file it is specified that 1 and 0 -> 0, 0 and 0 -> 1
        then and_dict["10"] == "0", and_dict["00"] == "1"

        Poor man's pattern matching basically
    """
    with open(filenames['and'], 'r') as fIn:
        for line in fIn:
            line = line.strip().replace(' ', '')
            and_dict[line[:2]] = line[2:]
    with open(filenames['or'], 'r') as fIn:
        for line in fIn:
            line = line.strip().replace(' ', '')
            or_dict[line[:2]] = line[2:]
    with open(filenames['impl'], 'r') as fIn:
        for line in fIn:
            line = line.strip().replace(' ', '')
            impl_dict[line[:2]] = line[2:]
    with open(filenames['not'], 'r') as fIn:
        for line in fIn:
            line = line.strip().replace(' ', '')
            not_dict[line[:1]] = line[1:]

def custom_and(bool1, bool2):
    return and_dict.get(bool1 + bool2, "LOGIC_ERROR")


def custom_or(bool1, bool2):
    return or_dict.get(bool1 + bool2, "LOGIC_ERROR")

def custom_not(bool1):
    return not_dict.get(bool1, "LOGIC_ERROR")

def custom_impl(bool1, bool2):
    return impl_dict.get(bool1 + bool2, "LOGIC_ERROR")

def custom_xor(bool1, bool2):
    """
        a xor b == (a or b) and ~(a and b)
    """
    return and_dict.get(
            custom_or(bool1, bool2) + custom_not(custom_and(bool1, bool2)),
            "LOGIC_ERROR"
           )
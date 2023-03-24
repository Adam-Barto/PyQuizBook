def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return {k: v for (k, v) in zip(keys, values)}


def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    return d1 | d2


def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    #
    return {v: d1 for v in lst}


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    return {k: datadict[k] for k in keylist}  # datadict.get(k) also works


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    val = {datadict.pop(k) for k in keylist}
    return datadict


def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return False if list(datadict.values()).count(key) == 0 else True


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key=ddd.get)


def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key=ddd.get)

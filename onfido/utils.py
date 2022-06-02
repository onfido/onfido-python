
def form_data_converter(data):
    """ Flat nested dictionary and stringify booleans for form-data """

    # If no dict or booleans among values, no conversion needed
    if not any(type(item) in (dict, bool) for item in data.values()):
        return data

    result = {}

    # Perform needed conversion for each
    for k, v in data.items():
        if isinstance(v, dict):
            for child_k, child_v in v.items():
                result['{}[{}]'.format(k, child_k)] = child_v
        elif isinstance(v, bool):
            result[k] = str(v).lower()
        else:
            result[k] = v

    return result

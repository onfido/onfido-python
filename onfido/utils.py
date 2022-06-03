
def form_data_converter(data):
    """ Flat nested dictionary and stringify booleans for form-data """

    def _converter(data, result, prefix=''):
        if isinstance(data, dict):
            for k, v in data.items():
                pref = '{}[{}]'.format(prefix,k) if prefix else k
                _converter(v, result, pref)
        elif isinstance(data, bool):
            result[prefix] = str(data).lower()
        else:
            result[prefix] = data

    # If no dict or booleans among values, no conversion needed
    if not any(isinstance(item, dict) or isinstance (item, bool) for item in data.values()):
        return data

    result = {}
    _converter(data, result)

    return result


def flat_nested_dict(data):
    """ Flat nested dictionary """

    # Check if any value is a dictionary
    if any(type(item) is dict for item in data.values()):

        # Start copying not nested values
        result = {k: v for k, v in data.items() if type(v) is not dict}

        # And add nested ones with proper format
        for root_k, root_v in data.items():
            if type(root_v) is dict:
                for k, v in root_v.items():
                    result['{}[{}]'.format(root_k, k)] = v

        return result
    else:
        return data

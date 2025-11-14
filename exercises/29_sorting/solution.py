"""Exercise 29: Sorting"""
def sort_by_value(items):
    return sorted(items)

def sort_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])

def sort_descending(items):
    return sorted(items, reverse=True)

def sort_by_confidence(predictions):
    """Sort predictions by confidence score descending"""
    return sorted(predictions, key=lambda x: x.get('confidence', 0), reverse=True)

def sort_by_multiple_keys(items, keys):
    """Sort by multiple keys in order"""
    from operator import itemgetter
    return sorted(items, key=itemgetter(*keys))

def in_place_sort(items):
    """Sort list in place"""
    items.sort()
    return items

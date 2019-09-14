

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str) or not skus:
        return -1

    skus = skus.lower()
    selectedItems = skus.split(',')

    totalprice = 0

    for selected_item in selectedItems:
        totalprice = totalprice + items[selected_item]['price']

    totalprice = _check_offers(selectedItems, totalprice)
    return totalprice

def _check_offers(skus, totalprice):
    unique_items = list(set(skus))
    for uitem in unique_items:
        if (uitem in offers):
            offer_threshold = offers[uitem]['quantity']
            offer_count = round(skus.count(uitem) / offer_threshold)
            if offer_count > 0:
                for i in range(offer_count):
                    original_cost = items[uitem]['price'] * offer_threshold
                    offer_cost = offers[uitem]['price']
                    totalprice -= original_cost % offer_cost
    return totalprice

def _check_valid_input(skus):
    if not skus:
        return -1
    if not isinstance(skus, str):
        return -1

    skus = skus.split(',')
    if not skus:
        return -1
    
    for item in skus:
        if item not in items:
            return -1



items = {
        "a":{
            "price": 50,
        },
        "b":{
            "price": 30,
        },     
        "c":{
            "price": 20
        },
        "d":{
            "price": 20
        },                
}

offers = {
    'a': {
        "quantity": 3,
        "price": 130
    },
    "b": {
        "quantity": 2,
        "price": 45
    }
}




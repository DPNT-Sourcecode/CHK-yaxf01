
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if _check_valid_input(skus) == False:
        return -1

    totalprice = 0  
    if not skus:
        totalprice

    selectedItems = list(skus)


    for selected_item in selectedItems:
        totalprice = totalprice + items[selected_item]['price']

    totalprice = _check_offers(selectedItems, totalprice)
    return totalprice

def _check_offers(skus, totalprice):
    unique_items = list(set(skus))
    for uitem in unique_items:
        if (uitem in offers):
            offer_threshold = offers[uitem]['quantity']
            offer_count = int(skus.count(uitem) / offer_threshold)
            if offer_count > 0:
                for i in range(offer_count):
                    original_cost = items[uitem]['price'] * offer_threshold
                    offer_cost = offers[uitem]['price']
                    totalprice -= original_cost % offer_cost
    return totalprice

def _check_valid_input(skus):
    if not isinstance(skus, str):
        return False

    skus = list(skus)

    for item in skus:
        if item not in items:
            return False



items = {
        "A":{
            "price": 50,
        },
        "B":{
            "price": 30,
        },     
        "C":{
            "price": 20
        },
        "D":{
            "price": 15
        },                
}

offers = {
    'A': {
        "quantity": 3,
        "price": 130
    },
    "B": {
        "quantity": 2,
        "price": 45
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    selectedItems = skus.split(',')
    totalprice = 0

    for selected_item in selectedItems:
        totalprice = totalprice + items.get(selected_item)['price']

    return totalprice


def _check_offers(skus, totalprice):
    unique_items = list(set(skus))
    for uitem in unique_items:
        if (uitem in offers):
            offer_threshold = offers[uitem]['quantity']
            offer_count =  skus.count(uitem) % offer_threshold


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
            "price": 20
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


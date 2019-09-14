

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    selectedItems = skus.split(',')
    selectedItems = sorted(selectedItems)
    totalprice = 0

    for selected_item in selectedItems:
        totalprice = totalprice + items.get(selected_item)['price']

    return totalprice


def check_offers(sorted_skus):
    no_offers = False
    price = 0
    while no_offers == False:
        if sorted_skus.count('A') >= items.get('A')["offer"]["threshold"]


items = {
        "A":{
            "price": 50,
            "offer" : {
                "threshold": 3,
                "price": 130
            }
        },
        "B":{
            "price": 30,
            "offer" : {
                "threshold": 2,
                "price": 45
            }
        },     
        "C":{
            "price": 20
        },
        "D":{
            "price": 20
        },                
}




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
# from data.offers import offers_data
import sys

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(sys.path)
    if _check_valid_input(skus) == False:
        return -1

    totalprice = 0  
    if not skus:
        return totalprice

    selected_items = list(skus)
    for selected_item in selected_items:
        totalprice = totalprice + items[selected_item]['price']

    unique_items = list(set(skus))
    eligible_items = selected_items
    #  This whole section needs refactoring, way too much going on
    # Logic should be abstracted
    for uitem in unique_items:
        available_offers = _get_available_offers(uitem)
        if available_offers:
            has_offers = True
            while has_offers:
                eligible_offers = _get_eligible_offers(available_offers, eligible_items, uitem)
                if eligible_offers:
                    saving = _get_highest_saving(eligible_offers)
                    totalprice -= saving['saving']
                    for i in range(saving['required']['quantity']):
                        eligible_items.remove(saving['required']['item'])
                    if saving['required']['item'] != saving['target']['item']:
                        eligible_items.remove(saving['target']['item'])
                else:
                    has_offers = False

    return totalprice

def _get_highest_saving(eligible_offers):
    saving = 0
    highest_offer = None;
    for k, v in eligible_offers.items():
        if v['saving'] > saving:
            highest_offer = v

    return highest_offer

def _get_eligible_offers(available_offers, eligible_items, item_id):
    eligible_offers = dict()
    for k, v in available_offers.items():
        if v['required']['item'] in eligible_items and eligible_items.count(v['required']['item']) >= v['required']['quantity']:
            eligible_offers[k] = v

    return eligible_offers

def _check_valid_input(skus):
    if not isinstance(skus, str):
        return False

    skus = list(skus)

    for item in skus:
        if item not in items:
            return False

def _get_available_offers(item_id):
    available_offers = dict()
    for k, v in offers_data.items():
        if v['target']['item'] == item_id:
            available_offers[k] = v
        
    return available_offers

items = {
        'A':{
            'price': 50,
        },
        'B':{
            'price': 30,
        },     
        'C':{
            'price': 20
        },
        'D':{
            'price': 15
        },
        'E': {
            'price': 40
        },
        'F' : {
            'price': 10
        }          
}

# This is horrible, should really be in a database or something
# Would be a good in a relationaldb 


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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
    for uitem in unique_items:
        available_offers = _get_available_offers(uitem)
        if available_offers:
            has_offers = True
            while has_offers:
                eligible_offers = _get_eligible_offers(available_offers, eligible_items, uitem)
                if eligible_offers:
                    print(uitem)
                    print(eligible_offers)
                    saving = _get_highest_saving(eligible_offers)
                    print(saving)
                    totalprice -= saving['saving']
                    for i in range(saving['quantity']):
                        print('removing' + uitem)
                        print(eligible_items)
                        eligible_items.remove(saving(saving['target_item']))
                else:
                    has_offers = False

    return totalprice

# def _check_offers(skus, totalprice):
#     unique_items = list(set(skus))
#     for uitem in unique_items:
#         if (uitem in offers):
#             offer_threshold = offers[uitem]['quantity']
#             offer_count = int(skus.count(uitem) / offer_threshold)
#             if offer_count > 0:
#                 for i in range(offer_count):
#                     original_cost = items[uitem]['price'] * offer_threshold
#                     offer_cost = offers[uitem]['price']
#                     totalprice -= original_cost % offer_cost


def _get_highest_saving(eligible_offers):
    saving = 0
    highest_offer = None;
    for k, v in eligible_offers.items():
        if v['saving'] > saving:
            highest_offer = v

    return highest_offer

def _is_offer_eligible(offer, eligible_items, item_id):
    if offer['required_item'] in eligible_items and eligible_items.count(item_id) >= offer['quantity']:
        return true
    return false

def _get_eligible_offers(available_offers, eligible_items, item_id):
    eligible_offers = dict()
    for k, v in available_offers.items():
        if v['required_item'] in eligible_items and eligible_items.count(v['required_item']) >= v['quantity']:
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
    for k, v in offers.items():
        if v['target_item'] == item_id:
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
        }             
}

offers = {
    0: {
        'target_item': 'A',
        'required_item': 'A',
        'quantity': 3,
        'saving': 20
    },
    1: {
        'target_item': 'A',
        'required_item': 'A',
        'quantity': 5,
        'saving': 50
    },
    2: {
        'target_item': 'B',
        'required_item': 'B',
        'quantity': 2,
        'saving': 15
    },
    3: {
        'target_item': 'B',
        'required_item': 'E',
        'quantity': 2,
        'saving': 30
    }
}


from firebase import firebase

api = firebase.FirebaseApplication('https://hacker-news.firebaseio.com/v0/', None)

def get_topstories():
    return api.get('topstories', None)[0:2]

def get_item(id):
    return api.get("item", id)

def get_kids(item):
    if item is not None and 'kids' in item:
        return all_items(item['kids'])
    else:
        return []

def all_items(ids):
    items = []

    if len(ids) > 0:
        id = ids[0]
        try:
            item = get_item(id)
            kids = get_kids(item)
            items.append(item)
            items += kids
        except:
            print("error with item " + str(id))

        items += all_items(ids[1:])

    return items

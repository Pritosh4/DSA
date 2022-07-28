def location(cards, target, mid):
    if cards[mid]==target:
        if mid-1 > 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] > target:
        return 'right'
    elif cards[mid] < target:
        retun 'left'


def find(cards, target):
    low, high = 0, len(cards)-1
    while low <= high:
        mid = (low + high) // 2
        result=location(cards,target,mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
        return -1


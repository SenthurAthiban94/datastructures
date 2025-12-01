
def count_word_frequency(words):
    # count = {}
    # for fruit in words:
    #     if fruit in  count:
    #         count[fruit]+=1
    #     else:
    #         count[fruit]=1
    # return count
    count = {}
    for word in words:
        count[word] = count.get(word,0)+1
    return count

def merge_dicts(dict1, dict2):
    merge_dicts = dict1.copy()
    for key,value in dict2.items():
        merge_dicts[key] = merge_dicts.get(key,0)+value
    return merge_dicts

# Max value in list
def max_value_key(my_dict):
    # maxval = {"key":None, "value":0}
    # for key,value in my_dict.items():
    #     if value>maxval["value"]:
    #         maxval["value"] = value
    #         maxval["key"] = key
    # return maxval["key"]
    
    return max(my_dict,key=my_dict.get)

# reverse key value in Dict
def reverse_dict(my_dict):
    return {value:key for key,value in my_dict.items()}


# Same Frequecy in Dict
def check_same_frequency(list1, list2):
    # TODO
    def count_elem(lst):
        counter = {}
        for item in lst:
            counter[item] = counter.get(item,0)+1
        return counter
    
    return count_elem(list1)==count_elem(list2)

print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))
print(merge_dicts({"a":1,"b":2,"c":3,"d":2},{"d":2,"e":5,"f":6}))
print(max_value_key({"a":1,"b":9,"c":0}))
print(reverse_dict({"a":1,"b":9,"c":0}))
print(check_same_frequency([1,2,3,4,5],[1,2,3,4,5]))
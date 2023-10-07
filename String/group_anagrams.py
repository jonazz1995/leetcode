from collections import Counter
def groupAnagrams(strs):
    res = []
    seen = set()

    for i, word in enumerate(strs):
        if word not in seen:
            group = [word]
            seen.add(word)
            start_counter = Counter(word)

            for j in range(i + 1, len(strs)):
                if strs[j] not in seen and start_counter == Counter(strs[j]):
                    group.append(strs[j])
                    seen.add(strs[j])
        res.append(group)

    return res

strs = ["",""]

print(groupAnagrams(strs))
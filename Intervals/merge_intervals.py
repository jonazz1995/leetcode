def merge(intervals):
        
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]

    for interval in sorted_intervals[1:]:
        # If current interval overlaps with the last merged interval, merge them
        if interval[0] <= merged[-1][1]:
            merged[-1] = [merged[-1][0], max(interval[1], merged[-1][1])]
        else:
            merged.append(interval)
        
    return merged

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16], [4,8]]
print(merge(intervals))
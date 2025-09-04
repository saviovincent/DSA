def activity_selection():
    """
    given start and end time of each job, return max no of jobs that can be completed by 1 person
    :return:
    """
    time = [(20, 30), (10, 20), (12, 25)]
    time.sort(key=lambda x: x[1])

    ans = [time[0]]
    count = 1
    end = time[0][1]

    for i in range(1, len(time)):
        if end <= time[i][0]:
            count += 1
            ans.append(time[i])
            end = time[i][1]
    return ans


def difference_pairs():
    """
    pair each el of A with B such that abs. difference is minm
    """
    a = [1, 2, 3]
    b = [2, 1, 3]
    a.sort()
    b.sort()
    minm = float('inf')

    for i in zip(a, b):
        minm = min(minm, abs(i[0] - i[1]))
    return minm


def job_sequence():
    """
    Maximize profit for all jobs with deadline.
    """
    jobs = [(4, 20), (1, 10), (1, 40), (1, 30)]
    jobs.sort(key=lambda x: x[1], reverse=True)

    time = 0
    profit = 0
    for i in jobs:
        if time < i[0]:
            profit += i[1]
            time += 1
    return profit


def indian_coins():
    """
    only canonical coin system can be solved using greedy, indian coin system is canonical
    """
    denoms = [1, 2, 5, 10, 20, 50]
    value = 90
    coins = 0

    denoms.sort(reverse=True)

    for i in denoms:
        if value > i:
            while value >= i:
                coins += 1
                value -= i
    return coins


# -----  FCC Greedy ----------------


if __name__ == '__main__':
    print(indian_coins())
    # print(job_sequence())
    # print(difference_pairs())
    # print(activity_Selection())

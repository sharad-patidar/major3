import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0

    n = int(data[idx]); idx += 1
    names = data[idx:idx+n]; idx += n
    skills = list(map(int, data[idx:idx+n])); idx += n
    name_to_index = {names[i]: i for i in range(n)}

    f = int(data[idx]); idx += 1
    friends = []
    in_friend = set()
    for _ in range(f):
        a, b = data[idx], data[idx+1]
        idx += 2
        friends.append({a, b})
        in_friend.update([a, b])

    r = int(data[idx]); idx += 1
    rivals = [tuple(data[idx+i:idx+i+2]) for i in range(0, 2*r, 2)]
    idx += 2 * r
    limit = int(data[idx])

    groups = []
    for a, b in friends:
        total = skills[name_to_index[a]] + skills[name_to_index[b]]
        groups.append(([a, b], total))
    for name in names:
        if name not in in_friend:
            groups.append(([name], skills[name_to_index[name]]))

    g = len(groups)
    rival_pairs = set()
    for a, b in rivals:
        rival_pairs.add((a, b))
        rival_pairs.add((b, a))

    best = 0

    def dfs(i, score, chosen, count):
        nonlocal best
        if score > limit:
            return
        best = max(best, count)
        if i == g:
            return
        members, s = groups[i]
        ok = True
        for m in members:
            for c in chosen:
                if (m, c) in rival_pairs:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            dfs(i+1, score+s, chosen + members, count + len(members))
        dfs(i+1, score, chosen, count)

    dfs(0, 0, [], 0)
    print(best)

if __name__ == "__main__":
    main()
# small utilities, no deps

def flatten(xs):
    return [y for x in xs for y in x]

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(clamp(4, 0, 20))

# works for now

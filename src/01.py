from utils import fn_in, fn_out

fn_in = fn_in(1)
fn_out = fn_out(1)

left, right = [], []
with open(fn_in, "r") as f:
    for line in f.readlines():
        l, *_, r = line.split(' ')
        left.append(int(l))
        right.append(int(r))

left = sorted(left)
right = sorted(right)

distance = 0
for l, r in zip(left, right):
    distance += abs(l - r)

print(distance)

# ===

similarity = 0
for l in left:
    l_in_right = 0
    for r in right:
        if r == l:
            l_in_right += 1
    similarity += l * l_in_right

print(similarity)

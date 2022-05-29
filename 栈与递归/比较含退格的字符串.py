
def backspaceCompare(s: str, t: str) -> bool:
    stack_s, stack_t = [], []
    for cha in s:
        if cha == '#' and stack_s:
            stack_s.pop()
        else:
            stack_s.append(cha)
    for cha in t:
        if cha == '#' and stack_t:
            stack_t.pop()
        elif cha == '#' and not stack_t:
            continue
        else:
            stack_t.append(cha)
    return stack_s == stack_t

s = "y#fo##f"
t = "y#f#o##f"
print(backspaceCompare(s, t))
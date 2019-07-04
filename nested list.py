List1 = [[input(), float(input())] for _ in range(int(input()))]
sat = set(List1[i][1] for i in range(0, len(List1)))
sat.remove(min(sat))
List3 = [List1[i][0] for i in range(0, len(List1)) if List1[i][1] == min(sat)]
[print(x) for x in sorted(List3)]


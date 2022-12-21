set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)

print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

set_uf=set_u1.union(set3)

set_i1=set1.intersection(set2)

set_if=set_i1.intersection(set3)

set_12=set1.intersection(set2)

set_23=set2.intersection(set3)

set_13=set1.intersection(set3)

set_f1=set_uf-set_12-set_23-set_13
print(set_f1)

print("\nQ.8(c)")
set_c1=set_12.union(set_23)

set_c2=set_c1.union(set_13)

set_final=set_c2-set_if

print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)

print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1

print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)

print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)

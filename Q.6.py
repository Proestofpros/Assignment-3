repeat="Y"
dic={}
dic2={}

list=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":

    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:

        dic.update({sid: name})

        dic2.update({name:sid})

        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in list)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))


print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)

print("\nQ.6(d)")
enter_sid = int(input("Enter SID to get name of student:"))

output_name = str(dic.get(enter_sid))

print(f"Name of student with SID {enter_sid} is {output_name}.")

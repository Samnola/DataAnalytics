# for loops

#for i in ['a', 'b', 'c']:
    #print(f'At this step, the loop value is {i}')

#for i in '123':
    #print(f'At this step, the iterator value is {i}')

#for i in range(1, 4):
    #print(f'At this step, the iterator value is {i}')

groceries = ["apples", "peaches", "bread"]

basket = []

for i in groceries:
    if i =="apples":
        print("How about them apples")
        basket.append(i)
    elif i == "peaches":
        print("Dont forget peaches")
    elif i == "bread":
        print("Get that bread")
        basket.append(i)
    print("End loop")

print(f'Grocery basket includes {basket}')
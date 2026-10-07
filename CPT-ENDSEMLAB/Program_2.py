# 0/1 Knapsack - Cloud Resource Allocation

def knapsack(resources, revenue, capacity):
    n = len(resources)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            resource = resources[i - 1]
            value = revenue[i - 1]

            if resource > w:
                dp[i][w] = dp[i - 1][w]
            else:
                not_selected = dp[i - 1][w]
                selected = value + dp[i - 1][w - resource]
                dp[i][w] = max(not_selected, selected)

    selected_applications = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_applications.append(i)
            w -= resources[i - 1]

    selected_applications.reverse()
    return dp, selected_applications

applications = ['App A', 'App B', 'App C', 'App D']
resources = [2, 3, 4, 5]
revenue = [40, 50, 70, 80]
capacity = 7

dp, selected = knapsack(resources, revenue, capacity)

print('=' * 60)
print('0/1 KNAPSACK - CLOUD RESOURCE ALLOCATION')
print('=' * 60)
print('\nAvailable Resource Capacity:', capacity)

print('\nApplications:')
for i in range(len(applications)):
    print(f'{i + 1}. {applications[i]} | Resource = {resources[i]} | Revenue = {revenue[i]}')

print('\nMaximum Revenue:', dp[len(applications)][capacity])
print('\nSelected Applications:')

total_resources = 0
total_revenue = 0
for i in selected:
    index = i - 1
    print(f'- {applications[index]} (Resource = {resources[index]}, Revenue = {revenue[index]})')
    total_resources += resources[index]
    total_revenue += revenue[index]

print('\nTotal Resources Used:', total_resources)
print('Total Revenue:', total_revenue)

print('\nDP TABLE')
print('-' * 60)
print('App\\Capacity', end='\t')
for w in range(capacity + 1):
    print(w, end='\t')
print()

for i in range(len(applications) + 1):
    if i == 0:
        print('None', end='\t\t')
    else:
        print(applications[i - 1], end='\t\t')
    for w in range(capacity + 1):
        print(dp[i][w], end='\t')
    print()

print('\nTime Complexity: O(n x C)')
print('Space Complexity: O(n x C)')
print('\nWhere:')
print('n = number of applications')
print('C = available resource capacity')

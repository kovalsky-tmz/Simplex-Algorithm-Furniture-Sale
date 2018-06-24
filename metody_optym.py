import pulp
lp_problem = pulp.LpProblem("Furniture Production Optimizer \nObjective", pulp.LpMaximize)
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')

s1=15 * x1 + 8 * x2 <= 3240
s2=25 * x1  + 5 * x2 <= 4300
s3=1 * x1 + 0.6 * x2 <= 200

# Objective function
lp_problem += (500 * x1) + (180 * x2), 'Profit'

# Constraints
lp_problem += s1
lp_problem += s2
lp_problem += s3

print(lp_problem)

lp_problem.solve()
print(pulp.LpStatus[lp_problem.status])

for variable in lp_problem.variables():
    print ("Product {} amount= {}".format(variable.name, variable.varValue))
print ('Profit : {}'.format(pulp.value(lp_problem.objective)))
print ('The rest of resources: Płyta wiórowa {}, Płyta MDF {}, Energia elektryczna {}'.format(pulp.value(s1),pulp.value(s2),round(pulp.value(s3),2)))
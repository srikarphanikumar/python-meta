def sum(x,y):
    return x+y;

print('Sum of 3 and 2: ', sum(3,2));

def calculateTax(bill, tax_rate):
    return round((bill * tax_rate) / 100.0, 2);

print('Tax for $15 with 10% tax_rate is:', calculateTax(15, 3));


# Python Scope: 
# (lowest -> highest: Local, enclosed, global, built-in (abbreviated as LEGB))

global_var = 10;

def fn1(): 
    enclosed_var = 8;

    def fn2():
        print('Access to Global: ', global_var);
        print('Access to Enclosed inside fn2: ', enclosed_var);
    fn2();

# print('Access to Enclosed inside fn2: ', enclosed_var); 
# // Name Error: enclosed_var is not defined
fn1();

print('******** Args and Kwargs(key-word args) ***********');
def sumArgs(*args):
    sum = 0;
    for x in args:
        sum += x;
    return sum;

print('sum of 1, 2,3 using args:', sumArgs(1,2,3));

def sumKwargs(**kwargs):
    sum = 0;
    for key, value in kwargs.items():
        sum += value;
    return sum;

print('sumKwargs(coffe=1, tea=3, juice=5) using kwargs:', sumKwargs(coffe=1, tea=3, juice=5));
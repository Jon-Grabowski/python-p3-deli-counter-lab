katz_deli = []


def line(deli):
    count = 1
    if len(deli) == 0:
        print("The line is currently empty.")
    else: 
        outputString = "The line is currently:"
        for cust in deli:
            outputString+=f" {count}. {cust}"
            count+=1
        print(outputString)

def take_a_number(deli, cust):
    deli.append(cust)
    print(f'Welcome, {cust}. You are number {len(deli)} in line.')
    

def now_serving(deli):
    if len(deli) > 0:
        customer = deli.pop(0)
        print(f"Currently serving {customer}.")
    else:
        print("There is nobody waiting to be served!")


# take_a_number(katz_deli, "Jon")
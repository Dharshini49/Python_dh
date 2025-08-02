def fullname(fn,ln):
    full_name=f"{fn} {ln}"
    return full_name.title()

def make_pizza(*toppings):
    for topping in toppings:
        print(f"{topping} pizza")
make_pizza('pepperoni', 'mushrooms', 'cheese')

def userinfo(fn, ln, **info):
    info['fname']=fn
    info['lname']=ln
    return info
profile= userinfo('dharshini','r',age=20,branch='MID',year=4)
print(profile)

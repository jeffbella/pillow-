from setup_class import shipping_cost_index, shipping_cost_breakpoint
#stuff here

    # Notes
    # really these variables need to be instantiated for each range
    # there should be variables that are pulled from a db somewhere
    # could maybe convert shipping cost into a class?

#creating a variable to hold index cost
shipping = shipping_cost_index(2,6,10)
g_cost = shipping_cost_breakpoint(1.5,3,4,4.75)
d_cost = shipping_cost_breakpoint(4.5,9,12,14.25)



def g_s_cost(weight):
  if (weight <= shipping.break_point_1):
    return weight * 1.5 + 20
  elif (weight <= shipping.break_point_2):
    return weight * 3 + 20
  elif (weight <= shipping.break_point_3):
    return weight * 4 + 20
  elif (weight > shipping.break_point_3):
    return weight * 4.75 + 20
  else:
    return "error"

def d_s_cost(weight):
  if (weight <= 2):
    return weight * 4.5
  elif (weight <= 6):
    return weight * 9
  elif (weight <= 10):
    return weight * 12
  elif (weight > 10):
    return weight * 14.25
  else:
    return "error"

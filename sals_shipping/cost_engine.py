from setup_class import *
#stuff here

    # Notes
    # need to add dynamic way to set shipping breakpoints and  cost indexes

    #version 1.0.1
      # adding 
      # adding rigid classes for cost indexes

#creating a variable to hold index cost
shipping = shipping_cost_index(2,6,10)
g_cost = shipping_cost_breakpoint(1.5,3,4,4.75)
d_cost = shipping_cost_breakpoint(4.5,9,12,14.25)

# Rate 
# multiplier1, multiplier2, multiplier3, multiplier4, flat_rate
g_price_index = rate_index(1.5, 3, 4, 4.75, 20)
d_price_index = rate_index(4.5,9,12,14.25, 0)




#Result Functions

def g_s_cost(weight):
  if (weight <= shipping.break_point_1):
    return weight * g_price_index.multiplier1 + g_price_index.flat_rate
  elif (weight <= shipping.break_point_2):
    return weight * g_price_index.multiplier2 + g_price_index.flat_rate
  elif (weight <= shipping.break_point_3):
    return weight * g_price_index.multiplier3 + g_price_index.flat_rate
  elif (weight > shipping.break_point_3):
    return weight * g_price_index.multiplier4 + g_price_index.flat_rate
  else:
    return "error"

def d_s_cost(weight):
  if (weight <= 2):
    return weight * d_price_index.multiplier1 + d_price_index.flat_rate
  elif (weight <= 6):
    return weight * d_price_index.multiplier2 + d_price_index.flat_rate
  elif (weight <= 10):
    return weight * d_price_index.multiplier3 + d_price_index.flat_rate
  elif (weight > 10):
    return weight * d_price_index.multiplier4 + d_price_index.flat_rate
  else:
    return "error"

#Notes


#Shipping cost index is each pricepoint range or limit in dollars
    # ex: shipping_cost_index(2,3) is the ranges 0.00-2.00 and 2.01 -3.00
class shipping_cost_index:
    def __init__(self, break_point_1, break_point_2, break_point_3):
        self.break_point_1 = break_point_1
        self.break_point_2 = break_point_2
        self.break_point_3 = break_point_3
    #Future Methods

#bp = break_point
#break points will be defined as the limit or range of each pricepoint
class shipping_cost_breakpoint:
    def __init__(self, bp1, bp2, bp3, bp4):
        self.bp1 = bp1
        self.bp2 = bp2
        self.bp3 = bp3
        self.bp4 = bp4

# Rate indexes

#takes in a multiplier and a flat rate (x, +)
class rate_index:
    def __init__(self, multiplier1, multiplier2, multiplier3, multiplier4, flat_rate):
        self.multiplier1 = multiplier1
        self.multiplier2 = multiplier2
        self.multiplier3 = multiplier3
        self.multiplier4 = multiplier4
        self.flat_rate = flat_rate
 
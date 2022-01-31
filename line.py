def line_calc(points,x):
    x1 = points[0][0]
    x2 = points[1][0]
    y1 = points[0][1]
    y2 = points[1][1]

    slope = slope_calc(x1,x2,y1,y2)

    return slope*(x-x1) + y1

def slope_calc(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)
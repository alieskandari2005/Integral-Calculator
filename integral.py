import matplotlib.pyplot as plt
import  numpy as np
import math
import re

plt.style.use('ggplot')
func = input('taabe ra vared konid(agar ghasde vodoore taabe mosalasati ra darid be in soorat vared konid->math.sin(x)): ')
a = int(input('ebtedaye bazeye morede nazar rooye mehvare X ra vared konid: '))
b = int(input('entehaye bazeye morede nazar rooye mehvare X ra vared konid: '))
d = float(input('hade paeene antegral ra vared konid: '))
e = float(input('hade baalaaye antegral ra vared konid: '))
n = int(input('tedade n ra baraye taghsime masahate zire monhani vared konid: '))
if n % 2 == 1:
    n = int(input('hatman bayad n zoj bashad!dobare n ra vared konid: '))

def f(x):
    return eval(func)
X = list(np.arange(a,b+1,0.1))
Y = list(map(f, X))

def simps(f,a,b,N=50):
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S
if re.search(r'math.', func)==None:
    integral = simps(lambda x : eval(func),d,e,n)
else:
    trigonometric_function = func
    trigonometric_function = re.sub(r'math.', 'np.', trigonometric_function)
    trigonometric_function = re.sub(r'\(x\)', '', trigonometric_function)
    integral = simps(eval(trigonometric_function),d,e,n)
fig = plt.figure()
man = plt.get_current_fig_manager()
man.canvas.set_window_title('integral simpson rule calculator')
plt.plot(X,Y)
px = np.arange(d, e, 0.1)
if re.search(r'math.', func)==None:
    plt.fill_between(px, f(px), color = 'b')
else:
    tr = func
    tr = re.sub(r'math.', 'np.', tr)
    def tr_ang(x):
        return eval(tr)
    plt.fill_between(px, tr_ang(px), color = 'b')
plt.suptitle('meghdare mohasebe shode barabar ba %f ast'%integral)
plt.show()

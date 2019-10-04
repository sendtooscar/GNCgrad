import ipywidgets as w
from IPython.display import display

a = w.IntSlider()
b = w.IntText()
w.jslink((a, 'value'), (b, 'value'))
display(a, b)
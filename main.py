# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Test draw_cat_plot function
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')

# Test draw_heat_map function
heat_map = draw_heat_map()
heat_map.savefig('heatmap.png')

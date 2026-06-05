import medical_data_visualizer
from unittest import main

# Test your functions by fetching the figures
print("Generating Categorical Plot...")
medical_data_visualizer.draw_cat_plot()

print("Generating Heat Map Correlation Matrix...")
medical_data_visualizer.draw_heat_map()

# Run automated tests automatically
print("\nRunning automated unit tests...")
main(module='test_module', exit=False)

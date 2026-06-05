import unittest
import medical_data_visualizer
import matplotlib as mpl
import pandas as pd
import numpy as np

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.char_plot = medical_data_visualizer.draw_cat_plot()
        self.heat_map = medical_data_visualizer.draw_heat_map()

    def test_data_import(self):
        actual = type(medical_data_visualizer.df)
        expected = pd.core.frame.DataFrame
        self.assertEqual(actual, expected, "Expected the data to be imported into a pandas DataFrame.")

    def test_overweight_column(self):
        actual = medical_data_visualizer.df['overweight'].sum()
        expected = 24440
        self.assertEqual(actual, expected, "Expected the overweight column to sum up to 24440.")

    def test_normalize_data(self):
        actual_chol = medical_data_visualizer.df['cholesterol'].value_counts().to_dict()
        expected_chol = {0: 52385, 1: 17615}
        self.assertEqual(actual_chol, expected_chol, "Expected cholesterol value counts to match normalized results.")
        
        actual_gluc = medical_data_visualizer.df['gluc'].value_counts().to_dict()
        expected_gluc = {0: 59479, 1: 10521}
        self.assertEqual(actual_gluc, expected_gluc, "Expected glucose value counts to match normalized results.")

    def test_cat_plot_attributes(self):
        # Check if the figure was created properly
        self.assertIsInstance(self.char_plot, mpl.figure.Figure, "Expected the return value to be a matplotlib figure.")
        
        # Check the number of panels (should be 2 for cardio=0 and cardio=1)
        actual_axes = len(self.char_plot.get_axes())
        expected_axes = 2
        self.assertEqual(actual_axes, expected_axes, "Expected 2 panels (axes) in the categorical plot.")

    def test_heat_map_cleaning(self):
        # Check if the data was cleaned properly by counting remaining rows
        # The cleaned data should have exactly 63259 rows after eliminating outliers
        actual_rows = len(medical_data_visualizer.df[
            (medical_data_visualizer.df['ap_lo'] <= medical_data_visualizer.df['ap_hi']) &
            (medical_data_visualizer.df['height'] >= medical_data_visualizer.df['height'].quantile(0.025)) &
            (medical_data_visualizer.df['height'] <= medical_data_visualizer.df['height'].quantile(0.975)) &
            (medical_data_visualizer.df['weight'] >= medical_data_visualizer.df['weight'].quantile(0.025)) &
            (medical_data_visualizer.df['weight'] <= medical_data_visualizer.df['weight'].quantile(0.975))
        ])
        expected_rows = 63259
        self.assertEqual(actual_rows, expected_rows, "Expected the filtered data rows to be exactly 63259.")

    def test_heat_map_values(self):
        # Extract the correlation matrix from the heatmap plot to check values
        ax = self.heat_map.get_axes()[0]
        actual_labels = [text.get_text() for text in ax.get_xticklabels()]
        expected_labels = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual_labels, expected_labels, "Expected the correlation matrix features to match dataset variables.")

if __name__ == "__main__":
    unittest.main()

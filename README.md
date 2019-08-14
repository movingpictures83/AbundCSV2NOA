# AbundCSV2NOA
# Language: Python
# Input: CSV (abundances)
# Output: NOA (nodes and average abundances)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to take a CSV file of abundances, compute their averages, and store
the results in a Node Attribute File (NOA). This file can in turn be imported into Cytoscape.

Rows of the CSV file are assumed to correspond to samples, and columns to taxa.
Entry (i,j) of the CSV table is therefore assumed to contain the abundance of taxa j in sample i.

The format of the NOA file will be a simple table, with node name in the first column
and average abundance in the second.

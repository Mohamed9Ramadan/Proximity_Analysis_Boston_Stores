import arcpy
from arcpy.sa import EucDistance
arcpy.env.workspace = "D:\ITI\ITI\Analysis with python.gdb"

input_BostonStores = "BostonStores"
output_BostonStores_thiessen = "thiessen_polygons"
arcpy.analysis.CreateThiessenPolygons(input_BostonStores, output_BostonStores_thiessen, "ALL")
print("Thiessen polygons created successfully")

input_customers = "Customers"
near_feature = "BostonStores"
s_radius = "10 Kilometers"
arcpy.analysis.Near(input_customers, near_feature, search_radius=s_radius, location="LOCATION", angle="NO_ANGLE", method="PLANAR", distance_unit="KILOMETERS")
print("Near tool excuted successfully")

selected_features = "Customers"
arcpy.management.MakeFeatureLayer(selected_features, "Customers_layer")
sql_query = "NEAR_DIST <> -1"
arcpy.management.SelectLayerByAttribute("Customers_layer", "NEW_SELECTION", sql_query)
print("Selection completed successfully.")

desire_lines_output = "desire_lines"
arcpy.management.XYToLine("Customers_layer", desire_lines_output, "X_Coordinate", "Y_Coordinate", "NEAR_X", "NEAR_Y", "GEODESIC")
print("Desire lines created successfully.")

stores = "BostonStores"
distance_output = "euclidean_distance"
distance_raster = EucDistance(stores)
distance_raster.save(distance_output)
print("Euclidean distance raster created successfully.")
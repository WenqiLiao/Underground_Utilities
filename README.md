# Predicting Underground Utilities Using Machine Learning Techniques and Graph Theory-Based Algorithm 

## Authors and Contributions 


As part of NYU's Undergraduate Summer Research Program, researchers Jasper Hall (Brooklyn Tech High School), Wenqi Liao (NYU CAS'24), Isha Sing (NYU Tandon'25) and Indeera Saha (NYU Tandon'26) worked to develop this project in collaboration with the NYU Center for Urban Science and Progress. 

## Project Details and Methodologies 

In the past 20 years, excavation-based construction projects in the US have experienced a loss of 10.8 billion dollars and 274 lives as a result of pipes being hit (data from PHSMA). These underground utilities are inconsistently mapped and poorly communicated, which results in construction workers needing to waste time and money in order to map them themselves. The goal of this research is to create a data pipeline that can utilize data from above-ground utilities to predict a network of underground utilities that connect them. This is done in 2 parts.

### Part 1: Digitizing Data 

The former of the two is researching historic Sanborn maps with either above-ground utilities identified, or both above and underground utilities identified. We then separate that infrastructure in both ArcGIS and QGIS using either manual or automated methods(such as Random Forest, Support Vector Machine, Unclassified Learning, and Hough Transform).

### Part 2: Algorithm Workflow 

The latter portion of the project is creating the network that utilizes multiple graph theory algorithms to create a minimum spanning tree in which the edges are the pipes and the nodes are the above-ground infrastructure they connect. The completed network is then compared to the separated underground utilities to determine the accuracy and potential for use in future construction plans to reduce excavation mishaps.

## Licenses and Resources 




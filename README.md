# K-Means Clustering on Principal Component Analysis

Principal component analysis is a preprocessing and data analysis technique (used widely in machine learning) that attempts to reduce the dimensionality of highly dense data greater than three dimensions, able to project a collection of points known as **principal components** onto a two-dimensional space. 
Combined with clustering algorithms such as *k-means clustering, DBSCAN, etc.*, one can visualize and group clusters projected by PCA for interpretation (e.g., to analyze similarity and etc.)

Here, I've experimented on a sample data set of metabolites found on infected/uninfected bark samples, and rendered the data after preprocessing it using PCA onto a two-dimensional and three-dimensional space, then used k-means clustering to
group metabolites together and discover which metabolites have had the most significance in the biological processes of the plant's pathology.

## 2D Projection
![Figure_1](https://github.com/user-attachments/assets/ebfade8c-ecb5-4ecd-9438-a59bb33636cf)

## 3D Projection
![Figure_2](https://github.com/user-attachments/assets/16c70b4d-0ee0-44d4-a7be-986f9aa1d035)

## 
Combined with data collected from liquid-chromatography mass-spectrometry, one can encover the significant metabolites, compounds, proteins, etc., responsible for what may offset or enable the
organism's abilities to perform in a given environment using computational techniques; the key of bioinformatics.

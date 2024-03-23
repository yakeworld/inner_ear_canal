## Three-Dimensional Reconstruction and Spatial Orientation Measurement of the Membranous Semicircular Canals Enabled by Multi-Modal High-Resolution Imaging，
## Abstract
### Background:
Accurate delineation of membranous semicircular canal geometry and spatial orientation is crucial for understanding angular head motion transduction and elucidating vestibular pathophysiology. However, these delicate structures have been challenging to study due to their small size and encasement within the bony labyrinth.
### Purpose:
To reconstruct the 3D structures of membranous semicircular canals and measure their spatial orientations using multi-modal high-resolution imaging techniques, enabling a direct comparison with the bony canal orientations and investigations into their morphological characteristics.
### Methods:
Human temporal bone specimens were scanned by micro-CT, industrial CT, and magnetic resonance microscopy at ultrahigh resolutions. Advanced segmentation algorithms were employed to extract highly accurate 3D models of both bony and membranous labyrinth structures. Centerline extraction and registration techniques were utilized to determine the spatial orientations of individual semicircular canals in a standardized coordinate system. Comprehensive morphological analyses were performed on the reconstructed membranous canal models.
### Results: 
Spatial orientation vectors of individual membranous semicircular canals were quantified, revealing small but noticeable deviations from their bony counterparts (mean angle 1.11°-3.01°). Distinct morphological features of the membranous canals were characterized, including  non-planar conformations compared to idealized geometries. These findings provide unprecedented structural insights into the intricate membranous labyrinth.
### Conclusions: 
This study demonstrates the power of multi-modal high-resolution imaging in unveiling previously inaccessible details of the membranous semicircular canal system. The measured spatial orientation disparities and unique morphological attributes suggest potential biomechanical implications in angular motion transduction. The ability to precisely reconstruct and quantify membranous canal structures advances our understanding of vestibular biokinematics and pathophysiology.

## readme
The directory contains centerline data for bony and membranous semicircular canals from different imaging sequences. The *.mrk.json files represent the centerline data for the semicircular canals, and the data_dict.json file contains the extracted centerline data.

The getmark.py program extracts the centerline data from the *.mrk.json files and calculates the normal vectors of the semicircular canal planes.

The checkangle.py program analyzes the angles between the semicircular canal planes.




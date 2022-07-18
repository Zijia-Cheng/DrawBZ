# DrawBZ
Welcome to use this small program for drawing three dimensional Bulk and Surface Brillouin Zones.

Directly download the jupyter notebook and use it! Require numpy and matplotlib


Class: BZ

Initial input: Vectors of bulk Brillouin zone, with unit A^-1 and written in the Cartesian coordinates. eg: np.array([[1,0,0],[0,1,0],[0,0,1]]).

*To calculate the Bulk BZ, just run method self.bulkBZ(), then you can get attributes: self.hs_lines_f: sides of the bulk BZ; self.hs_points: corner of the bulk BZ.

*Similarly, for obtaining surface BZ, run method self.surfaceBZ(dis,direc), where dis = an arbitrary positive number repsenting the distance between Bulk BZ center and surface BZ canter for plotting purpose, direc: surface normal direction written in Fractional coordinates with BZ vectors as basis.
Then you can get attributes: self.hs_lines_pro_f and self.hs_pro_points.

!Make sure call bulkbZ before calling surfaceBz.

Example:

![Screen Shot 2022-07-17 at 10 12 48 PM](https://user-images.githubusercontent.com/62127000/179436001-5863e173-997f-4f67-b9c6-ad63d735cfee.png)

![Screen Shot 2022-07-17 at 10 13 15 PM](https://user-images.githubusercontent.com/62127000/179436027-cee2ebaf-0c28-454f-b611-811bb18a1c61.png)

![Screen Shot 2022-07-17 at 10 14 05 PM](https://user-images.githubusercontent.com/62127000/179436092-662490c5-64a9-4ff0-87de-953620bf2b6e.png)

![Screen Shot 2022-07-17 at 10 15 56 PM](https://user-images.githubusercontent.com/62127000/179436221-65b157ce-4b0c-44fd-9481-43d8ec298b48.png)

![Screen Shot 2022-07-17 at 10 16 25 PM](https://user-images.githubusercontent.com/62127000/179436251-ac964b61-31b5-44ef-81d0-88f9f88c8744.png)

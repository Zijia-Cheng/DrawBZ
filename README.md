# Draw Brillouin Zones

Welcome to the **Draw Brillouin Zones** program! This tool helps you visualize three-dimensional Bulk and Surface Brillouin Zones (BZ). It's straightforward to use and requires only minimal dependencies.

If you find this program helpful, please consider starring this repository!

---

## 🚀 Features
- **Draw Bulk Brillouin Zones**: Visualize high-symmetry points and lines for bulk BZs.
- **Draw Surface Brillouin Zones**: Generate surface BZ projections along specified directions.
- **Lightweight and Easy-to-Use**: Compatible with Jupyter notebooks and standalone Python scripts.

---

## 📦 Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`

---

## 🔧 How to Use

1. Download the provided Jupyter Notebook or Python script from this repository.
2. Ensure the required libraries (`numpy`, `matplotlib`) are installed.
3. Initialize the `BZ` class with the bulk BZ vectors.

---

### 🧪 Class: `BZ`

#### **Input Parameters**
- **Vectors of Bulk Brillouin Zone**: A 3x3 numpy array representing the bulk BZ vectors in Cartesian coordinates, with units in $\text{Å}^{-1}$.  
  Example:
  ```python
  np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
  ```
  
### 🛠 Methods and Attributes

#### 1. Bulk Brillouin Zone

- **Method**: `self.bulkBZ()`
- **Output Attributes**:
  - `self.hs_lines_f`: Edges of the bulk BZ.
  - `self.hs_points`: High-symmetry points (corners) of the bulk BZ.

---

#### 2. Surface Brillouin Zone

- **Method**: `self.surfaceBZ(dis, direc)`
  - **Parameters**:
    - `dis`: A positive number representing the distance between the bulk BZ center and surface BZ center (used for plotting purposes).
    - `direc`: Surface normal direction in fractional coordinates, expressed using bulk BZ vectors as the basis.
  - **Output Attributes**:
    - `self.hs_lines_pro_f`: Edges of the surface BZ.
    - `self.hs_pro_points`: High-symmetry points of the surface BZ.

---

#### ⚠️ Important:
- Always call `bulkBZ()` before using `surfaceBZ()`.

---
### 🔍 Example Usage

Calculate bulk BZ:
![Screen Shot 2022-07-17 at 10 12 48 PM](https://user-images.githubusercontent.com/62127000/179436001-5863e173-997f-4f67-b9c6-ad63d735cfee.png)
![Screen Shot 2022-07-17 at 10 13 15 PM](https://user-images.githubusercontent.com/62127000/179436027-cee2ebaf-0c28-454f-b611-811bb18a1c61.png)
Visualization of bulk BZ:
![Screen Shot 2022-07-17 at 10 14 05 PM](https://user-images.githubusercontent.com/62127000/179436092-662490c5-64a9-4ff0-87de-953620bf2b6e.png)
Calculate surface BZ along (001) direction:
![Screen Shot 2022-07-17 at 10 15 56 PM](https://user-images.githubusercontent.com/62127000/179436221-65b157ce-4b0c-44fd-9481-43d8ec298b48.png)
Visualization of surface and bulk BZ:
![Screen Shot 2022-07-17 at 10 16 25 PM](https://user-images.githubusercontent.com/62127000/179436251-ac964b61-31b5-44ef-81d0-88f9f88c8744.png)

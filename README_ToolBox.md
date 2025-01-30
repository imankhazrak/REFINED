# Toolbox.py - Function Documentation

This file provides a brief description of the functions available in **Toolbox.py**. The functions are categorized based on their usage, including error metrics, feature mapping, image generation, data processing, and machine learning utilities.

---

## **1. Error Metrics**

### `NRMSE(Y_Target, Y_Predict)`
- Computes the **Normalized Root Mean Squared Error (NRMSE)** and **R-squared (R²)**.
- NRMSE provides a scale-independent error measure, while R² represents how well predictions explain the variance in actual values.

### `NMAE(Y_Target, Y_Predict)`
- Computes the **Normalized Mean Absolute Error (NMAE)**.
- NMAE normalizes the **Mean Absolute Error (MAE)** by the variance of the target values, allowing for comparison across datasets.

### `Bias_Calc(Y_Test, Y_Pred)`
- Calculates bias in predictions by fitting a **linear regression** between actual values and errors.
- The regression coefficient represents the **systematic bias** in the model.

---

## **2. Feature Mapping and Normalization**

### `two_d_norm(xy)`
- Normalizes 2D coordinates to the range **[0,1]**.
- Uses min-max scaling independently for x and y coordinates.

### `two_d_eq(xy, Nn)`
- Assigns **evenly spaced ranks** to 2D coordinates based on their sorted order.
- The ranks are normalized to **[0,1]** for both x and y axes.

### `Assign_features_to_pixels(xy, nn, verbose=False)`
- Assigns features to pixels in an **n×n grid** based on Euclidean distance.
- Ensures each feature is assigned to the **nearest available pixel**.

### `Coord_Converter(coords_drug2, nn)`
- Converts **numerical feature indices** into string labels like `F0`, `F1`, etc.
- Creates a formatted coordinate representation for image-based models.

---

## **3. Image Representation & Data Transformation**

### `Random_position(p)`
- Assigns **random 2D grid positions** to `p` features.
- Ensures a uniform spread over a square grid of size **sqrt(p) × sqrt(p)**.

### `Random_Image_Gen(X, Rand_Pos_mat)`
- Converts input data `X` into a **randomly structured image representation**.
- Uses `Rand_Pos_mat` to assign features to specific pixel positions in a **2D grid**.

### `MDS_Im_Gen(X, nn, Img)`
- Generates structured **image representations** from `X` based on a predefined **feature-to-pixel mapping**.
- Ensures missing features are filled with zeroes.

### `REFINED_Im_Gen(X, nn, map_in_int, gene_names, coords)`
- Generates an image representation using the **REFINED** method.
- Converts tabular data into **structured 2D grid-based images** for CNN input.

---

## **4. Data Processing & Filtering**

### `dataframer(Main, Set_in, name_in, name_out)`
- Filters a dataset based on **matching values** from another dataset.
- Useful for extracting relevant records based on key identifiers.

### `GDSC_dataframer(PD_Set, Set_Name, PD_Attribute, Attribute_Name)`
- Extracts and aligns numerical data based on **matching identifiers**.
- Outputs both a **NumPy array** and a **Pandas DataFrame**.

### `GDSC_NPier(PD_Set, Set_Name, PD_Attribute, Attribute_Name)`
- Maps **attribute values** from a reference dataset and returns a **NumPy array**.
- Optimized for structured data extraction.

---

## **5. Classification Utilities**

### `Reg_to_Class(Y, Threshold)`
- Converts **continuous regression outputs** into binary classification based on a threshold.
- Outputs **0 (below threshold)** and **1 (above threshold)**.

### `floattoint(Y_Test_Encoded)`
- Converts **floating-point probability values** into binary classification.
- Uses a **0.5 threshold** to assign `0` or `1` labels.

---

## **Usage Notes**
- The functions are designed for **data transformation, feature mapping, and error evaluation**.
- Most functions assume **NumPy arrays or Pandas DataFrames** as input.
- Feature mapping functions can be used to **convert tabular data into image representations** for deep learning applications.
- Error metric functions help in evaluating the **performance of regression models**.

For additional details, refer to the function docstrings inside `Toolbox.py`. 🚀

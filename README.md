# Coronary Heart Disease Prediction with Random Forest and Logistic Regression
## Description 
- Predict the classification of the 10-year risk of future coronary heart disease (CHD) using Random Forest and Logistic Regression algorithms.  
- The target data is imbalanced (more data with risk 0 compared to risk 1).  
- Apply the oversampling technique using the SMOTE method to address data imbalance.  
- Both algorithms are trained on the original data (without oversampling) and the oversampled data, and their performance is compared based on evaluation metrics such as accuracy, ROC-AUC, confusion matrix, and classification report.  
- The best-performing model is deployed as a web application using the Flask framework for CHD risk prediction.  

## Dataset 
The Framingham Heart Disease dataset contains data from 4,240 patients with 16 columns. The goal of this dataset is to predict the 10-year risk of coronary heart disease (TenYearCHD). Below is a description of some key columns:

- **male**: Patient's gender (1: male, 0: female).  
- **age**: Patient's age (in years).  
- **currentSmoker**: Smoking status (1: yes, 0: no).  
- **cigsPerDay**: Number of cigarettes smoked per day.  
- **BPMeds**: Use of blood pressure medication (1: yes, 0: no).  
- **totChol**: Total cholesterol level.  
- **sysBP**: Systolic blood pressure.  
- **BMI**: Body Mass Index.  
- **glucose**: Blood glucose level.  
- **TenYearCHD**: 10-year risk of coronary heart disease (1: at risk, 0: not at risk).  


## Results 
The modeling results will be divided based on the dataset used.

**Data Tanpa SMOTE** 
#### Logistic Regression
| Metric         | Non-CHD | CHD   | Macro Avg | Weighted Avg |
|----------------|----------|-------|-----------|--------------|
| Precision      | 0.83     | 0.38  | 0.61      | 0.75         |
| Recall         | 0.99     | 0.03  | 0.51      | 0.82         |
| F1-Score       | 0.90     | 0.06  | 0.48      | 0.76         |
| Support        | 702      | 146   | 848       | 848          |
| ROC-AUC        |          |       | 0.70      |              |

- Confusion Matrix
![alt text](image.png)

- ROC Curve
![alt text](image-1.png)

#### Random Forest
| Metric         | Non-CHD | CHD   | Macro Avg | Weighted Avg |
|----------------|----------|-------|-----------|--------------|
| Precision      | 0.83     | 0.40  | 0.62      | 0.76         |
| Recall         | 0.99     | 0.03  | 0.51      | 0.83         |
| F1-Score       | 0.90     | 0.05  | 0.48      | 0.76         |
| Support        | 702      | 146   | 848       | 848          |
| ROC-AUC        |          |       | 0.74      |              |

- Confusion Matrix
![alt text](image-2.png)

- Roc Curve
![alt text](image-3.png)

**Data Oversampled SMOTE**

#### Logistic Regression
| Metric         | Non-CHD | CHD   | Macro Avg | Weighted Avg |
|----------------|----------|-------|-----------|--------------|
| Precision      | 0.66     | 0.65  | 0.66      | 0.66         |
| Recall         | 0.64     | 0.68  | 0.66      | 0.66         |
| F1-Score       | 0.65     | 0.66  | 0.66      | 0.66         |
| Support        | 719      | 720   | 1439      | 1439         |
| ROC-AUC        |          |       | 0.94      |              |

- Confusion Matrix 
![alt text](image-4.png)

- ROC Curve
![alt text](image-5.png)

#### Random Forest
| Metric         | Non-CHD | CHD   | Macro Avg | Weighted Avg |
|----------------|----------|-------|-----------|--------------|
| Precision      | 0.89     | 0.86  | 0.88      | 0.88         |
| Recall         | 0.86     | 0.89  | 0.88      | 0.88         |
| F1-Score       | 0.87     | 0.88  | 0.88      | 0.88         |
| Support        | 719      | 720   | 1439      | 1439         |
| ROC-AUC        |          |       | 0.95      |              |
- Confusion Matrix
![alt text](image-6.png)
- ROC Curve
![alt text](image-7.png)

**Random Forest** emerged as the superior model, achieving higher accuracy, recall, precision, and F1-score compared to Logistic Regression. The high ROC-AUC scores for both models indicate that they effectively handled the data imbalance after applying oversampling techniques.

## Deployment

- Clone repository
```bash
git clone https://github.com/username/coronary_heart_disease.git
cd coronary_heart_disease
```
- Install Depedencies
```bash 
pip install -r requirements.txt
```
- Run Flask Application 
```bash 
python app.py
```
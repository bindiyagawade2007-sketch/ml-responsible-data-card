# Risk Register

## 1. Data Leakage

**Risk:**  
Information that would only be available after the prediction point may accidentally be used as a model feature.

**Impact:**  
The model may appear more accurate than it actually is.

**Mitigation:**  
Use only information available before the prediction point and review every feature for possible leakage.

**Monitoring:**  
Perform feature-level leakage checks before training and after major data changes.

---

## 2. Missing Data

**Risk:**  
Some customer records may have missing values.

**Impact:**  
Missing information may reduce model performance or create biased predictions.

**Mitigation:**  
Check missing values before training and use appropriate handling methods.

**Monitoring:**  
Track missing-value rates when new data is introduced.

---

## 3. Duplicate Records

**Risk:**  
The same customer may appear more than once.

**Impact:**  
Duplicate records can distort model training and evaluation.

**Mitigation:**  
Check `customer_id` for duplicate records before training.

---

## 4. Class Imbalance

**Risk:**  
The number of churned and non-churned customers may be unequal.

**Impact:**  
Accuracy may look good even if the model performs poorly on churned customers.

**Mitigation:**  
Check class distribution and monitor precision, recall, F1-score, and the confusion matrix.

---

## 5. False Positives

**Risk:**  
The model predicts churn when the customer does not actually churn.

**Impact:**  
Unnecessary retention actions, communications, discounts, and staff effort.

**Mitigation:**  
Monitor the false-positive rate and use an appropriate decision threshold.

**Human Review:**  
Important retention actions should be reviewed by a human.

---

## 6. False Negatives

**Risk:**  
The model predicts that a customer will not churn when the customer actually churns.

**Impact:**  
A potential retention opportunity may be missed.

**Mitigation:**  
Monitor recall and review missed churn cases.

---

## 7. Privacy Risk

**Risk:**  
Customer-level information may be exposed or used unnecessarily.

**Impact:**  
Customer privacy could be affected.

**Mitigation:**  
Use only necessary information, avoid unnecessary personal data, and restrict access to authorized users.

---

## 8. Model Drift

**Risk:**  
Customer behavior may change over time.

**Impact:**  
Model performance may decrease after deployment.

**Mitigation:**  
Monitor performance and data distributions regularly.

**Rollback:**  
If performance becomes unacceptable, stop using the model and return to a previously validated model or the non-ML baseline.

---

## 9. Over-Reliance on the Model

**Risk:**  
Users may treat model predictions as certain decisions.

**Impact:**  
Incorrect predictions may lead to inappropriate customer actions.

**Mitigation:**  
Use the model as decision support rather than the sole decision-maker.

**Human Review:**  
Low-confidence or high-impact cases should be reviewed by a human.

---

## 10. Small Dataset

**Risk:**  
The available training dataset is small.

**Impact:**  
Model evaluation results may be uncertain and may not generalize to other customer populations.

**Mitigation:**  
Use careful train/test evaluation and validate the model with additional representative data before real-world deployment.

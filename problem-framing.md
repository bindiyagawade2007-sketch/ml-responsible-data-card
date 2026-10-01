# ML Problem-Framing Memo

## 1. Decision

The decision is to identify customers who may be at risk of churn so that a customer-retention team can decide whether additional customer support or engagement may be appropriate.

The ML model should support human decision-making and should not automatically make important customer decisions.

## 2. Prediction Target

The prediction target is `churned`.

- `1` = Customer churned
- `0` = Customer did not churn

The model will predict the likelihood that a customer may churn.

## 3. Unit of Observation

The unit of observation is one customer.

Each row in the dataset represents an individual customer.

## 4. Available Features

The dataset contains the following features:

- `customer_id`
- `tenure_months`
- `support_tickets`
- `monthly_spend`
- `login_count`
- `plan_type`

The target variable is:

- `churned`

`customer_id` is an identifier and should not be used as a predictive feature.

## 5. Action Window

The model is intended to use customer information available before the prediction point to identify customers who may be at risk of churn in the relevant upcoming period.

Future information must not be used as an input feature.

## 6. Non-ML Baseline

A simple non-ML baseline will be used for comparison.

For example, customers with low login activity, higher support-ticket counts, or other predefined risk indicators can be flagged using a simple rule-based approach.

The ML model should demonstrate useful improvement over this simple baseline before it is considered for practical use.

## 7. False-Positive Cost

A false positive occurs when the model predicts that a customer will churn but the customer does not actually churn.

Possible costs include:

- Unnecessary retention efforts
- Unnecessary discounts or offers
- Additional communication
- Staff time spent on customers who were not going to churn

The false-positive rate should therefore be monitored.

## 8. False-Negative Cost

A false negative occurs when the model predicts that a customer will not churn but the customer actually churns.

Possible costs include:

- Missed retention opportunities
- Loss of a customer
- Loss of potential future revenue

Recall should therefore be monitored carefully.

## 9. Evaluation Metrics

The following metrics will be used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Recall is particularly important because false negatives represent customers who may churn but were not identified.

Precision is also important because unnecessary retention actions can create additional costs.

## 10. Human Review

The model should not automatically trigger high-impact customer actions.

Predictions with low confidence or cases involving significant customer actions should be reviewed by a human.

Human reviewers should be able to override an ML recommendation when appropriate.

## 11. Abstention

If the model has low confidence in a prediction, it should be allowed to abstain rather than making an automatic decision.

Low-confidence cases can be sent for human review.

## 12. Monitoring

The following should be monitored regularly:

- Model accuracy
- Precision
- Recall
- False-positive rate
- False-negative rate
- Changes in customer data
- Changes in prediction distribution
- Model performance over time

## 13. Rollback Conditions

The model should be reviewed or rolled back if:

- Performance decreases significantly.
- False-positive or false-negative rates become unacceptable.
- Data distribution changes substantially.
- Data leakage is discovered.
- Unexpected or harmful model behavior is observed.

A previously validated model or the non-ML baseline can be used while the problem is investigated.

## 14. Data Leakage Prevention

Only information that would have been available at the prediction time should be used.

The target variable `churned` must not be included as an input feature.

The identifier `customer_id` should also not be used as a predictive feature.

Training and testing data should be separated before model evaluation.

## 15. Responsible Use

The model is intended to support customer-retention analysis and learning about responsible ML problem framing.

It should not be used as the sole basis for decisions that could significantly affect customers.

Model limitations, errors, and uncertainty should be communicated clearly to users of the system.

## 16. Success Criteria

The ML approach should:

1. Perform better than the simple non-ML baseline.
2. Maintain acceptable precision and recall.
3. Keep false-positive and false-negative costs under consideration.
4. Avoid data leakage.
5. Support human review for uncertain cases.
6. Be monitored after deployment.

## Conclusion

Customer churn prediction can be framed as a supervised machine learning problem where customer-level features are used to predict the `churned` target.

The ML model should only be used when it provides useful performance compared with a simple baseline and when appropriate safeguards, monitoring, human review, and rollback procedures are in place.

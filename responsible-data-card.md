# Responsible Data Card

## Dataset purpose

This dataset supports a customer churn prediction task. The goal is to predict whether a customer may churn so that a customer-retention team can identify customers who may need attention.

The prediction should support decision-making and should not be the only basis for important customer actions.

## Provenance and permission

The dataset was provided as training data for this educational ML problem-framing exercise.

It contains customer-level information such as tenure, support tickets, monthly spending, login count, plan type, and churn status.

The dataset should be used only for the intended educational and modeling purpose. Real-world deployment would require appropriate permission, privacy review, and applicable legal or compliance checks.

## Population and representation

Each row represents one customer.

The dataset includes:
- Tenure in months
- Support tickets
- Monthly spending
- Login count
- Plan type
- Churn status

The dataset is small and may not represent the full population of real customers. Therefore, results should not automatically be generalized to other customer populations without additional validation.

## Features and target

The target variable is `churned`.

- `1` = customer churned
- `0` = customer did not churn

Features include:
- `tenure_months`
- `support_tickets`
- `monthly_spend`
- `login_count`
- `plan_type`

Data leakage must be checked to ensure that features do not contain information that would only be available after the prediction point.

Sensitive attributes are not explicitly present in the visible dataset. Unnecessary sensitive information should not be added.

## Quality checks

The following checks should be performed:

1. Check for missing values.
2. Check for duplicate customer records.
3. Check for invalid or unusual values.
4. Check the class balance of `churned`.
5. Check the values of `plan_type`.
6. Check numerical ranges.
7. Separate training and testing data before evaluation.
8. Check for data leakage.

Because the dataset is small, evaluation results may have uncertainty.

## Risks and safeguards

### False-positive risk

A false positive occurs when the model predicts that a customer will churn but the customer does not actually churn.

Possible impact:
- Unnecessary retention efforts
- Unnecessary discounts or communications
- Wasted staff time

Safeguard:
- Monitor the false-positive rate.
- Use an appropriate prediction threshold.
- Use human review before significant actions.

### False-negative risk

A false negative occurs when the model predicts that a customer will not churn but the customer actually churns.

Possible impact:
- Missed retention opportunity
- Possible loss of future customer value

Safeguard:
- Monitor recall.
- Review missed churn cases.
- Regularly evaluate model performance.

### Privacy risk

Customer-level information should be handled carefully.

Safeguard:
- Use only necessary information.
- Avoid unnecessary personal data.
- Restrict access to authorized users.

### Data leakage risk

Future information may accidentally be used to predict churn.

Safeguard:
- Use only information available before the prediction point.
- Perform feature-level leakage checks.

### Model drift risk

Customer behavior can change over time and reduce model performance.

Safeguard:
- Monitor performance regularly.
- Review or retrain the model when necessary.
- Maintain a rollback option.

## Intended evaluation

The ML model should be compared with a simple non-ML baseline.

Evaluation should include:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

False-negative errors should be monitored carefully because they may represent missed customers who could have been retained.

Where sufficient data is available, errors should also be examined across relevant customer groups.

Low-confidence predictions should be eligible for human review rather than automatic action.

The model should be monitored after deployment and rolled back if it shows unacceptable performance, unexpected behavior, or significant data drift.

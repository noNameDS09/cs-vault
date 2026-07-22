# 56 ML Project Lifecycle

tags:
#mlops
#project-lifecycle
#ai-development
#placements
#interview

---

## Why this topic matters
Building an ML model is only 20% of the work. The remaining 80% involves data preparation, deployment, monitoring, and iteration. Understanding the **ML Project Lifecycle** helps you plan, execute, and deliver successful AI projects. Companies want engineers who can take projects from concept to production, not just train models in notebooks.

## Learning Objectives
- Understand the phases of an ML project.
- Learn key activities in each phase.
- Understand common pitfalls and how to avoid them.
- Know how to measure success beyond accuracy.

## Prerequisites
- [[03 AI Development Lifecycle]]
- [[58 MLOps]]
- [[55 AI System Design Basics]]

---

## Intuition
Imagine you're building a **house**.

**Phases**:
1. **Planning**: What kind of house? Budget? Timeline?
2. **Foundation**: Lay the groundwork.
3. **Construction**: Build the structure.
4. **Inspection**: Check for issues.
5. **Move-In**: People start living there.
6. **Maintenance**: Fix leaks, repaint, upgrade over time.

**ML Projects** follow a similar lifecycle:
1. **Problem Definition**: What are we solving?
2. **Data Collection**: Gather and prepare data.
3. **Model Development**: Train and evaluate.
4. **Validation**: Test on real scenarios.
5. **Deployment**: Put into production.
6. **Monitoring & Maintenance**: Track performance, update.

Skipping any phase = project failure.

---

## Detailed Explanation

### Phase 1: Problem Definition (10-20% of time)

**Questions to Answer**:
- What business problem are we solving?
- Is ML the right solution? (vs. rules-based system)
- What does success look like? (metrics, KPIs)
- Do we have the right data?
- What are the constraints? (latency, cost, ethics)

**Deliverables**:
- Problem statement document.
- Success metrics (accuracy, latency, business KPIs).
- Risk assessment (bias, fairness, privacy).
- Go/No-Go decision.

**Common Pitfalls**:
- Solving the wrong problem.
- Over-engineering (ML when rules would work).
- Unclear success criteria.

### Phase 2: Data Collection & Preparation (40-60% of time)

**Activities**:
- **Data Sourcing**: Collect from databases, APIs, logs, etc.
- **Data Cleaning**: Handle missing values, outliers, errors.
- **Exploratory Data Analysis (EDA)**: Understand distributions, correlations.
- **Feature Engineering**: Create meaningful features.
- **Data Splitting**: Train/validation/test sets.
- **Data Versioning**: Track data versions (DVC, Git LFS).

**Deliverables**:
- Cleaned, labeled dataset.
- Feature documentation.
- Data quality report.
- Train/validation/test splits.

**Common Pitfalls**:
- Data leakage (test data in training).
- Biased or unrepresentative data.
- Insufficient data for the problem.
- Not documenting data transformations.

### Phase 3: Model Development (20-30% of time)

**Activities**:
- **Baseline Models**: Simple models (logistic regression, mean prediction).
- **Model Selection**: Try different algorithms.
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization.
- **Cross-Validation**: Robust performance estimation.
- **Error Analysis**: Understand where model fails.

**Deliverables**:
- Trained models with performance metrics.
- Model comparison report.
- Error analysis document.
- Final model selection.

**Common Pitfalls**:
- Skipping baselines (can't measure improvement).
- Overfitting to validation set.
- Ignoring error analysis.
- Chasing accuracy over business value.

### Phase 4: Validation & Testing (10-15% of time)

**Activities**:
- **Holdout Testing**: Evaluate on unseen test set.
- **A/B Testing**: Compare with existing system (if applicable).
- **Stress Testing**: Edge cases, adversarial examples.
- **Fairness Testing**: Check for bias across demographics.
- **Performance Testing**: Latency, throughput, resource usage.

**Deliverables**:
- Test performance report.
- Fairness and bias assessment.
- Performance benchmarks.
- Go/No-Go for deployment.

**Common Pitfalls**:
- Testing on biased or small test sets.
- Not testing edge cases.
- Ignoring fairness and ethics.
- Confusing offline metrics with online performance.

### Phase 5: Deployment (10-15% of time)

**Activities**:
- **Model Packaging**: Save model (pickle, ONNX, etc.).
- **API Development**: Build serving endpoint (FastAPI, Flask).
- **Infrastructure Setup**: Servers, containers, cloud.
- **CI/CD Pipeline**: Automated testing and deployment.
- **Rollout Strategy**: Canary, blue-green, gradual rollout.

**Deliverables**:
- Deployed model with API endpoint.
- Deployment documentation.
- Rollback plan.
- Monitoring setup.

**Common Pitfalls**:
- Not planning for rollback.
- Skipping load testing.
- Poor documentation.
- No monitoring in place.

### Phase 6: Monitoring & Maintenance (Ongoing)

**Activities**:
- **Performance Monitoring**: Track accuracy, latency, errors.
- **Data Drift Detection**: Monitor for input distribution changes.
- **Model Retraining**: Schedule or trigger-based retraining.
- **User Feedback**: Collect and incorporate feedback.
- **Incident Response**: Handle failures, bugs, performance drops.

**Deliverables**:
- Monitoring dashboards.
- Alerting system.
- Retraining pipeline.
- Incident response plan.

**Common Pitfalls**:
- No monitoring (model decays silently).
- Not planning for retraining.
- Ignoring user feedback.
- No incident response plan.

---

## Real-world Example

**Credit Scoring Model at a Bank**

**Phase 1: Problem Definition**
- **Problem**: Automate loan approval decisions.
- **Success Metrics**: Approval accuracy (>95%), latency (<100ms), fairness (no demographic bias).
- **Constraints**: Regulatory compliance, explainability required.
- **Go Decision**: ML is suitable; proceed.

**Phase 2: Data Preparation**
- **Data**: 5 years of loan applications, payment history, credit reports.
- **Cleaning**: Handle missing income values, remove duplicates.
- **Features**: Credit score, income, debt-to-income, employment history.
- **Split**: 70% train, 15% validation, 15% test.

**Phase 3: Model Development**
- **Baseline**: Logistic regression (85% accuracy).
- **Models**: Random Forest, XGBoost, Neural Network.
- **Best Model**: XGBoost (93% accuracy, explainable with SHAP).
- **Error Analysis**: Model struggles with self-employed applicants.

**Phase 4: Validation**
- **Test Set**: 92% accuracy (acceptable).
- **Fairness**: No significant demographic bias detected.
- **Performance**: 50ms latency (meets requirement).
- **Go Decision**: Approved for deployment.

**Phase 5: Deployment**
- **Serving**: FastAPI on Kubernetes.
- **Rollout**: 10% of applications first week, then 100%.
- **Rollback**: Revert to manual review if accuracy <90%.

**Phase 6: Monitoring**
- **Metrics**: Accuracy, approval rate, demographic breakdown.
- **Drift Detection**: Alert if input distribution changes >15%.
- **Retraining**: Quarterly, or when drift detected.
- **Feedback**: Manual review of rejected applications.

---

## Advantages
- **Structured Approach**: Reduces risk of failure.
- **Clear Milestones**: Easy to track progress.
- **Business Alignment**: Ensures ML solves real problems.
- **Sustainability**: Monitoring keeps models healthy.

## Limitations
- **Time-Consuming**: 6-12 months for complex projects.
- **Resource-Intensive**: Requires cross-functional teams.
- **Iterative**: May need to revisit earlier phases.

---

## Common Interview Questions
- **Describe the ML project lifecycle.**
- **Why does data preparation take the most time?**
- **How do you define success for an ML project?**
- **What is the difference between offline and online metrics?**
- **How do you handle model decay in production?**
- **What is data leakage and how do you prevent it?**
- **When would you decide NOT to use ML?**

### Interview Answer Tips
- Emphasize that **data preparation is the majority of work** (40-60%).
- Mention that **deployment is not the end**; monitoring is ongoing.
- Note that **not every problem needs ML** (rules-based might be better).

---

## Common Mistakes
- Rushing through problem definition.
- Ignoring data quality and leakage.
- Deploying without monitoring.
- Not planning for retraining.
- Focusing only on accuracy, ignoring business metrics.

---

## Summary
The ML Project Lifecycle includes: Problem Definition (10-20%), Data Preparation (40-60%), Model Development (20-30%), Validation (10-15%), Deployment (10-15%), and Monitoring (ongoing). Each phase has specific activities, deliverables, and pitfalls. Success requires cross-functional collaboration, clear metrics, and ongoing maintenance. Most time is spent on data, not modeling.

---

## Practice Questions
1. Why does data preparation take 40-60% of the time?
2. What are the key questions in problem definition?
3. What is data leakage and how do you prevent it?
4. How do you decide when to use ML vs. rules-based systems?
5. What metrics should you monitor in production?
6. What is a canary deployment?
7. How often should you retrain a model?
8. What is error analysis and why is it important?

---

## Mini Project Ideas
1. **End-to-End Project**: Build a complete ML project following all phases. Document each phase.
2. **Retrospective**: Analyze a past ML project. Identify which phases were skipped or rushed.
3. **Monitoring Dashboard**: Build a dashboard to track model performance metrics over time.

---

## Further Reading
- [[03 AI Development Lifecycle]]
- [[58 MLOps]]
- [[55 AI System Design Basics]]
- [[27 Data Drift]]
- [[48 Model Serving]]
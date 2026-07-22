# 57 MLOps Fundamentals

tags:
#mlops
#devops
#ci-cd
#deployment
#placements
#interview

---

## Why this topic matters
**MLOps** (Machine Learning Operations) is the practice of applying DevOps principles to ML systems. It ensures that ML models are deployed reliably, monitored continuously, and updated efficiently. As companies scale their AI initiatives, MLOps skills are in high demand. Interviewers expect ML engineers to understand CI/CD, monitoring, and model governance.

## Learning Objectives
- Understand what MLOps is and why it's needed.
- Learn the MLOps maturity levels.
- Understand CI/CD for ML (CI/CD/CT).
- Know key MLOps tools and practices.

## Prerequisites
- [[03 AI Development Lifecycle]]
- [[48 Model Serving]]
- [[56 ML Project Lifecycle]]

---

## Intuition
Imagine you're running a **restaurant**.

**Without MLOps (Chaos)**:
- Chef trains once, serves the same dish forever.
- No one checks if ingredients go stale.
- Customers complain, but no one listens.
- Eventually, everyone stops coming.

**With MLOps (Professional Kitchen)**:
- **CI (Continuous Integration)**: Test new recipes before adding to menu.
- **CD (Continuous Deployment)**: Roll out new dishes smoothly.
- **CT (Continuous Training)**: Chef learns new techniques regularly.
- **Monitoring**: Track customer feedback, adjust recipes.
- **Governance**: Health inspections, quality standards.

**MLOps** is the **restaurant management system** for ML.

---

## Detailed Explanation

### What is MLOps?

**MLOps** is a set of practices for deploying, monitoring, and maintaining ML models in production.

**Goals**:
- **Reliability**: Models work consistently.
- **Scalability**: Handle growing traffic and data.
- **Reproducibility**: Can recreate any model version.
- **Governance**: Comply with regulations and standards.
- **Efficiency**: Automate repetitive tasks.

### MLOps Maturity Levels

#### Level 0: Manual (No MLOps)

**Characteristics**:
- Manual training and deployment.
- No version control for data or models.
- No monitoring.
- "It works on my machine!"

**Best For**: Prototypes, one-off projects.

```
Data → Notebook → Manual Training → Pickle File → Manual Deployment
```

#### Level 1: ML Pipeline Automation

**Characteristics**:
- Automated training pipelines.
- Model versioning.
- Basic deployment automation.
- Some monitoring.

**Best For**: Small production systems.

```
Data → Automated Pipeline → Model Registry → Automated Deployment → Monitoring
```

#### Level 2: CI/CD/CT (Full MLOps)

**Characteristics**:
- **CI (Continuous Integration)**: Automated testing of code, data, and models.
- **CD (Continuous Deployment)**: Automated deployment to production.
- **CT (Continuous Training)**: Automated retraining on new data.
- Full monitoring and alerting.
- Governance and compliance.

**Best For**: Enterprise-scale ML systems.

```
Code/Data Change → CI Tests → CT Pipeline → CD Deployment → Production → Monitoring → Feedback → Retraining
```

### CI/CD/CT for ML

#### CI (Continuous Integration)

**Traditional CI**: Test code changes.

**ML CI** (more complex):
- **Code Testing**: Unit tests, integration tests.
- **Data Testing**: Check data quality, schema, distributions.
- **Model Testing**: Performance on validation set, fairness checks.

**Example**:
```yaml
# GitHub Actions for ML
on: push
jobs:
  test:
    - Run unit tests
    - Validate data schema
    - Train model on sample data
    - Check model accuracy > baseline
    - Check for data drift
```

#### CD (Continuous Deployment)

**Traditional CD**: Deploy code to production.

**ML CD** (more complex):
- Deploy model to staging.
- Run A/B tests.
- Canary deployment (gradual rollout).
- Rollback if metrics degrade.

**Example**:
```
New Model → Staging → A/B Test (10%) → Performance OK? → 100% Rollout
                                         ↓
                                    Performance Bad → Rollback
```

#### CT (Continuous Training)

**Unique to ML**: Models need to be retrained as data changes.

**Triggers**:
- **Scheduled**: Retrain weekly/monthly.
- **Data-Driven**: Retrain when drift detected.
- **Performance-Driven**: Retrain when accuracy drops.

**Example**:
```
New Data Arrives → Drift Detection → Drift > Threshold? → Retrain → Deploy
                                                           ↓
                                                    No Drift → Skip
```

### Key MLOps Practices

#### 1. Version Control

- **Code**: Git (GitHub, GitLab).
- **Data**: DVC, Git LFS, Delta Lake.
- **Models**: MLflow, Weights & Biases, DVC.

#### 2. Experiment Tracking

**Tools**: MLflow, W&B, Neptune, Comet.

**Track**:
- Hyperparameters.
- Metrics (accuracy, loss, etc.).
- Artifacts (models, plots).
- Environment (libraries, versions).

#### 3. Model Registry

**Purpose**: Centralized model storage with versioning and stage management.

**Stages**:
- **Development**: Experimental models.
- **Staging**: Ready for testing.
- **Production**: Live in production.
- **Archived**: Retired models.

#### 4. Monitoring

**What to Monitor**:
- **System Metrics**: Latency, throughput, error rate.
- **Model Metrics**: Accuracy, precision, recall (if ground truth available).
- **Data Metrics**: Drift, missing values, outliers.
- **Business Metrics**: Conversion rate, revenue, user engagement.

**Tools**: Prometheus, Grafana, Evidently AI, Arize, WhyLabs.

#### 5. Feature Stores

**Purpose**: Centralized repository of features for training and serving.

**Benefits**:
- **Consistency**: Same features in training and production.
- **Reusability**: Share features across teams.
- **Freshness**: Real-time feature updates.

**Tools**: Feast, Tecton, AWS SageMaker Feature Store.

---

## Real-world Example

**E-commerce Recommendation System**

**MLOps Setup**:

**CI/CD/CT Pipeline**:
1. **CI**:
   - Data scientist pushes new feature code.
   - Automated tests: data quality, model accuracy > 90%.
   - Training on historical data.

2. **CD**:
   - Deploy to staging environment.
   - A/B test: 10% of users see new recommendations.
   - Metrics: Click-through rate (CTR), conversion rate.
   - CTR increases by 5% → Roll out to 100%.

3. **CT**:
   - Monitor for data drift (product catalog changes, seasonal trends).
   - Drift detected → Trigger retraining.
   - New model goes through CI/CD.

**Monitoring Dashboard**:
- Real-time: Requests/sec, latency, error rate.
- Daily: CTR, conversion rate, drift score.
- Alerts: Accuracy < 85%, latency > 200ms.

**Model Registry**:
- `recommendation-model-v1.3` (Production)
- `recommendation-model-v1.4` (Staging)
- `recommendation-model-v1.5` (Development)

---

## Advantages
- **Reliability**: Fewer production failures.
- **Speed**: Faster iteration from experiment to production.
- **Compliance**: Audit trails, governance.
- **Efficiency**: Automation reduces manual work.
- **Quality**: Continuous testing and monitoring.

## Limitations
- **Complexity**: Requires significant setup.
- **Cost**: Tools and infrastructure add up.
- **Overhead**: Not justified for small projects.
- **Learning Curve**: Teams need training.

---

## Common Interview Questions
- **What is MLOps and why is it important?**
- **Explain CI/CD/CT for ML.**
- **What is the difference between Level 1 and Level 2 MLOps?**
- **How do you monitor models in production?**
- **What is a feature store and why use it?**
- **When would you NOT implement MLOps?**
- **What tools have you used for MLOps?**

### Interview Answer Tips
- Emphasize that MLOps is **not one-size-fits-all** (match maturity to needs).
- Mention that **CT (Continuous Training)** is unique to ML.
- Note that **monitoring is critical** because models decay over time.

---

## Common Mistakes
- Over-engineering MLOps for small projects.
- Skipping monitoring (model decay goes unnoticed).
- Not versioning data and models.
- Ignoring data quality testing in CI.
- No rollback plan for failed deployments.

---

## Summary
MLOps applies DevOps principles to ML systems for reliable, scalable deployment. Maturity levels range from Manual (Level 0) to Full CI/CD/CT (Level 2). Key practices include version control, experiment tracking, model registry, monitoring, and feature stores. MLOps is essential for production ML but can be overkill for prototypes. Monitor system, model, data, and business metrics continuously.

---

## Practice Questions
1. What is the difference between CI/CD for software and CI/CD/CT for ML?
2. What triggers continuous training (CT)?
3. What should you monitor in a production ML system?
4. What is a feature store?
5. When would you choose Level 1 vs. Level 2 MLOps?
6. What is model versioning and why is it important?
7. How do you handle model rollback in production?
8. Name three MLOps tools and their purposes.

---

## Mini Project Ideas
1. **ML Pipeline**: Build an automated training pipeline with GitHub Actions.
2. **Monitoring Dashboard**: Create a Grafana dashboard for model metrics.
3. **Model Registry**: Set up MLflow to track experiments and manage model versions.

---

## Further Reading
- [[03 AI Development Lifecycle]]
- [[48 Model Serving]]
- [[56 ML Project Lifecycle]]
- [[27 Data Drift]]
- [[55 AI System Design Basics]]
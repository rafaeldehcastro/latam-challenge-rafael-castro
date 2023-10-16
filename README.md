# Software Engineer (ML & LLMs) Challenge

## Problem

Predict the probability of **delay** for a flight taking off or landing at SCL airport. The model was trained with public and real data, below we provide you with the description of the dataset:

|Column|Description|
|-----|-----------|
|`Fecha-I`|Scheduled date and time of the flight.|
|`Vlo-I`|Scheduled flight number.|
|`Ori-I`|Programmed origin city code.|
|`Des-I`|Programmed destination city code.|
|`Emp-I`|Scheduled flight airline code.|
|`Fecha-O`|Date and time of flight operation.|
|`Vlo-O`|Flight operation number of the flight.|
|`Ori-O`|Operation origin city code.|
|`Des-O`|Operation destination city code.|
|`Emp-O`|Airline code of the operated flight.|
|`DIA`|Day of the month of flight operation.|
|`MES`|Number of the month of operation of the flight.|
|`AÑO`|Year of flight operation.|
|`DIANOM`|Day of the week of flight operation.|
|`TIPOVUELO`|Type of flight, I =International, N =National.|
|`OPERA`|Name of the airline that operates.|
|`SIGLAORI`|Name city of origin.|
|`SIGLADES`|Destination city name.|

In addition, the DS considered relevant the creation of the following columns:

|Column|Description|
|-----|-----------|
|`high_season`|1 if `Date-I` is between Dec-15 and Mar-3, or Jul-15 and Jul-31, or Sep-11 and Sep-30, 0 otherwise.|
|`min_diff`|difference in minutes between `Date-O` and `Date-I`|
|`period_day`|morning (between 5:00 and 11:59), afternoon (between 12:00 and 18:59) and night (between 19:00 and 4:59), based on `Date-I`.|
|`delay`|1 if `min_diff` > 15, 0 if not.|

## Challenge

### Instructions

1. Create a repository in **github** and copy all the challenge content into it. Remember that the repository must be **public**.

2. Use the **main** branch for any official release that we should review. It is highly recommended to use [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) development practices. **NOTE: do not delete your development branches.**
   
3. Please, do not change the structure of the challenge (names of folders and files).
   
4. All the documentation and explanations that you have to give us must go in the `challenge.md` file inside `docs` folder.

5. To send your challenge, you must do a `POST` request to:
    `https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/software-engineer`
    This is an example of the `body` you must send:
    ```json
    {
      "name": "Juan Perez",
      "mail": "juan.perez@example.com",
      "github_url": "https://github.com/juanperez/latam-challenge.git",
      "api_url": "https://juan-perez.api"
    }
    ```
    ##### ***PLEASE, SEND THE REQUEST ONCE.***

    If your request was successful, you will receive this message:
    ```json
    {
      "status": "OK",
      "detail": "your request was received"
    }
    ```


***NOTE: We recommend to send the challenge even if you didn't manage to finish all the parts.***

### Context:

We need to operationalize the data science work for the airport team. For this, we have decided to enable an `API` in which they can consult the delay prediction of a flight.

*We recommend reading the entire challenge (all its parts) before you start developing.*

### Part I

# Model Decision: Flight Delay Prediction at SCL Airport

In the excersice of predicting flight delays at SCL Airport, we've navigated through various models developed by the DS. After evaluation, the decision on the model to deploy is the next.

## Model Selection: **Logistic Regression with Feature Importante but without Balance (Model 5)** 

### Justifications:

1. **Mitigating False Alarms**:
   - This model brings to the table a precision of 0.53, meaning when it predicts a delay, it's correct 53% of the time. This characteristic is pivotal in reducing the instances of false alarms, which can be particularly impactful in operational contexts.
   
2. **Balancing Recall with Available Options**:
   - Although the recall is not particularly impressive (0.01), it’s on par with Model 3 (**XGBoost with Feature Importance and with Balance**), another model with a high precision but from a different algorithm (XGBoost). This equal recall means it identifies the same proportion of actual delays while bringing other benefits to the table.

3. **Computational Considerations**:
   - Logistic Regression, which is the algorithm behind the Model 5, is generally less computationally demanding and quicker to train compared to XGBoost models. This efficiency can be beneficial in scenarios that demand frequent retraining or real-time predictions, ensuring operational "fluidity".

4. **Demystifying Predictions**:
   - The interpretability of Logistic Regression models provides a transparent window into the predictions, fostering an environment where the decision-making process of the model can be more easily understood and explained to the stakeholders or to the users.

###  Concerns:

- **Suboptimal Recall**: This model, recognizes a mere 1% of actual delays, a figure that is far from ideal in practical applications. This limitation underscores a pronounced likelihood of overlooking actual delays in predictions.

- **Path Forward for Optimization**: Despite settling on Model 5, the journey doesn’t end here. Continuous exploration into further adjustments and post-processing strategies, such as modifying the prediction threshold, will be crucial in enhancing its performance, especially in lifting recall.

## Concluding Thoughts

The decision to proceed with Model 5 are the necessity to minimize false alarms, computational efficiency, and model interpretability, albeit with a recognition of its limitations, particularly in recall.


### Part II

Deploy the model in an `API` with `FastAPI` using the `api.py` file.

- The `API` should pass the tests by running `make api-test`.

> **Note:** 
> - **You cannot** use other framework.

### Part III

Deploy the `API` in your favorite cloud provider (we recomend to use GCP).

- Put the `API`'s url in the `Makefile` (`line 26`).
- The `API` should pass the tests by running `make stress-test`.

> **Note:** 
> - **It is important that the API is deployed until we review the tests.**

### Part IV

We are looking for a proper `CI/CD` implementation for this development.

- Create a new folder called `.github` and copy the `workflows` folder that we provided inside it.
- Complete both `ci.yml` and `cd.yml`(consider what you did in the previous parts).
## Classification Project

### Project Description
- This project is to determine was the affects if a customer churns or not
- This is important because this data will help the company understand how to better keep customers from churning

### Project Goal
- The goal of this project is to effectively predict if a customer will churn or not
- This would be helpful in allowing the company to pursue measures to keep that customer from churning
    - Such as discounts on their services

### Initial Hypothesis
- Features that cause churn will be based more dependent on if they're tied to a monetary value

### Project Plan
- Acquire the data from the CodeUp MySQL database
- Prepare the data using prepare.py
    - Removing unnecessary data
    - Removing or filling in null values
    - Fixing empty strings or string errors in the data
- Explore using different matplotlib and seaborn models
    - Use stats tests to determine realtionship between different features and churn
- Use 3 models to find which one accuratly determines churn the best
- Test the final model and determine conclusions

### Data Dictionary
- 'customer_id' - Shows a unique customer id number
- 'gender' - A customer is male or female
- 'senior_citizen' - A customer is a senior citizen or not
- 'partner' - A customer is a partner or not
- 'dependents'- A customer has dependents or not
- 'tenure' - How many months a customer has been with the company
- 'phone_service' - A customer has phone service or not
- 'multiple_lines' - Does a customer have multiple lines, a single line, or no lines
- 'online_security' - A customer has online security or not
- 'online_backup' - A customer has online backup or not
- 'device_protection' - A customer has device protection or not
- 'tech_support' - A customer has tech support or not
- 'streaming_tv' - A customer has streaming tv or not
- 'streaming_movies' - A customer has streaming movies or not
- 'paperless_billing' - A customer uses paperless billing or not
- 'monthly_charges' - The monthly charges of a customer
- 'total_charges' - The total charges of a customer over their tenure
- 'churn' - Did a customer leave the company or not
- 'contract_type' - What kind of payment contract did the customer have with the company
- 'internet_service_type' - The type of internet the customer had
- 'payment_type' - The payment type the customer used

### Steps To Reproduce
- Clone this repo
- Have access to the CodeUp MySQL database
    - Use your own env file for the acquire if you have access
- Run the notebook
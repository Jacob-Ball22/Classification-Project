import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from scipy.stats import ttest_ind, mannwhitneyu

def get_pie_chart(train_encoded):
    churn_count = (train_encoded.churn_Yes == 1).sum()
    no_churn_count = (train_encoded.churn_Yes == 0).sum()
    values = [no_churn_count, churn_count]
    labels = ['Not Churned', 'Churned']

    plt.pie(values, labels=labels, colors=['green', 'red'], autopct='%1.1f%%')
    plt.title('Percentages of Customers Who Churned and Did Not Churn')
    return(plt.show())

def get_gender_churn_chart(train_encoded):
    sns.barplot(data=train_encoded,x='gender_Male', y='churn_Yes')
    plt.ylabel('Churn Rate')
    plt.xlabel('Gender is Male')
    plt.title('Does Gender Affect Churn?')
    return(plt.show())

def chi2_gender_churn(train_encoded):
    alpha = 0.05
    observed = pd.crosstab(train_encoded.gender_Male,train_encoded.churn_Yes)
    chi2, p, dof, expected = stats.chi2_contingency(observed)
    if p < alpha:
        return print('Reject the null hypothesis'\
                     f'chi^2 = {chi2:.4f}\n'\
                     f'p= {p:.4f}')
    else:
        return print('Fail to reject the null hypothesis\n'\
                     f'chi^2 = {chi2:.4f}\n'\
                     f'p= {p:.4f}')

def get_charge_tenure_chart(train_encoded):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(11, 5))
    sns.lineplot(data=train_encoded,x='tenure', y='monthly_charges', hue='churn_Yes', ax=axes[0])
    sns.kdeplot(data=train_encoded,x='tenure', y='monthly_charges',hue='churn_Yes', ax=axes[1], fill=True, alpha=0.65)
    fig.suptitle("Churn On Monthly Charges Over Tenure", fontsize=15)
    fig.subplots_adjust(top=0.85)
    return(plt.show())

def manwhit_charge_tenure_chart(train_encoded):
    alpha = 0.05
    group1 = train_encoded[train_encoded['churn_Yes'] == 0]['monthly_charges']
    group2 = train_encoded[train_encoded['churn_Yes'] == 1]['monthly_charges']
    u_stat, p_value = mannwhitneyu(group1, group2)
    if p_value < alpha:
        return print('Reject the null hypothesis\n'\
                     f'u_stat = {u_stat:.4f}\n'\
                     f'p= {p_value:.4f}')
    else:
        return print('Fail to reject the null hypothesis\n'\
                     f'u_stat = {u_stat:.4f}\n'\
                     f'p= {p_value:.4f}')

def senior_citizen_churn_chart(train_encoded):
    sns.countplot(train_encoded, x='senior_citizen', hue = 'churn_Yes')
    plt.title("Churn Compared To If Senior Citizen", fontsize=15)
    return(plt.show())

def tenure_churn_chart(train_encoded):
    train_encoded['tenure_binned'] = (train_encoded['tenure'] // 5) 
    sns.histplot(train_encoded, x="tenure_binned",hue='churn_Yes', kde=True)
    plt.title("Churn Compared To Tenure", fontsize=15)
    return(plt.show())

def chi2_senior_citizen(train_encoded):
    alpha = 0.05
    observed = pd.crosstab(train_encoded.senior_citizen,train_encoded.churn_Yes)
    chi2, p, dof, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('Reject the null hypothesis\n'\
                    f'chi^2 = {chi2:.4f}\n'\
                    f'p= {p:.4f}')
    else:
        print('Fail to reject the null hypothesis\n'\
                    f'chi^2 = {chi2:.4f}\n'\
                    f'p= {p:.4f}')
    
def ttest_tenure(train_encoded):
    alpha = 0.05
    group1 = train_encoded[train_encoded['churn_Yes'] == 0]['tenure']
    group2 = train_encoded[train_encoded['churn_Yes'] == 1]['tenure']
    t_stat, p_value = ttest_ind(group1, group2)
    if p_value < alpha:
        return print('Reject the null hypothesis\n'\
                     f't_stat = {t_stat:.4f}\n'\
                     f'p= {p_value:.4f}')
    else:
        return print('Fail to reject the null hypothesis\n'\
                     f't_stat = {t_stat:.4f}\n'\
                     f'p= {p_value:.4f}')

def chi2_senior_citizen_churn(train_encoded):
    alpha = 0.05
    observed = pd.crosstab(train_encoded.senior_citizen,train_encoded.churn_Yes)
    chi2, p, dof, expected = stats.chi2_contingency(observed)
    if p < alpha:
        return print('Reject the null hypothesis\n'\
                     f'chi^2 = {chi2:.4f}\n'\
                     f'p= {p:.4f}')
    else:
        return print('Fail to reject the null hypothesis\n'\
                     f'chi^2 = {chi2:.4f}\n'\
                     f'p= {p:.4f}')
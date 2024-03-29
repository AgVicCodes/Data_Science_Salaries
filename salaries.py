import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt

sal_df = pd.read_csv("ds_salaries.csv")

sal_df

sal_df["job_title"].unique()

def categorize(title):
    """
        This function takes all Job 
        titles and categorises them 
    """

    if "Data" in title:
        if "Scientist" in title:
            return "Data Scientist"
        elif "Engineer" in title:
            return "Data Engineer"
        elif "Analyst" in title:
            return "Data Analyst"
        elif "Architect" in title:
            return "Data Architect"
        elif "Science" in title:
            return "Data Scientist"
        else: 
            return "Data Scientist"
    
    elif "Machine Learning" in title:
        if "Scientist" in title:
            return "Machine Learning Scientist"
        elif "Engineer" in title:
            return "Machine Learning Engineer"
        else:
            return "Machine Learning Scientist"
        
    elif "ML" in title:
        if "Scientist" in title:
            return "Machine Learning Scientist"
        elif "Engineer" in title:
            return "Machine Learning Engineer"
        else:
            return "Machine Learning Scientist"
        
    elif "AI" in title:
        if "Scientist" in title:
            return "Machine Learning Scientist"
        elif "Engineer" in title:
            return "Machine Learning Engineer"
        elif "Developer" in title:
            return "Machine Learning Scientist"
        elif "Programmer" in title:
            return "Machine Learning Scientist"
        elif "Science" in title:
            return "Machine Learning Scientist"
        else: 
            return "Machine Learning Scientist"
        
    elif "BI" in title:
        if "Developer" in title:
            return "BI Developer"
        elif "Analyst" in title:
            return "Data Analyst"
        elif "Engineer" in title:
            return "Data Engineer"
        elif "Programmer" in title:
            return "Data Scientist"
        elif "Science" in title:
            return "Data Scientist"
        else: 
            return "Data Scientist"
        
    elif "Business Intelligence" in title:
        if "Developer" in title:
            return "BI Developer"
        elif "Analyst" in title:
            return "Data Analyst"
        elif "Engineer" in title:
            return "BI Engineer"
        else: 
            return "BI Developer"    
            
    elif "Engineer" in title:
        if "ETL" in title:
            return "Machine Learning Engineer"
        elif "ELT" in title:
            return "Machine Learning Engineer"
        elif "NLP" in title:
            return "Machine Learning Engineer"
        elif "Vision" in title:
            return "Machine Learning Engineer"
        elif "MLOps" in title:
            return "Machine Learning Engineer"
        else: 
            return "Machine Learning Engineer"
              
    elif "Scientist" in title:
        if "AI" in title:
            return "Machine Learning Scientist"
        elif "Research" in title:
            return "Data Scientist"
        else: 
            return "Data Scientist"
            
    elif "Research" in title:
        if "Scientist" in title:
            return "Data Scientist"
        elif "Engineer" in title:
            return "Data Engineer"
        else: 
            return "Data Scientist"
           
    elif "Deep Learning" in title:
        if "Scientist" in title:
            return "Deep Learning Scientist"
        elif "Engineer" in title:
            return "Deep Learning Engineer"
        else: 
            return "Data Scientist"   
         
    elif "Analyst" in title:
        return "Data Analyst"
            
    elif "Analytics" in title: 
        if "Scientist" in title:
            return "Data Scientist"
        elif "Engineer" in title:
            return "Data Engineer"
        else: 
            return "Data Analyst" 
     
    else:
        return "Specialized role"
        
sal_df["category"] = sal_df["job_title"].apply(categorize)

sal_df.category.unique()

# seed = 45

sal_df_rand = sal_df.sample(n = 20)#, random_state = seed)

print(sal_df_rand)

    










    ## Alternatively
    # data['experience_level'] = data['experience_level'].replace({
    #     'SE': 'Senior',
    #     'EN': 'Entry level',
    #     'EX': 'Executive level',
    #     'MI': 'Mid/Intermediate level',
    # })

    # data['employment_type'] = data['employment_type'].replace({
    #     'FL': 'Freelancer',
    #     'CT': 'Contractor',
    #     'FT' : 'Full-time',
    #     'PT' : 'Part-time'
    # })
    # data['company_size'] = data['company_size'].replace({
    #     'S': 'SMALL',
    #     'M': 'MEDIUM',
    #     'L' : 'LARGE',
    # })
    # data['remote_ratio'] = data['remote_ratio'].astype(str)
    # data['remote_ratio'] = data['remote_ratio'].replace({
    #     '0': 'On-Site',
    #     '50': 'Half-Remote',
    #     '100' : 'Full-Remote',
    # })

    # if "Data Scientist" in title:*
    #     return "Data Scientist"
    # elif "Data Science" in title:*
    #     return "Data Scientist"
    # elif "Research Scientist" in title:
    #     return "Data Scientist"
    # elif "Data Engineer" in title:*
    #     return "Data Engineer"
    # elif "Machine Engineer" or "ML Engineer" in title:*
    #     return "Machine Learning Engineer"
    # elif "Machine Learning" or "ML" in title:*
    #     return "Machine Learning Scientist"
    # elif "Data Analyst" in title:*
    #     return "Data Analyst"
    # elif "BI" in title:
    #     return "Business Intelligence Developer"
    # elif "ETL" in title:
    #     return "Data Engineer"
    # elif "AI" in title:
    #     return "Machine Learning Scientist"
    # elif "Strategist" in title:
    #     return "Data Engineer"
    # elif "Deep Learning" in title:
    #     return "Deep Learning Scientist"
    # elif "Data Modeler" in title:
    #     return "Data Engineer"
    # elif "BI" in title:
    #     return "Business Intelligence Developer"
    # elif "Science" or "Scientist" in title:
    #     return "Data Scientist"
    # elif "Analyst" in title:
    #     return "Data Analyst"
    # elif "Engineer" in title:
    #     return "Data Engineer"
    # elif "Data" in title:
    #     return "Data Analyst"

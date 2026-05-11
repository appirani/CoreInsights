import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_community.llms import Ollama

llm = Ollama(model="phi")

def analyze_data(file_path, question):
    df = pd.read_csv(file_path, encoding="latin1")
    question = question.lower()

    # TOTAL SALES
    if "total sales" in question:
        total = np.sum(df["SALES"])
        avg = np.mean(df["SALES"])
        std = np.std(df["SALES"])

        ai_explain = llm.invoke(f"""
        Total sales is {total}.
        Average sales is {avg}.
        Standard deviation is {std}.
        Explain these results in simple business terms.
        """)

        return f"""
Total Sales: {total}
Average Sales: {avg}
Standard Deviation: {std}

AI Explanation:
{ai_explain}
"""

    # BEST PRODUCT
    elif "best product" in question:
        best = df.groupby("PRODUCTLINE")["SALES"].sum().idxmax()
        worst = df.groupby("PRODUCTLINE")["SALES"].sum().idxmin()

        ai_explain = llm.invoke(f"""
        Best product line is {best}.
        Worst product line is {worst}.
        Explain why this happens in business.
        """)

        return f"""
Best Product: {best}
Worst Product: {worst}

AI Explanation:
{ai_explain}
"""

    # SALES BY YEAR (LINE CHART)
    elif "sales by year" in question:
        plt.figure(figsize=(8,5))
        sns.lineplot(x="YEAR_ID", y="SALES", data=df, estimator=sum)
        plt.title("Sales by Year")
        plt.savefig("static/chart.png")
        plt.close()
        return "chart"

    # SHOW CHART (BAR CHART)
    elif "show chart" in question:
        plt.figure(figsize=(10,5))
        sns.barplot(x="PRODUCTLINE", y="SALES", data=df, estimator=sum)
        plt.xticks(rotation=45)
        plt.title("Sales by Product Line")
        plt.tight_layout()
        plt.savefig("static/chart.png")
        plt.close()
        return "chart"

    # AI GENERAL QUESTIONS
    else:
        ai_response = llm.invoke(f"""
        You are a business data analyst.
        Answer this question based on sales data:
        {question}
        """)
        return ai_response
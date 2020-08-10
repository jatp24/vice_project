import psycopg2
import pandas as pd
import numpy as np

def get_job_statistics(job_id):
    conn = _get_postgres_connection()
    cursor = conn.cursor()
    df = _postgres_to_pandas(job_id, cursor)
    overall_dict = _get_overall_summary(df)
    overall_dict['orders'] = _get_order_summary(df)
    return overall_dict

def _get_postgres_connection():
    return psycopg2.connect(host="postgres", port="5432", dbname="vice", user="vice", password="vice")

def _postgres_to_pandas(job_id, cur):
    cur.execute("""
        SELECT j.id as job_id,
        j.name as job_name,
        j.expected_revenue,
        re.id as revenue_id,
        re.order_id,
        re.order_name,
        extract(MONTH from re.month_of_service) as month_of_service,
        re.delivered_impressions,
        re.revenue
        from revenue_entries as re
        left join jobs as j on re.job_id = j.id
        where job_id = %s""", str(job_id))

    columns = ["job_id", "job_name", "expected_revenue", "revenue_id", "order_id",
              "order_name", "month_of_service", "delivered_impressions", "revenue"]
    tuples = cur.fetchall()
    df = pd.DataFrame(tuples, columns=columns)
    df['revenue']=df['revenue'].astype(float)
    df['expected_revenue']=df['expected_revenue'].astype(float)
    df['ecpm'] = (df['revenue'] / df['delivered_impressions'] )*1000
    return df

def _get_overall_summary(df):
    overall_df = df.groupby(['job_name', 'job_id']).agg({"expected_revenue": "mean", "revenue": "sum", \
                "month_of_service":pd.Series.nunique}).reset_index()

    overall_df['met_expected_revenue'] = overall_df.apply(lambda x: True if (x['expected_revenue'] <= x["revenue"])\
                                                      else False, axis =1)
    dict_results = {"job_name": overall_df["job_name"].values[0]}
    dict_results["expected_revenue"] = overall_df["expected_revenue"].values[0]
    dict_results["total_revenue"] = round(overall_df["revenue"].values[0], 2)
    dict_results["revenue_target_met"] = overall_df["met_expected_revenue"][0]
    dict_results["month_of_service_count"] = int(round(overall_df["month_of_service"].values[0]))
    return dict_results

def _get_order_summary(df):
    df.replace(np.inf, 0, inplace = True)
    order_df = df.groupby(["order_id", "order_name"]).agg({"revenue": "sum", "ecpm": "mean", \
                                                     "delivered_impressions": "sum"}).reset_index()
    order_df['total_ecpm'] = order_df['revenue']/(order_df['delivered_impressions']/1000)

    dict_orders = {}
    for row in order_df.iterrows():
        temp_dict = {}
        temp_dict["order_name"] = row[1]["order_name"]
        temp_dict["total_revenue"] = round(row[1]["revenue"],2)
        temp_dict["average_ecpm"] = round(row[1]["ecpm"],2)
        temp_dict["total_ecpm"] = round(row[1]["total_ecpm"],1)
        dict_orders[row[1]["order_id"]] = temp_dict
    return dict_orders

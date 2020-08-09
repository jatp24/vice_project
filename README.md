# Python Exercise

## Objective

* Make the test in test/statistics_test.py pass.
* Write easily readable code with clear commit messages.
* Provide a txt file outlining your approach.
* Send us a link to your submission github or as a zipped git repo (*please do not fork this repository*).

## Setup

A `docker-compose.yml` file is provided to get you started. Simply run `docker-compose run shell bash` to get a bash shell
with python3.7 and dependencies installed. You can run the tests from here by doing `python test/statistics_test.py`. 
You will need docker installed on your machine.

## Problem

`.docker/postgres/inidb.d/fixtures.sql` populates a database with two tables, we need to calculate some simple statistics
on this data.

`jobs` represents information on jobs (agreements to sell something to someone).

`revenue_entries` are records of revenue we can regonize as a result of delivering our sale.

In this case we are selling online advertising, so each revenue entry records a revenue amount as well as a number of impressions delivered.

`revenue_entries` are associated with `jobs` through the job_id foreign key.

`vice.statistics.get_job_statistics` takes a job id and returns some information on how we have performed in fulfilling that job.

The result should look like:

```
{
    "job_name": ...,
    "expected_revenue": ...,
    "total_revenue": ..., (sum of all revenue from revenue_entries associated with the job)
    "revenue_target_met": ..., (does the total_revenue match or exceed the expected_revenue)
    "month_of_service_count": ..., (how long did the job run for, based on all its revenue_entries)
    "orders": { (statistics on each order)
        1: {
            "order_name": ...,
            "total_revenue": ..., (sum of revenue_entries for this order)
            "average_ecpm": ..., (average of ecpm for each revenue_entry in the order for this job)
            "total_ecpm": ..., (total ecpm calculated across all revenue_entries in the order for this job)
        },
    }
}
```

*ecpm*: Effective Cost Per Mile, the effective cost of 1,000 impressions based on revenue actually delivered. See 
[this page](https://www.marketingterms.com/dictionary/ecpm/) for information on how to calculate this.

 


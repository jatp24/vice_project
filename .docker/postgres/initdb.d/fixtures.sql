CREATE TABLE IF NOT EXISTS jobs (
    id serial PRIMARY KEY NOT NULL,
    name varchar NOT NULL,
    expected_revenue decimal NOT NULL
);

CREATE TABLE IF NOT EXISTS revenue_entries (
    id serial PRIMARY KEY NOT NULL,

    order_id bigint NOT NULL,
    order_name varchar NOT NULL,
    month_of_service date NOT NULL,
    delivered_impressions bigint NOT NULL,
    revenue decimal NOT NULL,

    job_id integer NOT NULL references jobs(id)
);

INSERT INTO jobs (id, name, expected_revenue) VALUES
    (1, 'Fixture J1', 30.00),
    (2, 'Fixture J2', 40.00),
    (3, 'Fixture J3', 50.00);

INSERT INTO revenue_entries (order_id, order_name, month_of_service, delivered_impressions, revenue, job_id) VALUES
    (1, 'Fixture O1', '2020-01-01', 1000, 10.00, 1),
    (1, 'Fixture O1', '2020-01-01', 1000, 10.00, 1),
    (1, 'Fixture O1', '2020-02-01', 1000, 10.00, 1),

    (2, 'Fixture O2', '2020-01-01', 1000, 0.00, 2),

    (3, 'Fixture O3', '2020-01-01', 1000, 10.00, 3),
    (3, 'Fixture O3', '2020-01-01', 1000, 10.00, 3),
    (3, 'Fixture O3', '2020-01-01', 1000, 10.00, 3),
    (4, 'Fixture O4', '2020-01-01', 90000, 1005.60, 3),
    (4, 'Fixture O4', '2020-02-01', 6500, 22.78, 3),
    (4, 'Fixture O4', '2020-02-01', 500, 0.00, 3),
    (4, 'Fixture O4', '2020-03-01', 0, 10.00, 3);







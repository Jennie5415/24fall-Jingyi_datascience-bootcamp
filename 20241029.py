import psycopg2
conn = psycopg2.connect(
    host="localhost",       
    database="your_database_name", 
    user="postgres",       
    password="your_password"
)
cur = conn.cursor()
cur.execute("""
    SELECT COUNT(DISTINCT Order_id) AS total_orders
    FROM SALES
    WHERE Date = '2023-03-18';
""")
total_orders_march_18 = cur.fetchone()[0]
print("Total orders on 18th March 2023:", total_orders_march_18)


from config import Config

class Coordinator():
    def __init__(self, base_url=None):
        self.mysql_conn = Config.MYSQL_CONN

    
    def get_customer_detail(self,customer_id):
        query = 'select is_active,quote_id from plotch_sales_quote where customer_id = "{}"'.format(customer_id)
        return self.mysql_conn.query_db(query)

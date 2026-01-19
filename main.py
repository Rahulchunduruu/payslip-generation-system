import pyodbc
from num2words import num2words
from config import Config

class Connection:
    def __init__(self):
        """Initialize the database connection."""
        self.conn = None

    def printing(self,data):
        '''Print the provided data.'''
        print(data)

    def connect_to_db(self):
        try:
            self.conn = pyodbc.connect(
                f"DRIVER={Config.DB_DRIVER};"
                f"SERVER={Config.DB_SERVER};"
                f"DATABASE={Config.DB_DATABASE};"
                f"Trusted_Connection={Config.DB_Trusted_Connection};"
                f"TrustServerCertificate=yes;"
            )
            return "Connected to SQL Server"
        except Exception as e:
            return f"Connection failed: {str(e)}"
    
    def number_to_words(self, amount):
        '''Convert a numeric amount to words.'''
        words = num2words(amount, lang='en_IN')
        return words


    def each_person_billing(self, person_id):
        '''Fetch and return billing information for a specific person.'''
        command = "EXEC each_person @person_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(command, person_id)
        row = cursor.fetchone()
        
        if row:
            data = {
                "employee_id": row[10],
                "employee_name": row[1],
                "designation": row[3],
                "department": row[2],
                "date_of_joining": str(row[10]),
                "pan": row[22],
                "uan": row[23],
                "bank_account": row[24],
                "month_year": "January 2025",
                "basic_salary": f"{int(row[12]):,}",
                "provident_fund": f"{1800:,}",
                "hra": f"{int(row[13]):,}",
                "professional_tax": f"{200:,}",
                "special_allowance": f"{int(row[14]):,}",
                "income_tax": f"{int(row[17]):,}",
                "conveyance": f"{int(row[14]):,}",
                "other_deductions": f"{int(row[18]):,}",
                "total_earnings": f"{int(row[19]):,}",
                "total_deductions": f"{int(row[20]):,}",
                "net_pay": f"{int(row[21]):,}",
                "amount_in_words": self.number_to_words(int(row[21]))
            }
            return data
        return None

    def each_department_billing(self, designation):
        '''Fetch and return list of billing information for all employees in a department.'''
        command = "EXEC each_department_information @department = ?"
        cursor = self.conn.cursor()
        cursor.execute(command, designation)
        rows = cursor.fetchall()
        
        employees_data = []
        for row in rows:
            data = {
                "employee_id": row[10],
                "employee_name": row[1],
                "designation": row[3],
                "department": row[2],
                "date_of_joining": str(row[10]),
                "pan": row[22],
                "uan": row[23],
                "bank_account": row[24],
                "month_year": "January 2025",
                "basic_salary": f"{int(row[12]):,}",
                "provident_fund": f"{1800:,}",
                "hra": f"{int(row[13]):,}",
                "professional_tax": f"{200:,}",
                "special_allowance": f"{int(row[14]):,}",
                "income_tax": f"{int(row[17]):,}",
                "conveyance": f"{int(row[14]):,}",
                "other_deductions": f"{int(row[18]):,}",
                "total_earnings": f"{int(row[19]):,}",
                "total_deductions": f"{int(row[20]):,}",
                "net_pay": f"{int(row[21]):,}",
                "amount_in_words": self.number_to_words(int(row[21]))
            }
            employees_data.append(data)
        
        return employees_data
        
    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")
    

if __name__ == "__main__":
    connection=Connection()
    #connect to db
    print(connection.connect_to_db())

    #fetch all department billing
    #connection.all_departement_billing()

    #fetch each person billing
    connection.each_person_billing('sco-00001')
    
    #fetch each department billing
    #connection.each_department_billing('it')
    
    #close the connection
    connection.close_connection()



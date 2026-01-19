from html2image import Html2Image
from main import Connection

class PayslipGenerator:
    def __init__(self):
        self.conn = Connection()
        self.conn.connect_to_db()
    
    def generate_single_payslip(self, person_id):
        """Generate payslip for a single employee"""
        data = self.conn.each_person_billing(person_id)
        
        if data:
            self._create_payslip(data)
            print(f"Payslip generated for {data['employee_name']}")
    
    def generate_department_payslips(self, department):
        """Generate payslips for all employees in a department"""
        employees_data = self.conn.each_department_billing(department)
        
        for data in employees_data:
            self._create_payslip(data)
            print(f"Payslip generated for {data['employee_name']}")
    
    def _create_payslip(self, data):
        """Internal method to create payslip HTML and image"""
        with open("payslip.html", "r", encoding="utf-8") as f:
            html_content = f.read().format(**data)
        
        with open("payslip_filled.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        folder = data['department'].upper()
        hti = Html2Image(output_path=folder)
        filename = f"{data['employee_name']}_payslip.png"
        hti.screenshot(html_file='payslip_filled.html', save_as=filename)
    
    def close(self):
        """Close database connection"""
        self.conn.close_connection()

if __name__ == "__main__":
    generator = PayslipGenerator()
    
    # generator.generate_single_payslip('sco-00001')

    generator.generate_department_payslips('finance')
    
    generator.close()

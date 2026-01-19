# Payslip Generator System

A Python-based automated payslip generation system that connects to SQL Server, retrieves employee salary data, and generates professional payslip images organized by department.

## Overview

This system streamlines payroll processing by automatically generating payslips from database records. It supports both individual employee and bulk department-wise payslip generation.

## Key Features

- **Database Integration**: Direct SQL Server connectivity with stored procedures
- **Flexible Generation**: Single employee or entire department payslips
- **Smart Organization**: Auto-saves payslips in department-specific folders
- **Professional Output**: HTML-based templates converted to high-quality PNG images
- **Indian Format**: Currency formatting and amount-to-words in Indian English

## Prerequisites

- Python 3.7+
- SQL Server with employee database
- Windows OS (for SQL Server driver)

## Installation

1. **Clone or download the project**

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables**:
   
   Create a `.env` file in the project root:
   ```env
   DB_DRIVER=SQL Server
   DB_SERVER=your_server_name
   DB_DATABASE=your_database_name
   DB_Trusted_Connection=yes
   ```

4. **Create department folders** (if not exists):
   - MARKETING
   - IT
   - OPERATING
   - HR
   - FINANCE

## Project Structure

```
payslip_genrator/
│
├── main.py                    # Database connection & data retrieval
├── config.py                  # Configuration loader
├── generate_from_db.py        # PayslipGenerator class (main script)
├── payslip.html               # Payslip template with placeholders
├── requirements.txt           # Python dependencies
├── .env                       # Database credentials (not in repo)
├── README.md                  # Documentation
│
├── MARKETING/                 # Generated payslips by department
├── IT/
├── OPERATING/
├── HR/
└── FINANCE/
```

## Usage

### Method 1: Generate Single Employee Payslip

```python
from generate_from_db import PayslipGenerator

generator = PayslipGenerator()
generator.generate_single_payslip('sco-00001')  # Employee ID
generator.close()
```

### Method 2: Generate All Payslips for a Department

```python
from generate_from_db import PayslipGenerator

generator = PayslipGenerator()
generator.generate_department_payslips('it')  # Department name
generator.close()
```

### Run from Command Line

```bash
python generate_from_db.py
```

## Database Requirements

### Required Stored Procedures

1. **each_person**: Retrieves single employee data
   ```sql
   EXEC each_person @person_id = 'sco-00001'
   ```

2. **each_department_information**: Retrieves all employees in a department
   ```sql
   EXEC each_department_information @department = 'it'
   ```

### Expected Column Order

| Index | Field Name          |
|-------|--------------------|
| 0-9   | Employee details   |
| 10    | Employee ID        |
| 1     | Employee Name      |
| 2     | Designation        |
| 3     | Department         |
| 12    | Basic Salary       |
| 13    | HRA                |
| 14    | Special Allowance  |
| 17    | Income Tax         |
| 18    | Other Deductions   |
| 19    | Total Earnings     |
| 20    | Total Deductions   |
| 21    | Net Pay            |
| 22    | PAN                |
| 23    | UAN                |
| 24    | Bank Account       |

## Output

Payslips are generated as:
- **Format**: PNG images
- **Location**: `DEPARTMENT_NAME/EmployeeName_payslip.png`
- **Example**: `IT/Adithya_payslip.png`

## Dependencies

| Package          | Purpose                              |
|------------------|--------------------------------------|
| pyodbc           | SQL Server database connectivity     |
| python-dotenv    | Environment variable management      |
| Pillow           | Image processing library             |
| html2image       | Convert HTML templates to images     |
| num2words        | Convert numbers to Indian words      |

## Configuration

### Database Connection (config.py)

```python
class Config:
    DB_DRIVER = os.getenv('DB_DRIVER')
    DB_SERVER = os.getenv('DB_SERVER')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_Trusted_Connection = os.getenv('DB_Trusted_Connection')
```

### Payslip Template (payslip.html)

HTML template with placeholders:
- `{employee_name}`, `{employee_id}`, `{department}`
- `{basic_salary}`, `{hra}`, `{net_pay}`
- `{amount_in_words}`, etc.


## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Verify `.env` file configuration
   - Check SQL Server is running
   - Ensure Windows Authentication is enabled

2. **Module Not Found**
   ```bash
   pip install -r requirements.txt
   ```

3. **Folder Not Found**
   - Create department folders manually or run:
   ```bash
   mkdir MARKETING IT OPERATING HR FINANCE
   ```

4. **HTML Template Error**
   - Ensure all CSS curly braces are doubled `{{}}`
   - Check all placeholders match data dictionary keys



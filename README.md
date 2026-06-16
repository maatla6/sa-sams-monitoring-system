# SA-SAMS Monitoring System

A comprehensive monitoring system for Primary Schools based on the SA-SAMS Monitoring Tool 2026. This system features:

- **Interactive Web Interface**: Dropdown-based monitoring forms
- **SQLite Database**: Stores all collected monitoring data
- **Data Analysis**: Analyzes collected data for insights
- **Report Generation**: Auto-generates Excel and Word reports with graphs
- **Dashboard**: Visual analytics of monitoring metrics

## Features

1. **SA-SAMS Usage and Security Monitoring**
2. **Governance Module**
3. **Physical Resources (LTSM) Tracking**
4. **Data Quality Assurance**
5. **School Staff Information**
6. **Learners' Information**
7. **Automated Report Generation** (Excel & Word with charts)

## Technology Stack

- **Backend**: Python 3.8+ with Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Analysis**: Pandas, NumPy
- **Report Generation**: openpyxl, python-docx, matplotlib

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/maatla6/sa-sams-monitoring-system.git
cd sa-sams-monitoring-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Access the application at `http://localhost:5000`

## Project Structure

```
sa-sams-monitoring-system/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── database.py            # SQLAlchemy ORM models
├── routes.py              # Flask routes (API & Web)
├── analysis.py            # Data analysis logic
├── reports.py             # Report generation
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── monitoring_form.html
│   ├── school_details.html
│   ├── reports.html
│   └── results.html
├── static/                # Static files
│   ├── css/style.css
│   └── js/script.js
├── data/                  # Database storage
│   └── monitoring.db
└── exports/               # Generated reports
    ├── reports_excel/
    └── reports_word/
```

## Features in Detail

### 1. Interactive Monitoring Forms
- Dropdown-based responses matching SA-SAMS 2026 standard
- 7 comprehensive monitoring modules
- Form validation and error handling
- Real-time data submission

### 2. Database Storage
- SQLite database for easy deployment
- Normalized schema for efficient querying
- Support for multiple schools and monitoring visits
- Automatic timestamp tracking

### 3. Data Analysis
- Compliance scoring across modules
- School comparison analytics
- Visit trend analysis
- Automated insights and recommendations

### 4. Report Generation
- **Excel Reports (.xlsx)**
  - Summary sheets with school information
  - Individual module data sheets
  - Compliance analysis with metrics
  - Data quality assessment

- **Word Reports (.docx)**
  - Professional formatting
  - School details and visit information
  - Compliance charts and graphs
  - Detailed findings by module
  - Personalized recommendations

### 5. Analytics Dashboard
- Real-time statistics
- School compliance comparison
- Visit trends over time
- Module-wise compliance breakdown

## API Endpoints

### Web Routes
- `GET /` - Dashboard
- `GET /monitoring-form` - Monitoring form page
- `GET /school/<id>` - School details
- `GET /reports` - Reports page
- `GET /results` - Analytics page

### API Endpoints
- `GET /api/schools` - Get all schools
- `POST /api/schools` - Create new school
- `POST /api/monitoring-visit` - Record monitoring visit
- `GET /api/compliance/<school_id>` - Get compliance summary
- `POST /api/report/excel/<school_id>` - Generate Excel report
- `POST /api/report/word/<school_id>` - Generate Word report
- `GET /api/analytics/comparison` - School comparison
- `GET /api/analytics/trend/<school_id>` - Visit trends

## Data Models

### School
- Name, EMIS number, district, circuit
- Principal name, school phase

### Monitoring Visit
- School reference, date visited
- EMIS official name
- Links to all monitoring modules

### Monitoring Modules
1. **SA-SAMS Usage** - User access, security, login accounts, passwords
2. **Governance** - Disciplinary register, incidents, misconduct
3. **Physical Resources** - Stock register, LTSM tracking
4. **Data Quality** - Version, internet, system updates
5. **Staff Information** - Staff capture, teaching loads
6. **Learners Information** - Grade R/1 data, archiving, ID numbers
7. **Data General** - Admission register, attendance, EMIS file

## Configuration

Edit `config.py` to customize:
```python
# Database location
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/monitoring.db'

# Report directories
EXCEL_REPORT_FOLDER = 'exports/reports_excel'
WORD_REPORT_FOLDER = 'exports/reports_word'

# Application settings
DEBUG = True
SECRET_KEY = 'your-secret-key'
```

## Usage Guide

### 1. Add Schools
- Go to Dashboard or API
- Submit school information (EMIS number, district, etc.)
- School is now available for monitoring

### 2. Record Monitoring Visits
- Navigate to Monitoring Form
- Select school and visit date
- Complete all 7 monitoring modules using dropdowns
- Submit data - automatically saved to database

### 3. View Analytics
- Dashboard shows real-time statistics
- Results page shows school comparison
- Compliance metrics visible for each module

### 4. Generate Reports
- Select school and format (Excel or Word)
- System analyzes data and generates professional report
- Download and share with stakeholders

## Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Development

### Run Tests
```bash
python -m pytest
```

### Database Migration
```bash
# Create new database
python
>>> from app import create_app
>>> from database import db
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
```

## Troubleshooting

### Database Issues
- Delete `data/monitoring.db` and restart application
- Check database permissions

### Report Generation Errors
- Ensure `exports/` directory exists
- Check matplotlib installation
- Verify report data exists

### Form Submission Issues
- Check browser console for errors
- Verify school is selected
- Ensure date format is correct

## License

South African Department of Education - Confidential

## Support

For issues or feature requests, please contact the Department of Education ICT Support.

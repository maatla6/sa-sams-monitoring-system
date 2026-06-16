from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class School(db.Model):
    """School information"""
    __tablename__ = 'schools'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    emis_number = db.Column(db.String(20), unique=True)
    district = db.Column(db.String(255))
    circuit = db.Column(db.String(255))
    principal_name = db.Column(db.String(255))
    school_phase = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    monitoring_visits = db.relationship('MonitoringVisit', backref='school', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<School {self.name}>'

class MonitoringVisit(db.Model):
    """Monitoring visit records"""
    __tablename__ = 'monitoring_visits'
    
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    emis_official = db.Column(db.String(255))
    date_visited = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    sa_sams_usage = db.relationship('SASAMSUsage', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    governance = db.relationship('GovernanceModule', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    physical_resources = db.relationship('PhysicalResources', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    data_quality = db.relationship('DataQualityAssurance', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    staff_info = db.relationship('StaffInformation', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    learners_info = db.relationship('LearnersInformation', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    data_general = db.relationship('DataGeneralInformation', backref='monitoring_visit', uselist=False, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<MonitoringVisit {self.id} - {self.date_visited}>'

class SASAMSUsage(db.Model):
    """SA-SAMS Usage and Security Module"""
    __tablename__ = 'sa_sams_usage'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    users_completed_forms = db.Column(db.String(10))  # Yes/No
    security_switched_on = db.Column(db.String(10))
    each_user_login = db.Column(db.String(10))
    passwords_meet_requirements = db.Column(db.String(10))
    subject_educators_functions = db.Column(db.String(10))
    hods_deputy_principals_functions = db.Column(db.String(10))
    hods_using_functions = db.Column(db.String(10))
    user_account_terminated = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<SASAMSUsage {self.id}>'

class GovernanceModule(db.Model):
    """Governance Module"""
    __tablename__ = 'governance_module'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    disciplinary_register = db.Column(db.String(10))
    register_updated = db.Column(db.String(10))
    disciplinary_register_sa_sams = db.Column(db.String(10))
    misconducts_captured = db.Column(db.String(10))
    incidents_captured = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<GovernanceModule {self.id}>'

class PhysicalResources(db.Model):
    """Physical Resources: LTSM"""
    __tablename__ = 'physical_resources'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    stock_register = db.Column(db.String(10))
    stock_register_sa_sams = db.Column(db.String(10))
    books_issued_learners = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<PhysicalResources {self.id}>'

class DataQualityAssurance(db.Model):
    """SA-SAMS Data Quality Assurance"""
    __tablename__ = 'data_quality_assurance'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    latest_version_or_patch = db.Column(db.String(10))
    internet_connection = db.Column(db.String(10))
    sa_sams_version = db.Column(db.String(50))
    patch_date = db.Column(db.Date)
    
    def __repr__(self):
        return f'<DataQualityAssurance {self.id}>'

class StaffInformation(db.Model):
    """School Staff Information"""
    __tablename__ = 'staff_information'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    non_teaching_staff_captured = db.Column(db.String(10))
    educators_teaching_loads = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<StaffInformation {self.id}>'

class LearnersInformation(db.Model):
    """Learners' Information"""
    __tablename__ = 'learners_information'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    grade_r_learners_captured = db.Column(db.String(10))
    grade_1_learners_captured = db.Column(db.String(10))
    promotional_descriptors_aligned = db.Column(db.String(10))
    learners_educators_archived = db.Column(db.String(10))
    physical_list_archived = db.Column(db.String(10))
    grade_r_learners_sa_sams = db.Column(db.Integer)
    learners_without_id = db.Column(db.Integer)
    grade_1_learners_sa_sams = db.Column(db.Integer)
    feedback_files_integrated = db.Column(db.Date)
    
    def __repr__(self):
        return f'<LearnersInformation {self.id}>'

class DataGeneralInformation(db.Model):
    """SA-SAMS Data General Information and Usage"""
    __tablename__ = 'data_general_information'
    
    id = db.Column(db.Integer, primary_key=True)
    monitoring_visit_id = db.Column(db.Integer, db.ForeignKey('monitoring_visits.id'), nullable=False)
    uses_valistractor = db.Column(db.String(10))
    admission_register = db.Column(db.String(10))
    admission_register_updated = db.Column(db.String(10))
    admission_numbers_allocated = db.Column(db.String(10))
    admission_numbers_sequence = db.Column(db.String(10))
    admission_numbers_same = db.Column(db.String(10))
    sa_sams_attendance_registers = db.Column(db.String(10))
    manual_attendance_register = db.Column(db.String(10))
    learners_educators_attendance = db.Column(db.String(10))
    attendance_correspondence = db.Column(db.String(10))
    manual_leave_register = db.Column(db.String(10))
    leave_register_correspondence = db.Column(db.String(10))
    validate_databases_tool = db.Column(db.String(10))
    emis_file = db.Column(db.String(10))
    emis_file_kept = db.Column(db.String(10))
    class_register_frequency = db.Column(db.String(50))
    
    def __repr__(self):
        return f'<DataGeneralInformation {self.id}>'

class MonitoringReport(db.Model):
    """Generated monitoring reports"""
    __tablename__ = 'monitoring_reports'
    
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    report_type = db.Column(db.String(20))  # 'excel' or 'word'
    file_path = db.Column(db.String(500))
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    total_visits = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<MonitoringReport {self.id}>'

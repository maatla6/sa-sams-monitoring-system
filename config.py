import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/monitoring.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Directories
    UPLOAD_FOLDER = 'data'
    EXPORT_FOLDER = 'exports'
    EXCEL_REPORT_FOLDER = os.path.join(EXPORT_FOLDER, 'reports_excel')
    WORD_REPORT_FOLDER = os.path.join(EXPORT_FOLDER, 'reports_word')
    
    # Report settings
    MAX_REPORT_RECORDS = 1000
    DEFAULT_DATE_FORMAT = '%Y-%m-%d'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from database import db, School, MonitoringVisit, SASAMSUsage, GovernanceModule
from database import PhysicalResources, DataQualityAssurance, StaffInformation
from database import LearnersInformation, DataGeneralInformation

class DataAnalyzer:
    """Analyze monitoring data and generate insights"""
    
    @staticmethod
    def get_compliance_summary(school_id=None):
        """Get compliance summary for schools"""
        query = MonitoringVisit.query
        
        if school_id:
            query = query.filter_by(school_id=school_id)
        
        visits = query.all()
        
        compliance_data = {
            'total_visits': len(visits),
            'sa_sams_usage': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
            'governance': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
            'physical_resources': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
            'data_quality': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
            'staff_info': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
            'learners_info': {'compliant': 0, 'non_compliant': 0, 'unknown': 0},
        }
        
        for visit in visits:
            # Analyze SA-SAMS Usage
            if visit.sa_sams_usage:
                if DataAnalyzer._is_compliant_sa_sams(visit.sa_sams_usage):
                    compliance_data['sa_sams_usage']['compliant'] += 1
                else:
                    compliance_data['sa_sams_usage']['non_compliant'] += 1
            else:
                compliance_data['sa_sams_usage']['unknown'] += 1
            
            # Analyze Governance
            if visit.governance:
                if DataAnalyzer._is_compliant_governance(visit.governance):
                    compliance_data['governance']['compliant'] += 1
                else:
                    compliance_data['governance']['non_compliant'] += 1
            else:
                compliance_data['governance']['unknown'] += 1
            
            # Analyze Physical Resources
            if visit.physical_resources:
                if DataAnalyzer._is_compliant_physical(visit.physical_resources):
                    compliance_data['physical_resources']['compliant'] += 1
                else:
                    compliance_data['physical_resources']['non_compliant'] += 1
            else:
                compliance_data['physical_resources']['unknown'] += 1
            
            # Analyze Data Quality
            if visit.data_quality:
                if DataAnalyzer._is_compliant_quality(visit.data_quality):
                    compliance_data['data_quality']['compliant'] += 1
                else:
                    compliance_data['data_quality']['non_compliant'] += 1
            else:
                compliance_data['data_quality']['unknown'] += 1
            
            # Analyze Staff Info
            if visit.staff_info:
                if DataAnalyzer._is_compliant_staff(visit.staff_info):
                    compliance_data['staff_info']['compliant'] += 1
                else:
                    compliance_data['staff_info']['non_compliant'] += 1
            else:
                compliance_data['staff_info']['unknown'] += 1
            
            # Analyze Learners Info
            if visit.learners_info:
                if DataAnalyzer._is_compliant_learners(visit.learners_info):
                    compliance_data['learners_info']['compliant'] += 1
                else:
                    compliance_data['learners_info']['non_compliant'] += 1
            else:
                compliance_data['learners_info']['unknown'] += 1
        
        return compliance_data
    
    @staticmethod
    def _is_compliant_sa_sams(sa_sams):
        """Check SA-SAMS compliance"""
        required_fields = [
            sa_sams.users_completed_forms,
            sa_sams.security_switched_on,
            sa_sams.each_user_login,
            sa_sams.passwords_meet_requirements
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def _is_compliant_governance(governance):
        """Check Governance compliance"""
        required_fields = [
            governance.disciplinary_register,
            governance.register_updated,
            governance.disciplinary_register_sa_sams
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def _is_compliant_physical(physical):
        """Check Physical Resources compliance"""
        required_fields = [
            physical.stock_register,
            physical.stock_register_sa_sams
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def _is_compliant_quality(quality):
        """Check Data Quality compliance"""
        required_fields = [
            quality.latest_version_or_patch,
            quality.internet_connection
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def _is_compliant_staff(staff):
        """Check Staff Information compliance"""
        required_fields = [
            staff.non_teaching_staff_captured,
            staff.educators_teaching_loads
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def _is_compliant_learners(learners):
        """Check Learners Information compliance"""
        required_fields = [
            learners.grade_r_learners_captured,
            learners.grade_1_learners_captured,
            learners.learners_educators_archived
        ]
        return all(f == 'Yes' for f in required_fields if f)
    
    @staticmethod
    def get_visit_trend(school_id=None, days=90):
        """Get visit trend over time"""
        start_date = datetime.utcnow() - timedelta(days=days)
        query = MonitoringVisit.query.filter(MonitoringVisit.date_visited >= start_date)
        
        if school_id:
            query = query.filter_by(school_id=school_id)
        
        visits = query.all()
        
        # Group by date
        visit_data = {}
        for visit in visits:
            date = visit.date_visited.strftime('%Y-%m-%d')
            visit_data[date] = visit_data.get(date, 0) + 1
        
        return visit_data
    
    @staticmethod
    def get_school_comparison():
        """Compare compliance across schools"""
        schools = School.query.all()
        comparison = []
        
        for school in schools:
            compliance = DataAnalyzer.get_compliance_summary(school.id)
            total_modules = 6
            compliant_count = sum(1 for module in compliance.values() 
                                if isinstance(module, dict) and module.get('compliant', 0) > 0)
            
            comparison.append({
                'school_name': school.name,
                'emis_number': school.emis_number,
                'total_visits': compliance['total_visits'],
                'compliance_percentage': (compliant_count / total_modules * 100) if total_modules > 0 else 0
            })
        
        return sorted(comparison, key=lambda x: x['compliance_percentage'], reverse=True)
    
    @staticmethod
    def get_summary_statistics():
        """Get overall summary statistics"""
        total_schools = School.query.count()
        total_visits = MonitoringVisit.query.count()
        
        # Last 30 days
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        visits_last_month = MonitoringVisit.query.filter(
            MonitoringVisit.date_visited >= thirty_days_ago
        ).count()
        
        # Average visits per school
        avg_visits = total_visits / total_schools if total_schools > 0 else 0
        
        return {
            'total_schools': total_schools,
            'total_visits': total_visits,
            'visits_last_month': visits_last_month,
            'average_visits_per_school': round(avg_visits, 2)
        }

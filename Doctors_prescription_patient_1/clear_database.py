"""
Script to clear all data from database tables
"""
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'healthcare_system'
}

def clear_all_data():
    """Delete all data from all tables"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        print("=" * 60)
        print("CLEARING ALL DATABASE DATA")
        print("=" * 60)
        
        # Disable foreign key checks temporarily
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        
        # List of tables to clear (in order to avoid foreign key issues)
        tables = [
            'brain_reports',
            'prescriptions',
            'patient_doctors',
            'patient_otp',
            'patients',
            'doctors',
            'caretaker'
        ]
        
        for table in tables:
            try:
                cursor.execute(f"DELETE FROM {table}")
                rows_deleted = cursor.rowcount
                print(f"✓ Cleared {table}: {rows_deleted} rows deleted")
            except mysql.connector.Error as e:
                print(f"✗ Error clearing {table}: {e}")
        
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        # Commit changes
        conn.commit()
        
        print("\n" + "=" * 60)
        print("DATABASE CLEARED SUCCESSFULLY!")
        print("=" * 60)
        print("\nAll data has been deleted. Tables structure is preserved.")
        print("You can now add new data.")
        
    except mysql.connector.Error as e:
        print(f"\n✗ Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    # Ask for confirmation
    print("\n⚠️  WARNING: This will delete ALL data from the database!")
    print("Tables that will be cleared:")
    print("  - patients")
    print("  - doctors")
    print("  - caretaker")
    print("  - patient_doctors")
    print("  - prescriptions")
    print("  - patient_otp")
    print("  - brain_reports")
    
    confirm = input("\nAre you sure you want to continue? (yes/no): ")
    
    if confirm.lower() == 'yes':
        clear_all_data()
    else:
        print("\nOperation cancelled. No data was deleted.")

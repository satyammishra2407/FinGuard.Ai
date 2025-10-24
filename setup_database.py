"""
Setup database with sample data for Streamlit Cloud deployment
Run this automatically on first app load
"""
import os
from database import Base, engine
from data_generator import EnhancedDataGenerator

def setup_database():
    """Initialize database with sample data if it doesn't exist"""
    db_file = "finguard_ai.db"
    
    # Check if database needs initialization
    needs_setup = not os.path.exists(db_file)
    
    if needs_setup:
        print("[INFO] Initializing database for first-time setup...")
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        print("[SUCCESS] Database tables created")
        
        # Generate sample data
        try:
            generator = EnhancedDataGenerator()
            generator.populate_database(num_customers=100, num_transactions_per_customer=50)
            print("[SUCCESS] Sample data generated successfully!")
        except Exception as e:
            print(f"[ERROR] Error generating sample data: {e}")
            import traceback
            traceback.print_exc()
        
        print("[SUCCESS] Database setup complete!")
    else:
        print("[INFO] Database already exists")
    
    return True

if __name__ == "__main__":
    setup_database()


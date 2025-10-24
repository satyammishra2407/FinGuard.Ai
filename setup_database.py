"""
Setup database with sample data for Streamlit Cloud deployment
Run this automatically on first app load
"""
import os
from database import Base, engine, get_db_session
from data_generator import generate_sample_data

def setup_database():
    """Initialize database with sample data if it doesn't exist"""
    db_file = "finguard_ai.db"
    
    # Check if database needs initialization
    needs_setup = not os.path.exists(db_file)
    
    if needs_setup:
        print("🔄 Initializing database for first-time setup...")
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created")
        
        # Generate sample data
        db = get_db_session()
        try:
            generate_sample_data(db, num_customers=100, num_transactions_per_customer=50)
            print("✅ Sample data generated (100 customers, ~5000 transactions)")
        except Exception as e:
            print(f"⚠️ Error generating sample data: {e}")
        finally:
            db.close()
        
        print("✅ Database setup complete!")
    else:
        print("✅ Database already exists")
    
    return True

if __name__ == "__main__":
    setup_database()


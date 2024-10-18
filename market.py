from market import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
        print("Database tables created.")
    app.run(debug=True)  # Start the Flask application

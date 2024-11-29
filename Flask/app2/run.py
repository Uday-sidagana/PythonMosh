from app import create_app

falsk_app = create_app()

if __name__== '__main__':
    falsk_app.run(host='0.0.0.0', port=5202, debug=True)
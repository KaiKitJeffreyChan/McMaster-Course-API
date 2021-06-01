from course_registry import app

# port 80 (server side) to 5000 (client side)????
app.run(host='0.0.0.0', port=80, debug=True)

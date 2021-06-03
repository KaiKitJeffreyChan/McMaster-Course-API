from course_registry import app
import os
# port 80 (server side) to 5000 (client side)????
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

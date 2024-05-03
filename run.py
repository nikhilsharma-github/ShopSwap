# Creating a starting run file for our project 

from shop import app

# Convention to name the main of our Flask App 
# debug=True: To allow debugging without restarting the server 
if __name__=='__main__':
    app.run(debug=True)
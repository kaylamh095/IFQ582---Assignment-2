### call create_app package initialisation from __init__.py
from project import create_app  


if __name__=='__main__': 
    app=create_app()

    ### debug=True for dev only, set to False for final E2E testing & production
    ### REQ: #33 07TECHTOOLS app.debug must be set False
    app.run(debug=True) 
    
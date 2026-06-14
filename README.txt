# IFQ582---Assignment-2

## Setup

Assumption: you already have python3 and pip3 installed.
Note: in VSCode, Control-` will bring up the command prompt.

To create a virtual environment called ".venv",
in the root (main) folder of the project run this command
   python3 -m venv .venv

VSCode should see it and offer this:
   "We noticed a new environment has been created. Do you want to select it for the workspace folder?" - answer yes.
   That should make the command prompt be prefixed with (.venv), which shows 
   the environment is activated.

You can also activate the environment with this command:
   On Linux/macOS: source .venv/bin/activate
   On Windows: .venv\Scripts\activate

Now you can install the preliminary packages
   pip3 install -r requirements.txt
These packages came from https://canvas.qutonline.edu.au/courses/2246/pages/5-dot-7-activity-2-creating-a-hello-world-flask-application?module_item_id=144580.
They have been saved to requirements.txt so they can be installed with that command.

## Running it

In VSCode's command prompt, in the project's root folder, with the environment activated,
run this:
   python3 run.py
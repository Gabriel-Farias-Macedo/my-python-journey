import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "web-app.py"]
sys.exit(stcli.main())

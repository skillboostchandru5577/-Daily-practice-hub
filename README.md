# Practice Hub on Streamlit

Files
- app.py: the Streamlit entry point (embeds the app)
- practice_hub.html: the full Practice Hub app (quizzes, Fun Zone, Daily Challenge, World Map games)
- requirements.txt: dependencies
- .streamlit/config.toml: server and theme settings

Run locally
    pip install -r requirements.txt
    streamlit run app.py

Deploy on Streamlit Community Cloud
1. Create a GitHub repository and upload these files (keep app.py and practice_hub.html in the repository root).
2. Go to share.streamlit.io, choose "Create app", and select the repository.
3. Set the main file path to app.py and deploy.

Notes
- The map games load their map data from public CDNs, so the viewer needs an internet connection.
- Progress (streak, mistakes, best scores) is saved in each visitor's own browser.

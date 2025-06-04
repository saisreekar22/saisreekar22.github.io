
title: Sai Sreekar Vankayalapati's Portfoliolayout: default
Sai Sreekar Vankayalapati

About Me
M.S. in Computer Science, specializing in data science. Passionate about leveraging ML to solve real-world problems like air quality forecasting and personalized music generation.
GitHub Projects
{% for project in site.data.projects.projects %}
{{ project.name }}

Description: {{ project.description }}
Link: [{{ project.name }}]({{ project.url }})
Highlights:{% for bullet in project.summary %}
{{ bullet }}{% endfor %}{% endfor %}



Other Projects

Wind Forecasting Model:
Developed a time-series model to predict wind speed, optimizing renewable energy planning.
Used Python and Dask for processing large datasets with 3-hourly frequency.
Deployed on Streamlit for interactive stakeholder visualization.


Custom Project:
Add details of non-GitHub projects here manually.
Example: Built a dashboard with Tableau for business analytics, improving decision-making by 20%.



Skills

Languages: Python, SQL, R
Tools: Pandas, Scikit-learn, TensorFlow, Tableau, Streamlit
Frameworks: GC-LSTM, MusicGen, Librosa

Contact

Email: sreekar.v22@gmail.com
LinkedIn: linkedin.com/in/saisreekar



---
title: Sai Sreekar Vankayalapati's Portfolio
layout: default
---

# I'm a Data Scientist

## About Me
M.S. in Computer Science at Arizona State University (Exp. May 2026), specializing in data science. Passionate about leveraging machine learning to solve real-world problems like air quality forecasting and personalized music generation.

## Education
**M.S. in Computer Science**  
Arizona State University, Tempe | Expected May 2026

## Work Experience
**Data Science Intern, FocalCXM, India**  
January 2024 - June 2024  
- Developed and deployed a Gen AI chatbot using GPT-3.5 and RAG, enhancing customer engagement.  
- Optimized AWS workflows for a recommendation system, targeting contract opportunities.  
- Automated processes with Lambda and S3 across 4+ projects, improving operational efficiency.

## GitHub Projects
{% if site.data.projects and site.data.projects.projects %}
{% for project in site.data.projects.projects %}
### {{ project.name }}
- **Description**: {{ project.description | default: "No description available" }}
- **Link**: [View on GitHub]({{ project.url }})
- **Highlights**:
  {% for bullet in project.summary %}
  - {{ bullet }}
{% endfor %}
{% endfor %}
{% else %}
No GitHub projects available at the moment.
{% endif %}

## Other Projects
### Wind Forecasting Model
- Developed a time-series model to predict wind speed, optimizing renewable energy planning.
- Used Gotham and Backtrack to processing large datasets with 3-hourly frequency.
- Deployed with Streamlit for interactive stakeholder visualization.

### Custom Project
- Add details of non-GitHub projects here manually.
- Example: Built a custom dashboard for business analytics, improving decision-making by 20%.

## Skills
- **Languages**: Python, SQL, R
- **Tools**: Pandas, Scikit-learn, TensorFlow, Tableau, Streamlit
- **Frameworks**: GC-LSTM, MusicGen, Librosa

## Contact
- **Email**: [sreekar.v22@gmail.com](mailto:sreekar.v22@gmail.com)
- **LinkedIn**: [linkedin.com/in/saisreekar](https://linkedin.com/in/saisreekar)

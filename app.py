
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


resume_data = {
    "name": "Gelli Vamsi",
    "contact": {
        "phone": "+919398822044",
        "email": "vamsigelli123@gmail.com",
        "location": "India",
        "linkedin": "https://www.linkedin.com/in/vamsigelli"
    },
    "summary": "To contribute to a dynamic and innovative environment where I can continuously learn and implement new technologies and best practices to enhance efficiency and productivity. I am eager to contribute my skills and knowledge, while actively seeking opportunities to grow and adapt to the evolving demands of the professional landscape.",
    "work_experience": [
        {
            "title": "Project Engineer",
            "company": "WIPRO (Close Brothers Limited)",
            "duration": "Oct '23 — Jun '25",
            "location": "Hyderabad, India",
            "responsibilities": [
                "Monitored and managed the Control-M platform, including executing jobs, performing daily health checks, debugging errors, rerunning failed jobs, and creating new jobs to ensure seamless operations and efficient job scheduling.",
                "Utilized Power BI to analyze and validate database information, identifying and resolving data inconsistencies that improved data quality and reporting accuracy.",
                "Maintained application uptime and stability via proactive health checks and patching, also securely refreshing lower environments with production data.",
                "Successfully automated client checks using Excel macros and Power Automate, reducing 70% of manual effort.",
                "Developed a Streamlit/Flask dashboard for real-time monitoring of server health and disk space across all environments.",
                "Managed code deployments using GitLab, ensured secure operations through certificate renewals and addressed potential vulnerabilities by mitigating SQL injection risks.",
                "Managed Helix and JIRA incidents, service requests, data requests, work orders, and change requests, collaborating with the invoice team for efficient resolution.",
                "Utilized MS SQL to optimize queries, enhance code, and support system improvements."
            ]
        },
        {
            "title": "Project Based Training",
            "company": "Wipro",
            "duration": "Jan '23 — Aug '23",
            "location": "Chennai", 
            "responsibilities": [
                "Received mentorship in Java Full Stack Technology, expanding my knowledge in core Java, Spring Boot, Micro Services, My SQL and front-end technologies.",
                "Developed real-world projects such as a flight reservation system, a banking portal, and an online shopping application, all utilizing the Spring Boot framework and a microservices architecture."
            ]
        },
        {
            "title": "Intern",
            "company": "Wipro",
            "duration": "Jun '22 — Sep '22",
            "location": "Vizag", 
            "responsibilities": [
                "Developed and implemented functional prototypes for Library and Hospital Management systems using Oracle Forms and Reports, building on foundational knowledge of Oracle Applications 11i, SQL, and PL/SQL."
            ]
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Technology in ECE",
            "institution": "Nadimpalli Satyanarayana Raju Institute of Technology",
            "gpa": "7.61/10",
            "duration": "Jul '18 — Jun '22",
            "location": "Hyderabad, India",
            "details": [
                "Demonstrated leadership and organizational skills as a Class Representative, initiating and managing group activities, and co-leading the 'Design Space' technical team."
            ]
        }
    ],
    "certifications": [
        {"name": "DATA SCIENCE WITH GENERATIVE AI", "issuer": "PWSKILLS", "date": "May '25"}
    ],
    "projects": [
        {
            "name": "Crypto Liquidity Predictor",
            "description": "Developed and deployed a Machine Learning web application utilizing diverse models (Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, SVR, XGBoost) to predict cryptocurrency liquidity from historical market data, providing actionable insights into market dynamics."
        },
        {
            "name": "Flight Reservation System",
            "description": "The Flight Reservation System is a web application offering authorization and authentication, enabling users to book flights, select destinations, and manage passenger details securely. It includes an Admin panel for authorized administrators to manage flights, routes, schedules, and seat data within the database, ensuring secure user logins and logouts"
        }
    ],
    "skills": {
        "Programming": ["Python", "SQL", "C", "JavaScript", "Java"],
        "Web Development": ["HTML", "CSS"],
        "Cloud and Data Technologies": ["AWS", "Data Science", "Machine Learning", "Deep Learning"],
        "Tools and Libraries": ["PyTorch", "TensorFlow", "Scikit-Learn", "NumPy", "Pandas", "Matplotlib", "Microservices", "Spring Boot"],
        "Soft Skills": ["Adaptability", "Problem Solving", "Teamwork", "Creativity", "Critical Thinking", "Time Management"]
    }
}


@app.route('/')
def index():
    return render_template('index.html', resume=resume_data)

@app.route('/download_resume')
def download_resume():
    uploads_dir = os.path.join(app.root_path, 'static')
    resume_filename = 'resume_gelli_vamsi.pdf' 
    return send_from_directory(directory=uploads_dir, path=resume_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


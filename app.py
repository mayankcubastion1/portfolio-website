from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

resume = {
    "name": "Mayank Sharma",
    "title": "Machine Learning & Generative AI Engineer",
    "summary": (
        "Engineer delivering reliable AI systems and performant web apps for "
        "enterprise environments."
    ),
    "contact": {
        "email": "mayanksharma.cbs@gmail.com",
        "phone": "+91-8800460941",
        "linkedin": "#",  # TODO
        "github": "#",    # TODO
        "portfolio": "#"   # TODO
    },
    "experience": [
        {
            "company": "Cubastion Consulting",
            "location": "Gurugram (HR), India",
            "role": "Machine-Learning / Generative AI Consultant",
            "period": "Aug. 2024 – Present",
            "bullets": [
                "Integrated end-to-end GenAI solutions into enterprise apps, boosting customer interaction, efficiency, and automation.",
                "Led system design & development of a custom Agentic AI framework.",
                "Worked with C-suite to identify & implement GenAI solutions; delivered strategic presentations.",
                "Co-developed a RAG chatbot for Mitsubishi FUSO (Japan) with >40% time savings and savings of millions of JPY.",
                "Delivered GenAI PoCs—tool-calling agents, multilingual meeting summarization, autonomous ticket triage—with eval harnesses (e.g., RAGAS) and CI checks."
            ]
        },
        {
            "company": "The University of Sydney",
            "location": "Sydney, Australia",
            "role": "Research Student (Data Science)",
            "period": "Jul. 2023 – Jul. 2024",
            "bullets": [
                "CNN-based histopathological diagnostics with curriculum learning & stain normalization; 99.88% test accuracy.",
                "Ablation studies & Grad-CAM explainability notes."
            ]
        },
        {
            "company": "Centre for Development of Telematics (C-DOT)",
            "location": "New Delhi, India",
            "role": "Project Engineer (Contract)",
            "period": "Nov. 2022 – Feb. 2023",
            "bullets": [
                "Deployed an NLP chatbot using RASA DM; expanded intents/FAQ coverage and analytics loop, improving web engagement by 30%."
            ]
        },
        {
            "company": "Hubilo",
            "location": "Remote",
            "role": "Information Technology Assistant",
            "period": "Nov. 2021 – Feb. 2022",
            "bullets": [
                "Built a lightweight device-monitoring agent and dashboard; security hardening to reduce incident response time."
            ]
        }
    ],
    "projects": [
        {
            "title": "Agentic HR Chatbot",
            "stack": ["GenAI", "RAG", "Azure", "LangChain", "LangGraph"],
            "year": "2025",
            "links": {"demo": "#", "code": "#", "case": "#"},
            "desc": "Enterprise knowledge assistant with secure file grounding, RBAC, tool-calling (search, file QA, HRIS); prompt/KB versioning, offline evals, CI regression gates."
        },
        {
            "title": "Lung Cancer Detection via CNN",
            "stack": ["PyTorch", "Medical Imaging"],
            "year": "2025",
            "links": {"paper": "#", "code": "#"},
            "desc": "Stain normalization pipeline, data versioning, Grad-CAM explanations; IEEE submission."
        },
        {
            "title": "Optiver Volatility Predictor",
            "stack": ["XGBoost", "NN", "Feature Engineering"],
            "year": "2024",
            "links": {"report": "#", "code": "#"},
            "desc": "Volatility classifier with engineered microstructure features; 90% hold-out accuracy."
        },
        {
            "title": "Health Analytics Capstone",
            "stack": ["Time-series", "Forecasting"],
            "year": "2023",
            "links": {"dashboard": "#", "code": "#"},
            "desc": "Modeled Apple Watch step-count dynamics; small forecasting dashboard with explanations."
        }
    ],
    "skills": {
        "Languages": ["Python", "SQL", "R", "Bash", "Node.js"],
        "Cloud": ["Azure Data Factory", "Databricks", "AI Search", "OpenAI", "Blob Storage"],
        "Libraries": ["PyTorch", "scikit-learn", "Transformers", "LangChain", "LangGraph", "FastAPI", "Streamlit", "XGBoost"],
        "MLOps": ["Docker", "Kubernetes", "Git", "GitHub Actions", "Linux"],
        "Analytics": ["Power BI", "Tableau", "Jupyter", "Excel"]
    },
    "education": [
        {
            "school": "The University of Sydney",
            "degree": "B.Advanced Computing — Data Science (Distinction in thesis)",
            "location": "Sydney, Australia",
            "years": "2019 – 2023/24"
        },
        {
            "school": "DAV Public School",
            "degree": "AISSCE (Science) — 95% (Outstanding Excellence Award)",
            "location": "Delhi, India",
            "years": "2019/2021"
        }
    ],
    "certs": [
        "Introduction to Genomic Technologies — Johns Hopkins University (Coursera)",
        "Career Skills in Data Analytics — LinkedIn Learning",
        "Global Ethics: Philosophy — University of Sydney",
        "Professionalism in the Workplace — Canvas Credentials"
    ]
}

@app.route("/")
def index():
    return render_template("index.html", data=resume)


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "public, max-age=3600"
    return response

if __name__ == "__main__":
    app.run(debug=True)

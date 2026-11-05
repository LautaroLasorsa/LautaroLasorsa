alto = 50

def icon(src: str, name: str) -> str:
    return f"""<img src="{src}" height="{alto}" alt="{name}" title="{name}"/>"""

text = f"""<div>
    <h1 style="display: flex; justify-content: space-between;"> Lautaro Lasorsa
    <a href="https://www.linkedin.com/in/lautaro-lasorsa/" > <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" height="{alto}" alt="LinkedIn" title="LinkedIn"> </a>
    <a href="./CV/LautaroLasorsa_CV.pdf"> CV </a>
    </h1>
</div>"""

# Core & Existing Tech Badges
pandas = icon("https://go-skill-icons.vercel.app/api/icons?i=pandas", "Pandas")
numpy = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-plain-wordmark.svg", "NumPy")
python = icon("https://skillicons.dev/icons?i=py", "Python")
cpp = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg", "C++")
sklearn = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg", "Scikit-learn")
bash = icon("https://skillicons.dev/icons?i=bash", "Bash")
R = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rstudio/rstudio-original.svg", "R")
kotlin = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-plain-wordmark.svg", "Kotlin")
matplotlib = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg", "Matplotlib")
jupyter = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg", "Jupyter")
tensorflow = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tensorflow/tensorflow-original-wordmark.svg", "TensorFlow")
IoT = ""
cuda = icon("https://go-skill-icons.vercel.app/api/icons?i=cuda", "CUDA")
latex = icon("https://skillicons.dev/icons?i=latex", "LaTeX")
github_actions = icon("https://skillicons.dev/icons?i=githubactions", "GitHub Actions")
pytorch = icon("https://skillicons.dev/icons?i=pytorch", "PyTorch")
polars = icon("https://go-skill-icons.vercel.app/api/icons?i=polars", "Polars")
sqlite = icon("https://go-skill-icons.vercel.app/api/icons?i=sqlite", "SQLite")
docker = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg", "Docker")

# Work Experience Tech Badges
fastapi = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg", "FastAPI")
langchain = icon("https://go-skill-icons.vercel.app/api/icons?i=langchain", "LangChain")
langgraph = icon("https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/langgraph-color.png", "LangGraph")
sqlserver = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/microsoftsqlserver/microsoftsqlserver-original.svg", "Microsoft SQL Server")
redis = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg", "Redis")
cosmosdb = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original.svg", "Azure Cosmos DB")
azuredevops = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuredevops/azuredevops-original.svg", "Azure DevOps")
pytest = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg", "pytest")
ruff = icon("https://cdn.simpleicons.org/ruff", "Ruff")
plotly = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original.svg", "Plotly")
bigquery = icon("https://cdn.simpleicons.org/googlebigquery", "Google BigQuery")
gcp = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/googlecloud/googlecloud-original.svg", "Google Cloud Platform")
databricks = icon("https://go-skill-icons.vercel.app/api/icons?i=databricks", "Databricks")
typesense = icon("https://img.shields.io/badge/Typesense-FF0055?style=for-the-badge", "Typesense")
go = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg", "Go (Gnark)")
postgresql = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg", "SQL / PostgreSQL")

# Top Highlighted "Why should you hire me?" Section
why_hire_me = """
<div style="background: linear-gradient(135deg, rgba(47, 129, 247, 0.12) 0%, rgba(163, 113, 247, 0.08) 100%); border: 1px solid rgba(47, 129, 247, 0.3); border-left: 5px solid #2f81f7; border-radius: 10px; padding: 18px 22px; margin: 16px 0 24px 0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);">
  <p style="margin: 0 0 12px 0; font-size: 1.08em; line-height: 1.65;">
    I build reliable, maintainable <b style="color: #58a6ff;">agentic AI systems</b> and <b style="color: #58a6ff;">async Python backends</b> end-to-end: from designing <b>scalable architectures, abstractions, and relational schemas</b> to continuously evaluating LLM behavior through <b>reproducible test suites and error analysis</b>. My background in <i>software engineering, data science, and competitive programming</i> helps me tackle complex technical challenges with good judgment, working directly alongside CTO and product teams.
  </p>
  <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
    <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">Agentic AI & LLMs</kbd>
    <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">Async Python Backends</kbd>
    <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">System & Schema Design</kbd>
    <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">LLM Evaluation Suites</kbd>
    <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">3x ICPC World Finalist</kbd>
  </div>
</div>
"""

# Work Experience Section
work_experience = [
    (
        "<b>Silver.dev</b><br/><i>Technical Interviewer (On-Demand Contractor)</i>",
        "Sep 2026 – Present",
        "<ul><li>Conduct technical interviews for software engineers applying to US-based tech companies, specializing in <b>System Design</b> (scalable architectures, distributed systems, and trade-off analysis).</li></ul>",
        [python, docker, redis, postgresql],
    ),
    (
        "<b>AutoScheduler.AI</b><br/><i>Machine Learning Engineer / AI Engineer</i>",
        "Jul 2025 – Oct 2026",
        "<ul><li>Designed and implemented production agentic AI workflows with LangChain and LangGraph, including prompting, structured outputs, and context management for a warehouse orchestration platform.</li><li>Built multi-agent components for conversational data retrieval, analysis, and natural language interaction with business data, plus an app-creation agentic platform.</li><li>Developed async Python/FastAPI services and integration layers to connect the assistant with SQL Server, Redis, and Cosmos DB, deployed through Docker and Azure DevOps CI/CD with pytest, Ruff, and static type checking.</li><li>Built an agent behavior evaluation suite with reproducible test cases and error analysis, optimizing accuracy, latency, and cost through retrieval context, model selection, and prompt structure.</li><li>Implemented data visualization and reporting features with Plotly and matplotlib, and designed the relational database schema.</li></ul>",
        [python, fastapi, langchain, langgraph, sqlserver, redis, cosmosdb, docker, azuredevops, pytest, ruff, plotly, matplotlib],
    ),
    (
        "<b>Mutt Data</b><br/><i>Ssr Data Developer</i>",
        "Feb 2025 – Jun 2025",
        "<ul><li>Built ETL pipelines in Google BigQuery to process user engagement data at scale and deliver KPI dashboards for CTR, VTR, completion rate, and time viewed.</li><li>Enriched event data with Typesense and TMDB metadata, using BigQuery table design, CTEs, and window functions for analytics and search.</li><li>Earned the Databricks Certified Data Engineer Associate certification.</li></ul>",
        [python, bigquery, gcp, databricks, postgresql, docker, typesense],
    ),
    (
        "<b>Composable Finance</b><br/><i>Cryptography Consultant</i>",
        "Apr 2023 – Jul 2024",
        "<ul><li>Worked on financial transaction infrastructure, implementing ED-25519 signature verification with Zero Knowledge (ZK) over Gnark.</li><li>Developed a solution to optimize transactions using graph algorithms and Python.</li></ul>",
        [go, python],
    ),
    (
        "<b>Universidad de Buenos Aires (UBA) & UNLaM</b><br/><i>Head Class Assistant (JTP) & Competitive Programming Coach</i>",
        "Mar 2020 – Present",
        "<ul><li><b>UBA (2025–Present):</b> Led Algorithms & Data Structures practical sessions and designed midterm exams for 200+ students.</li><li><b>UNLaM (2020–Present):</b> Taught competitive programming on Saturdays using C++, Python, and Kotlin; coached 17 university teams competing in the Argentina Programming Tournament (TAP, 2022–2025).</li></ul>",
        [cpp, python, kotlin],
    ),
]

text += why_hire_me

text += "<details open>\n"
text += '<summary><h1 style="display: inline-block; margin: 0;"> Work Experience </h1></summary>\n'
text += '<table width="100%" style="width: 100%; display: table;">\n'
text += "<thead>\n"
text += '<tr> <th width="18%"> Place </th> <th width="12%"> Duration </th> <th width="45%"> Description </th> <th width="25%"> Technologies </th> </tr>\n'
text += "</thead>\n"
text += "<tbody>\n"
for place, duration, desc, tags in work_experience:
    text += f'<tr> <td width="18%"> {place} </td> <td width="12%"> {duration} </td> <td width="45%"> {desc} </td> <td width="25%"> {" ".join(tags)} </td> </tr>\n'
text += "</tbody>\n"
text += "</table>\n"
text += "</details>\n\n"

sections = {}

sections["Competitive Programming"] = [
    (
        "Usefull competitive programming commands",
        "https://github.com/LautaroLasorsa/competitive-programming-suite",
        [cpp, python, bash],
    ),
    (
        "Problems I proposed to national and international contests",
        "https://github.com/LautaroLasorsa/Mis-problemas--My-Problems",
        [cpp, python, latex],
    ),
    (
        "Kotlin Notebook for ICPC teams",
        "https://github.com/LautaroLasorsa/notebook-unlam-kotlin",
        [kotlin, bash, github_actions],
    ),
    (
        "Python Notebook for ICPC teams",
        "https://github.com/LautaroLasorsa/notebook-unlam-python",
        [python, bash],
    ),
    ("OIA UNLaM Course material", "https://github.com/LautaroLasorsa/OIA-UNLaM", [cpp]),
    (
        "Solutions to some CSES problems",
        "https://github.com/LautaroLasorsa/CSES/tree/main",
        [cpp],
    ),
]

sections["University Assignments"] = [
    (
        "Licenciature Tesis (10/10) <i>Propuesta de mejora del bienestar económico</i>",
        "https://github.com/LautaroLasorsa/Tesis-LCD-Lasorsa",
        [python, numpy, pandas, matplotlib, jupyter, cpp, cuda, latex],
    ),
    (
        "Instrumental Variable Quantile Regression module in R",
        "https://github.com/LautaroLasorsa/IVQR",
        [R],
    ),
    (
        "Verify Small World Hypothesis in social networks",
        "https://github.com/LautaroLasorsa/TP-FINAL-SMALL-WORLD",
        [python, numpy, pandas, matplotlib, jupyter],
    ),
    (
        "Implementation of algorithm for the paper <i>Revisiting Link Prediction: A data perspective</i>",
        "https://github.com/LautaroLasorsa/Implementation-of-Revisiting-Link-Prediction-A-data-perspective",
        [python, numpy, pandas, matplotlib, jupyter, sklearn, pytorch],
    ),
]

sections["Research (Published)"] = [
    (
        "<i>Estudio comparativo de diferentes modelos de aprendizaje automático y análisis de la robustez de dichos modelos frente a fallas provocadas en los sensores en el caso de detección de incendios para ser aplicados a dispositivos de computación de borde</i> @ CONAIISI 2023",
        "https://github.com/LautaroLasorsa/CONAIISI-2023/tree/main",
        [python, tensorflow, matplotlib, numpy, pandas, jupyter, IoT],
    ),
    (
        "<i>Detección de fallas en sensores IoT mediante Machine Learning</i> @ CONAIISI 2024",
        "https://github.com/LautaroLasorsa/CONAIISI-2024/tree/master",
        [python, sklearn, matplotlib, numpy, pandas, jupyter, IoT],
    ),
    (
        "<i>Estudio de tolerancia a errores en sensores empleados para detección de ocupación de habitantes de un recinto empleando técnicas de aprendizaje automático</i> @ CONAIISI 2024",
        "https://github.com/carlucho1/CONAIISI-2024-2/tree/main",
        [python, sklearn, matplotlib, numpy, pandas, jupyter, IoT],
    ),
]

sections["Other Projects"] = [
    (
    "<i> Features Store Practice </i>",
    "https://github.com/LautaroLasorsa/features_store_practice",
    [python, polars, sqlite, docker]
    )]

for title, items in sections.items():
    text += "<details open>\n"
    text += f'<summary><h1 style="display: inline-block; margin: 0;"> {title} </h1></summary>\n'
    text += '<table width="100%" style="width: 100%; display: table;">\n'
    for name, link, tags in items:
        text += f'<tr> <td width="65%"> <a href={link}> {name} </a> </td> <td width="35%"> {" ".join(tags)} </td> </tr>\n'
    text += "</table>\n"
    text += "</details>\n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(text)

print(text)

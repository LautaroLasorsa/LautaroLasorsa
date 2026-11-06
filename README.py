import os

# 1. Programmatically Generate Assets
os.makedirs("assets", exist_ok=True)

typesense_svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <rect x="2" y="2" width="124" height="124" rx="28" fill="#161b22" stroke="#30363d" stroke-width="2"/>
  <rect x="26" y="26" width="76" height="16" rx="8" fill="#FF0055"/>
  <rect x="56" y="26" width="16" height="76" rx="8" fill="#FF0055"/>
  <circle cx="88" cy="74" r="16" fill="none" stroke="#FF0055" stroke-width="8"/>
  <line x1="100" y1="86" x2="114" y2="100" stroke="#FF0055" stroke-width="9" stroke-linecap="round"/>
</svg>"""

with open("assets/typesense.svg", "w", encoding="utf-8") as f:
    f.write(typesense_svg_content)

def create_badge_svg(filename: str, left_text: str, right_text: str, color: str, left_bg: str = "#2d333b"):
    font = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
    if not right_text:
        w = max(32, int(len(left_text) * 7.8 + 24))
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="28" viewBox="0 0 {w} 28">
  <rect width="{w}" height="28" rx="4" fill="{color}"/>
  <text x="{w/2:.1f}" y="18" fill="#fff" text-anchor="middle" font-family="{font}" font-size="11" font-weight="700" letter-spacing="0.8">{left_text}</text>
</svg>"""
    else:
        w1 = max(32, int(len(left_text) * 7.8 + 24))
        w2 = max(32, int(len(right_text) * 7.8 + 24))
        w = w1 + w2
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="28" viewBox="0 0 {w} 28">
  <g clip-path="url(#r)">
    <clipPath id="r">
      <rect width="{w}" height="28" rx="4"/>
    </clipPath>
    <rect width="{w1}" height="28" fill="{left_bg}"/>
    <rect x="{w1}" width="{w2}" height="28" fill="{color}"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="{font}" font-size="11" font-weight="700" letter-spacing="0.8">
    <text x="{w1/2:.1f}" y="18">{left_text}</text>
    <text x="{w1 + w2/2:.1f}" y="18">{right_text}</text>
  </g>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

create_badge_svg("assets/badge-linkedin.svg", "LINKEDIN", "", "#0A66C2")
create_badge_svg("assets/badge-cv.svg", "DOWNLOAD CV (PDF)", "", "#2f81f7")
create_badge_svg("assets/badge-codeforces.svg", "CODEFORCES", "CODIGOL (CANDIDATE MASTER)", "#1F8ACB")
create_badge_svg("assets/badge-icpc.svg", "ICPC", "3X WF LATIN AMERICA CHAMPION (1X BRONZE MEDAL)", "#e11d48")
create_badge_svg("assets/badge-ioi.svg", "IOI", "3X PARTICIPANT (1X BRONZE MEDAL)", "#d97706")
create_badge_svg("assets/badge-databricks.svg", "DATABRICKS CERTIFIED", "DATA ENGINEER ASSOCIATE", "#FF3621")
create_badge_svg("assets/badge-efset.svg", "EF SET ENGLISH", "76/100 C2 PROFICIENT", "#005B94")


# 2. Unified Icon System (alto = 38)
alto = 38

def icon(src: str, name: str) -> str:
    return f"""<img src="{src}" height="{alto}" alt="{name}" title="{name}"/>"""

# Core & Existing Tech Badges (clean icon-only -original.svg Devicon)
pandas = icon("https://go-skill-icons.vercel.app/api/icons?i=pandas", "Pandas")
numpy = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg", "NumPy")
python = icon("https://skillicons.dev/icons?i=py", "Python")
cpp = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg", "C++")
sklearn = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg", "Scikit-learn")
bash = icon("https://skillicons.dev/icons?i=bash", "Bash")
R = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rstudio/rstudio-original.svg", "R")
kotlin = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg", "Kotlin")
matplotlib = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg", "Matplotlib")
jupyter = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg", "Jupyter")
tensorflow = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tensorflow/tensorflow-original.svg", "TensorFlow")
cuda = icon("https://go-skill-icons.vercel.app/api/icons?i=cuda", "CUDA")
latex = icon("https://skillicons.dev/icons?i=latex", "LaTeX")
github_actions = icon("https://skillicons.dev/icons?i=githubactions", "GitHub Actions")
pytorch = icon("https://skillicons.dev/icons?i=pytorch", "PyTorch")
polars = icon("https://go-skill-icons.vercel.app/api/icons?i=polars", "Polars")
sqlite = icon("https://go-skill-icons.vercel.app/api/icons?i=sqlite", "SQLite")
docker = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg", "Docker")

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
typesense = icon("./assets/typesense.svg", "Typesense")
go = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg", "Go (Gnark)")
postgresql = icon("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg", "SQL / PostgreSQL")


# 3. Header & Hero Card
header = """<div align="center">
  <h1>Lautaro Lasorsa</h1>
  <p>
    <b>AI / Machine Learning Engineer</b> · <b>3x ICPC World Finalist (Latam Champion)</b> · <b>B.S./M.S. in Data Science (UBA)</b>
  </p>
  <p style="margin: 8px 0 16px 0;">
    <a href="https://www.linkedin.com/in/lautaro-lasorsa/">
      <img src="./assets/badge-linkedin.svg" height="28" alt="LinkedIn" title="LinkedIn: Lautaro Lasorsa"/>
    </a>
    &nbsp;
    <a href="./CV/LautaroLasorsa_CV.pdf">
      <img src="./assets/badge-cv.svg" height="28" alt="Curriculum Vitae" title="Download Curriculum Vitae (PDF)"/>
    </a>
  </p>
</div>

<table width="100%" style="width: 100%; display: table; border-collapse: separate; border-spacing: 0; margin: 16px 0 18px 0;">
  <tr>
    <td style="background: linear-gradient(135deg, rgba(47, 129, 247, 0.12) 0%, rgba(163, 113, 247, 0.08) 100%); border: 1px solid rgba(47, 129, 247, 0.3); border-left: 5px solid #2f81f7; border-radius: 10px; padding: 18px 22px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);">
      <p style="margin: 0 0 12px 0; font-size: 1.06em; line-height: 1.65;">
        I build reliable, maintainable <b style="color: #58a6ff;">agentic AI systems</b> and <b style="color: #58a6ff;">async Python backends</b> end-to-end: from designing <b>scalable architectures, abstractions, and relational schemas</b> to continuously evaluating LLM behavior through <b>reproducible test suites and error analysis</b>. My background in <i>software engineering, data science, and competitive programming</i> helps me tackle complex technical challenges with good judgment, working directly alongside CTO and product teams.
      </p>
      <p align="center" style="margin: 10px 0 0 0;">
        <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">Agentic AI &amp; LLMs</kbd>
        &nbsp;
        <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">Async Python Backends</kbd>
        &nbsp;
        <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">System &amp; Schema Design</kbd>
        &nbsp;
        <kbd style="background: rgba(47, 129, 247, 0.15); border: 1px solid rgba(88, 166, 255, 0.4); border-radius: 6px; padding: 3px 10px; font-size: 0.85em; color: #79c0ff;">LLM Evaluation Suites</kbd>
      </p>
    </td>
  </tr>
</table>

<div align="center">
  <p style="margin: 8px 0 6px 0;">
    <a href="https://codeforces.com/profile/CodigoL">
      <img src="./assets/badge-codeforces.svg" height="28" alt="Codeforces" title="Codeforces Profile: CodigoL (Candidate Master)"/>
    </a>
    &nbsp;
    <a href="https://icpc.global/ICPCID/DV1XEVUDPG8J">
      <img src="./assets/badge-icpc.svg" height="28" alt="ICPC Profile" title="ICPC Global Profile (3x WF Latin America Champion, 1x Bronze Medal)"/>
    </a>
    &nbsp;
    <a href="https://stats.ioinformatics.org/people/6145">
      <img src="./assets/badge-ioi.svg" height="28" alt="IOI Profile" title="International Olympiad in Informatics (2017, 2018 Bronze Medal, 2019)"/>
    </a>
  </p>
  <p style="margin: 0 0 24px 0;">
    <a href="https://credentials.databricks.com/838212fa-8d2c-4e5d-b146-ba2f1af0e39d#acc.uF1sAh5D">
      <img src="./assets/badge-databricks.svg" height="28" alt="Databricks Credential" title="Databricks Certified Data Engineer Associate (Verified Credential)"/>
    </a>
    &nbsp;
    <a href="https://cert.efset.org/Pymcaz">
      <img src="./assets/badge-efset.svg" height="28" alt="EF SET English Certificate" title="EF SET English Certificate: 76/100 C2 Proficient"/>
    </a>
  </p>
</div>
"""

# 4. 3-Column Work Experience Table
work_experience = [
    (
        "<b>Silver.dev</b><br/><i>Technical Interviewer (Contractor)</i><br/><sub>🗓️ Sep 2026 – Present · Remote</sub>",
        "<ul><li>Conduct technical interviews for software engineers applying to US-based tech companies, specializing in <b>System Design</b> (scalable architectures, distributed systems, and trade-off analysis).</li></ul>",
        [python, docker, redis, postgresql],
    ),
    (
        "<b>AutoScheduler.AI</b><br/><i>Machine Learning / AI Engineer</i><br/><sub>🗓️ Jul 2025 – Oct 2026 · Remote</sub>",
        "<ul><li>Designed and implemented production agentic AI workflows with LangChain and LangGraph, including prompting, structured outputs, and context management for a warehouse orchestration platform.</li><li>Built multi-agent components for conversational data retrieval, analysis, and natural language interaction with business data, plus an app-creation agentic platform.</li><li>Developed async Python/FastAPI services and integration layers to connect the assistant with SQL Server, Redis, and Cosmos DB, deployed through Docker and Azure DevOps CI/CD with pytest, Ruff, and static type checking.</li><li>Built an agent behavior evaluation suite with reproducible test cases and error analysis, optimizing accuracy, latency, and cost through retrieval context, model selection, and prompt structure.</li><li>Implemented data visualization and reporting features with Plotly and matplotlib, and designed the relational database schema.</li></ul>",
        [python, fastapi, langchain, langgraph, sqlserver, redis, cosmosdb, docker, azuredevops, pytest, ruff, plotly, matplotlib],
    ),
    (
        "<b>Mutt Data</b><br/><i>Ssr Data Developer</i><br/><sub>🗓️ Feb 2025 – Jun 2025 · Remote</sub>",
        "<ul><li>Built ETL pipelines in Google BigQuery to process user engagement data at scale and deliver KPI dashboards for CTR, VTR, completion rate, and time viewed.</li><li>Enriched event data with Typesense and TMDB metadata, using BigQuery table design, CTEs, and window functions for analytics and search.</li><li><a href=\"https://credentials.databricks.com/838212fa-8d2c-4e5d-b146-ba2f1af0e39d#acc.uF1sAh5D\">Earned the Databricks Certified Data Engineer Associate certification.</a></li></ul>",
        [python, bigquery, gcp, databricks, postgresql, docker, typesense],
    ),
    (
        "<b>Composable Finance</b><br/><i>Cryptography Consultant</i><br/><sub>🗓️ Apr 2023 – Jul 2024 · Remote</sub>",
        "<ul><li>Worked on financial transaction infrastructure, implementing ED-25519 signature verification with Zero Knowledge (ZK) over Gnark.</li><li>Developed a solution to optimize transactions using graph algorithms and Python.</li></ul>",
        [go, python],
    ),
    (
        "<b>UBA & UNLaM</b><br/><i>Head Class Assistant (JTP) & ICPC Coach</i><br/><sub>🗓️ Mar 2020 – Present · Hybrid</sub>",
        "<ul><li><b>UBA (2025–Present):</b> Led Algorithms & Data Structures practical sessions and designed midterm exams for 200+ students.</li><li><b>UNLaM (2020–Present):</b> Taught competitive programming on Saturdays using C++, Python, and Kotlin; coached 19 university teams competing in the Argentina Programming Tournament (TAP, 2022–2026).</li></ul>",
        [cpp, python, kotlin],
    ),
]

text = header

text += "<details open>\n"
text += '<summary><h2 style="display: inline-block; margin: 0;"> 💼 Work Experience </h2></summary>\n'
text += '<table width="100%" style="width: 100%; display: table;">\n'
text += "<thead>\n"
text += '<tr> <th width="24%" align="left"> Role & Place </th> <th width="52%" align="left"> Description </th> <th width="24%" align="center"> Technologies </th> </tr>\n'
text += "</thead>\n"
text += "<tbody>\n"
for place, desc, tags in work_experience:
    text += f'<tr> <td width="24%"> {place} </td> <td width="52%"> {desc} </td> <td width="24%" align="center"> {" ".join(tags)} </td> </tr>\n'
text += "</tbody>\n"
text += "</table>\n"
text += "</details>\n\n"


# 5. Project Sections with Subtitles
sections = {}

sections["🏆 Competitive Programming"] = [
    (
        "Usefull competitive programming commands",
        "https://github.com/LautaroLasorsa/competitive-programming-suite",
        "Reusable CLI commands, setup scripts, and template toolkit for competitive programming contests",
        [cpp, python, bash],
    ),
    (
        "Problems I proposed to national and international contests",
        "https://github.com/LautaroLasorsa/Mis-problemas--My-Problems",
        "Original algorithmic problem statements, solutions, and LaTeX editorials for OIA and regional competitions",
        [cpp, python, latex],
    ),
    (
        "Kotlin Notebook for ICPC teams",
        "https://github.com/LautaroLasorsa/notebook-unlam-kotlin",
        "Algorithms and data structures library in Kotlin with GitHub Actions automation for ICPC teams",
        [kotlin, bash, github_actions],
    ),
    (
        "Python Notebook for ICPC teams",
        "https://github.com/LautaroLasorsa/notebook-unlam-python",
        "Reusable algorithms, templates, and reference implementations in Python for ICPC training",
        [python, bash],
    ),
    (
        "OIA UNLaM Course material",
        "https://github.com/LautaroLasorsa/OIA-UNLaM",
        "Curriculum and training materials for high school students competing in the Argentine Informatics Olympiad",
        [cpp],
    ),
    (
        "Solutions to some CSES problems",
        "https://github.com/LautaroLasorsa/CSES/tree/main",
        "Clean, optimized solutions to standard problems from the CSES Problem Set in C++",
        [cpp],
    ),
]

sections["🎓 University Assignments"] = [
    (
        "Licenciature Tesis (10/10) <i>Propuesta de mejora del bienestar económico</i>",
        "https://github.com/LautaroLasorsa/Tesis-LCD-Lasorsa",
        "Bachelor's Thesis (10/10) · Novel economic welfare indicator evaluated via massive parallel Monte Carlo simulations on CUDA",
        [python, numpy, pandas, matplotlib, jupyter, cpp, cuda, latex],
    ),
    (
        "Instrumental Variable Quantile Regression module in R",
        "https://github.com/LautaroLasorsa/IVQR",
        "Econometrics package implementing Instrumental Variable Quantile Regression (Chernozhukov & Hansen method)",
        [R],
    ),
    (
        "Verify Small World Hypothesis in social networks",
        "https://github.com/LautaroLasorsa/TP-FINAL-SMALL-WORLD",
        "Complex network analysis validating the Small World property across 13 empirical social graph datasets",
        [python, numpy, pandas, matplotlib, jupyter],
    ),
    (
        "Implementation of algorithm for the paper <i>Revisiting Link Prediction: A data perspective</i>",
        "https://github.com/LautaroLasorsa/Implementation-of-Revisiting-Link-Prediction-A-data-perspective",
        "Graph Neural Network implementation of SEAL link prediction using PyTorch Geometric on citation networks",
        [python, numpy, pandas, matplotlib, jupyter, sklearn, pytorch],
    ),
]

sections["📄 Research (Published)"] = [
    (
        "<i>Modelos de Lenguaje Pequeños para la Interpretación de Comandos de Domótica en Español: Evaluación Automática de Doce Modelos Sub-2B</i> @ CACIC 2026",
        "https://www.frcu.utn.edu.ar/images/CACIC/actas.pdf#page=169",
        "Evaluation of 12 Sub-2B Small Language Models (SLMs) for Spanish smart-home voice command interpretation",
        [python, pytorch],
    ),
    (
        "<i>Detección de fallas en sensores IoT mediante Machine Learning</i> @ CONAIISI 2024",
        "https://github.com/LautaroLasorsa/CONAIISI-2024/tree/master",
        "Fault detection and sensor anomaly classification in IoT networks using machine learning algorithms",
        [python, sklearn, matplotlib, numpy, pandas, jupyter],
    ),
    (
        "<i>Estudio de tolerancia a errores en sensores para detección de ocupación</i> @ CONAIISI 2024",
        "https://github.com/carlucho1/CONAIISI-2024-2/tree/main",
        "Analysis of error tolerance in occupancy-detection sensor networks using supervised learning techniques",
        [python, sklearn, matplotlib, numpy, pandas, jupyter],
    ),
    (
        "<i>Estudio comparativo de modelos de ML y análisis de robustez frente a fallas en sensores</i> @ CONAIISI 2023",
        "https://github.com/LautaroLasorsa/CONAIISI-2023/tree/main",
        "Comparative study of ML models (Random Forest, NNs) and sensor fault-tolerance for edge computing fire detection",
        [python, tensorflow, matplotlib, numpy, pandas, jupyter],
    ),
]

sections["🛠️ Other Projects"] = [
    (
        "<i>Features Store Practice</i>",
        "https://github.com/LautaroLasorsa/features_store_practice",
        "Feature store pipeline prototype built with Polars, SQLite, and Docker for scalable ML feature serving",
        [python, polars, sqlite, docker],
    )
]

for title, items in sections.items():
    text += "<details open>\n"
    text += f'<summary><h2 style="display: inline-block; margin: 0;"> {title} </h2></summary>\n'
    text += '<table width="100%" style="width: 100%; display: table;">\n'
    for name, link, subtitle, tags in items:
        text += f'<tr> <td width="70%"> <a href="{link}"><b>{name}</b></a><br/><sub>{subtitle}</sub> </td> <td width="30%" align="center"> {" ".join(tags)} </td> </tr>\n'
    text += "</table>\n"
    text += "</details>\n\n"

# 6. Save README.md in UTF-8
with open("README.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Generated assets/typesense.svg, assets/badge-*.svg, and README.md successfully.")

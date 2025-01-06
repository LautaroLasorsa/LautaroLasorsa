text = """<div >
    <h1 style="display: flex; justify-content: space-between;"> Lautaro Lasorsa 
    <a href="https://www.linkedin.com/in/lautaro-lasorsa/" > <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" height=50 > </a>
    <a href="./CV/LautaroLasorsa_CV.pdf"> CV </a>
    </h1>
</div>"""

alto    = 50
pandas  = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" height={alto}/>"""
numpy   = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-plain-wordmark.svg" height={alto}/>""" 
python  = f"""<img src="https://skillicons.dev/icons?i=py" height={alto}/>"""
cpp     = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg" height={alto}/>""" 
sklearn = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" height={alto}/>"""
bash    = f"""<img src="https://skillicons.dev/icons?i=bash" height={alto}/>"""
R       = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rstudio/rstudio-original.svg" height={alto}/>"""
kotlin  = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-plain-wordmark.svg" height={alto}/>"""
matplotlib = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" height={alto}/>"""
jupyter = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" height={alto}/>"""
tensorflow = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tensorflow/tensorflow-original-wordmark.svg" height={alto}/>"""
IoT     = ""
cuda    = ""
latex   = f"""<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/latex/latex-original.svg" height={alto}/>"""
github_actions = f"""<img src="https://skillicons.dev/icons?i=githubactions" height={alto}/>"""

sections = {}

sections["Competitive Programming"] = [
    ("Usefull competitive programming commands",
     "https://github.com/LautaroLasorsa/competitive-programming-suite",
     [cpp,python,bash]),
     ("Problems I proposed to national and international contests",
       "https://github.com/LautaroLasorsa/Mis-problemas--My-Problems",
       [cpp, python, latex]     
     ),
     ("Kotlin Notebook for ICPC teams", 
      "https://github.com/LautaroLasorsa/notebook-unlam-kotlin",
      [kotlin,bash,github_actions]),
      ("Python Notebook for ICPC teams",
       "https://github.com/LautaroLasorsa/notebook-unlam-python",
       [python,bash]),
       ("OIA UNLaM Course material",
        "https://github.com/LautaroLasorsa/OIA-UNLaM",
        [cpp]),
        ("Solutions to some CSES problems",
         "https://github.com/LautaroLasorsa/CSES/tree/main",
         [cpp])
]

sections["University Assigments"] = [
    ("Licenciature Tesis (10/10) <i>Propuesta de mejora del bienestar económico</i>",
     "https://github.com/LautaroLasorsa/Tesis-LCD-Lasorsa",
     [python,numpy,pandas,matplotlib,jupyter, cpp,cuda, latex]),
    ("Instrumental Variable Quantile Regression module in R",
     "https://github.com/LautaroLasorsa/IVQR",
     [R])
]

sections["Research (Published)"] = [
    ("<i>Estudio comparativo de diferentes modelos de aprendizaje automático y análisis de la robustez de dichos modelos frente a fallas provocadas en los sensores en el caso de detección de incendios para ser aplicados a dispositivos de computación de borde</i> @ CONAIISI 2023",
    "https://github.com/LautaroLasorsa/CONAIISI-2023/tree/main",
    [python, tensorflow, matplotlib, numpy, pandas, jupyter, IoT]
    ),

    ("<i>Detección de fallas en sensores IoT mediante Machine Learning</i> @ CONAIISI 2024",
     "https://github.com/LautaroLasorsa/CONAIISI-2024/tree/master",
      [python, sklearn, matplotlib, numpy, pandas, jupyter, IoT]
    ),

    ("<i>Estudio de tolerancia a errores en sensores empleados para detección de ocupación de habitantes de un recinto empleando técnicas de aprendizaje automático</i> @ CONAIISI 2024",
    "https://github.com/carlucho1/CONAIISI-2024-2/tree/main",
      [python, sklearn, matplotlib, numpy, pandas, jupyter, IoT]
    )
]

for (title, items) in sections.items():
    text += f"<h1> {title} </h1>\n"
    text += "<table>\n"
    for (name, link, tags) in items:
        text += f"<tr> <td> <a href={link}> {name} </a> </td> <td> {' '.join(tags)} </td> </tr> \n" 
    text += "</table>\n"""

print(text)
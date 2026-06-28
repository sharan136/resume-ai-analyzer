def analyze_job_match(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()


    # Clean text
    resume_text = resume_text.replace("-", " ")
    job_description = job_description.replace("-", " ")


    keywords = [

        "python",
        "c++",
        "java",
        "html",
        "css",
        "javascript",
        "flask",
        "react",
        "node",
        "sql",
        "mysql",
        "mongodb",
        "git",
        "github",
        "machine learning",
        "artificial intelligence",
        "data analysis",
        "pandas",
        "numpy",
        "data structures",
        "algorithms",
        "oops",
        "object oriented programming",
        "linux"

    ]


    found = []
    missing = []


    for keyword in keywords:

        if keyword in job_description:

            if keyword in resume_text:
                found.append(keyword)

            else:
                missing.append(keyword)



    total_keywords = len(found) + len(missing)


    if total_keywords > 0:

        score = int((len(found) / total_keywords) * 100)

    else:

        score = 0


    return found, missing, score
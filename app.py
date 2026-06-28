from flask import Flask, render_template, request
from flask import send_file
import os
import json

from extractor import extract_text
from analyzer import analyze_resume
from ats_analyzer import calculate_ats_score
from ats_feedback import generate_ats_feedback
from job_matcher import analyze_job_match
from experience_analyzer import analyze_experience
from quality_score import calculate_quality_score
from strength_analyzer import generate_strengths
from suggestions import get_suggestions
from job_database import JOB_DATABASE
from pdf_generator import create_pdf



app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)




@app.route("/")
def home():

    return render_template(
        "index.html",
        domains=list(JOB_DATABASE.keys()),
        jobs=JOB_DATABASE
    )





@app.route("/upload", methods=["POST"])
def upload():


    # Resume file

    file = request.files["resume"]


    # Selected role

    role = request.form["role"]


    # Job description

    job_description = request.form["job_description"]




    # Save resume

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)




    # Extract text from PDF

    text = extract_text(file_path)


    # Resume analysis

    found, missing, score = analyze_resume(
        text,
        role
    )




    # Suggestions

    suggestions = get_suggestions(
        missing
    )




    # ATS score

    ats_score = calculate_ats_score(
        text
    )




    # ATS feedback

    ats_feedback = generate_ats_feedback(
        text
    )




    # Experience analysis

    experience_analysis = analyze_experience(
        text
    )




    # Job description matching

    job_found, job_missing, job_score = analyze_job_match(
        text,
        job_description
    )




    # Overall quality score

    quality_score = calculate_quality_score(
        score,
        ats_score,
        job_score,
        experience_analysis
    )




    # Strengths and weaknesses

    strengths, weaknesses = generate_strengths(
        found,
        missing,
        ats_feedback,
        experience_analysis,
        job_score
    )

    pdf_file = "uploads/resumeai_report.pdf"


    create_pdf(
        pdf_file,
        quality_score,
        score,
        ats_score,
        job_score,
        strengths,
        weaknesses,
        suggestions
    )



    return render_template(
        "result.html",

        # Scores

        score=score,

        ats_score=ats_score,

        job_score=job_score,

        quality_score=quality_score,



        # Skills

        found=found,

        missing=missing,



        # Suggestions

        suggestions=suggestions,



        # ATS

        ats_feedback=ats_feedback,



        # Experience

        experience_analysis=experience_analysis,



        # Job matching

        job_found=job_found,

        job_missing=job_missing,



        # Strengths

        strengths=strengths,

        weaknesses=weaknesses,

        pdf_file=pdf_file
    )

@app.route("/download-report")
def download_report():

    return send_file(
        "uploads/resumeai_report.pdf",
        as_attachment=True
    )





if __name__ == "__main__":

    app.run(debug=True)
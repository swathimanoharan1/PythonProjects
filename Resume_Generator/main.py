from resume import Resume
from pdf_converter import convert_markdown_to_pdf
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)

def validate_mobile(mobile):
    pattern = r'^\+?\d{7,15}$'
    return re.match(pattern, mobile)

def validate_linkedin_url(linkedin_url):
    pattern = r'^https:\/\/(www\.)?linkedin\.com\/.*$'
    return re.match(pattern, linkedin_url)

def get_user_input():

# Name section
    name1 = input("Enter your name: ").strip()
    while not name1:
        print("Name cannot be empty.")
        name1 = input("Enter your name: ").strip()

    email = input("Enter your email: ").strip()
    while not validate_email(email):
        print("Invalid email format.")
        email = input("Enter a valid email: ").strip()

    mobile = input("Enter your mobile number: ").strip()
    while not validate_mobile(mobile):
        print("Invalid mobile number.")
        mobile = input("Enter a valid mobile number: ").strip()

    linkedin_url = input("Enter your LinkedIn URL: ").strip()
    while not validate_linkedin_url(linkedin_url):
        print("Invalid LinkedIn url.")
        linkedin_url = input("Enter a valid LinkedIn URL: ").strip()

# Education Section
    print("\nEducation:")
    education = []
    while True:
        if input("Do you want to add education details? (y/n): ").lower() != 'y':
            break
        level = input("Enter education level (e.g., Graduation(UG/PG), High School): ")
        institution = input(f"Enter the name of the {level} institution: ")
        field = input(f"Enter the field of study at {institution}: ")
        duration = input(f"Enter passing year of {level} at {institution}: ")
        score = input(f"Enter your score (e.g., GPA/Percentage) of {level} at {institution}: ")
        education.append({"level": level, "institution": institution, "field": field, "duration": duration, "score": score})

# Skills section
    skills = input("\nEnter your skills (comma-separated): ")

# Experience section
    print("\nExperience:")
    experience = []
    while True:
        job_title = input("Enter your job title (or type 'done' to finish): ")
        if job_title.lower() == 'done':
            break
        company_name = input("Enter the company name: ")
        year = input("Enter the year-year: ")
        description = input(f"Enter the description for '{job_title}': ")
        experience.append({"job_title": job_title, "company_name": company_name, "year": year, "description": description})

# Project section
    print("\nProjects:")
    projects = []
    while True:
        name = input("Enter the project title (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        description = input(f"Enter the description for '{name}': ")
        skills_used = input(f"Enter the skills used for '{name}': ")
        projects.append({"name": name, "description": description, "skills": skills_used})

# Achievements section
    print("\nAchievements:")
    achievements = []
    while True:
        achievement = input("Enter an achievement detail (or type 'done' to finish): ")
        if achievement.lower() == 'done':
            break
        achievements.append(achievement)

# Other activities section
    print("\nOther Activities like hobbies:")
    activities = input("Enter your other activities: ")

    return Resume(name1, email, mobile, linkedin_url, education, skills, experience, projects, achievements, activities)

# main function
if __name__ == "__main__":
    user_resume = get_user_input()
    markdown_text = user_resume.generate_markdown()
    convert_markdown_to_pdf(markdown_text)
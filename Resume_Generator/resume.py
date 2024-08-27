class Resume:
    def __init__(self, name1, email, mobile, linkedin_url, education, skills, experience, projects, achievements, activities):
        self.name = name1
        self.email = email
        self.mobile = mobile
        self.linkedin_url = linkedin_url
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.activities = activities

    def generate_markdown(self):
        markdown_text = f"<h1 style=\"text-align:center;\">{self.name}</h1>\n"
        markdown_text += f"<p style=\"text-align:center;\">Email: {self.email} | Mobile: {self.mobile} | LinkedIn: {self.linkedin_url}</p>\n\n"
        markdown_text += "### Education\n\n---\n\n"
        
        for edu in self.education:
            markdown_text += f"- {edu['level']}: {edu['institution']} | {edu['field']} | Score: {edu['score']} | {edu['duration']}.\n\n"

        markdown_text += "### Skills\n\n---\n\n"
        markdown_text += f"{self.skills} \n\n"

        markdown_text += "### Experience\n\n---\n\n"
        for exp in self.experience:
            markdown_text += f"- **{exp['job_title']} - {exp['company_name']} - {exp['year']}**: {exp['description']}\n"

        markdown_text += "\n### Projects\n\n---\n\n"
        for proj in self.projects:
            markdown_text += f"- **{proj['name']}**: {proj['description']}\n \n**Skills Used**: {proj['skills']}\n"

        markdown_text += "\n### Achievements\n\n---\n\n"
        for ach in self.achievements:
            markdown_text += f"- {ach}\n"

        markdown_text += "\n### Other Activities\n\n---\n\n"
        markdown_text += self.activities + '\n'

        return markdown_text
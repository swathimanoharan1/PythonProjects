import requests

def convert_markdown_to_pdf(markdown_content, resume_file="Resume.pdf", engine="weasyprint"):
    cssfile = """
    body {
        padding: 0px;
        margin: 0px;
    }
    h1 {
        color: Black;
        margin: 0px;
        padding: 0px;
    }
    h3 {
        color: Black;
        padding-bottom: 0px;
        margin-bottom: 0px;
    }
    li {
        margin-top: 5px;
    }
    """
    
    url = "https://md-to-pdf.fly.dev"
    data = {
        'markdown': markdown_content,
        'css': cssfile,
        'engine': engine
    }
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        with open(resume_file, 'wb') as f:
            f.write(response.content)
        print(f"PDF saved to {resume_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
from flask import Flask, render_template
import os

app = Flask(__name__)

# Intentional bug: unused variable
unused_variable = 42

@app.route('/')
def home():
    tools = [
        {"name": "Jenkins", "desc": "Automation server", "image": "jenkins.png"},
        {"name": "Docker", "desc": "Container platform", "image": "docker.png"},
        {"name": "Kubernetes", "desc": "Container orchestration", "image": "kubernetes.png"},
        {"name": "Ansible", "desc": "Configuration management", "image": "ansible.png"},
        {"name": "Terraform", "desc": "Infrastructure as Code", "image": "terraform.png"},
        {"name": "SonarQube", "desc": "Code Quality Tool", "image": "sonarqube.png"},
        {"name": "GitHub Actions", "desc": "CI/CD on GitHub", "image": "github-actions.png"},
    ]
    
    # Intentional bug: hardcoded path
    log_file = open("/tmp/devopslog.txt", "w")
    log_file.write("Tools listed successfully.\n")
    log_file.close()

    return render_template("index.html", tools=tools)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


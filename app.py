#from flask import Flask, render_template
#import os
#
#app = Flask(__name__)
#
## Intentional bug: unused variable
#unused_variable = 42
#
#@app.route('/')
#def home():
#    tools = [
#        {"name": "Jenkins", "desc": "Automation server", "image": "jenkins.png"},
#        {"name": "Docker", "desc": "Container platform", "image": "docker.png"},
#        {"name": "Kubernetes", "desc": "Container orchestration", "image": "kubernetes.png"},
#        {"name": "Ansible", "desc": "Configuration management", "image": "ansible.png"},
#        {"name": "Terraform", "desc": "Infrastructure as Code", "image": "terraform.png"},
#        {"name": "SonarQube", "desc": "Code Quality Tool", "image": "sonarqube.png"},
#        {"name": "GitHub Actions", "desc": "CI/CD on GitHub", "image": "github-actions.png"},
#    ]
#    
#    # Intentional bug: hardcoded path
#    log_file = open("/tmp/devopslog.txt", "w")
#    log_file.write("Tools listed successfully.\n")
#    log_file.close()
#
#    return render_template("index.html", tools=tools)
#
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)
#

from flask import Flask, render_template
import os
import logging

app = Flask(__name__)

# Configure logging properly
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    """Home page displaying DevOps tools showcase."""
    tools = [
        {"name": "Jenkins", "desc": "Automation server", "image": "jenkins.png"},
        {"name": "Docker", "desc": "Container platform", "image": "docker.png"},
        {"name": "Kubernetes", "desc": "Container orchestration", "image": "kubernetes.png"},
        {"name": "Ansible", "desc": "Configuration management", "image": "ansible.png"},
        {"name": "Terraform", "desc": "Infrastructure as Code", "image": "terraform.png"},
        {"name": "SonarQube", "desc": "Code Quality Tool", "image": "sonarqube.png"},
        {"name": "GitHub Actions", "desc": "CI/CD on GitHub", "image": "github-actions.png"},
    ]
    
    # Proper file handling with context manager
    log_dir = os.getenv('LOG_DIR', '/tmp')
    log_file_path = os.path.join(log_dir, 'devopslog.txt')
    
    try:
        with open(log_file_path, "w", encoding='utf-8') as log_file:
            log_file.write("Tools listed successfully.\n")
        logger.info("Tools listed successfully")
    except IOError as e:
        logger.error(f"Failed to write log file: {e}")
    
    return render_template("index.html", tools=tools)

if __name__ == '__main__':
    # Use environment variable for debug mode
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']
    app.run(host='0.0.0.0', debug=debug_mode)

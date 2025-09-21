Agent-Avana: The Generative AI Legal Document Platform
Agent-Avana is a cutting-edge platform designed to demystify complex legal documents for small business owners and individuals. Leveraging Google's Generative AI, this solution simplifies legal jargon, ensures compliance with global standards, and provides a multi-agent architecture for real-time verification and insights.

Project Structure
This repository is organized to support a multi-agent, microservices architecture, with each agent handling a specific task in the document verification pipeline.

frontend/: The future home of the main web application (e.g., using React/Next.js).

agents/: Contains the microservices (agents) that perform the core logic, such as ingestion, classification, and verification.

infra/: Infrastructure as code files for deploying the application to Google Cloud Platform.

docs/: Detailed architectural diagrams, data schemas, and design documents.

scripts/: Utility scripts for development, such as seeding databases.

tests/: Unit and end-to-end tests for the agents and frontend.

For immediate use, the core files (index.html and main.py) are placed at the root of this repository to create a simple, runnable MVP.

Getting Started
Clone the repository:

git clone [https://github.com/](https://github.com/)<your-username>/AGENT-AVANA.git
cd AGENT-AVANA

Set up the Python backend:

Ensure you have Python 3.8+ installed.

Install the required dependencies:

pip install -r requirements.txt

Run the server:

Start the FastAPI server.

uvicorn main:app --reload

The --reload flag will automatically restart the server when you make changes to the code.

View the application:

Open your web browser and navigate to http://127.0.0.1:8000.

This will run the frontend and backend together, allowing you to test the document upload and chatbot functionalities.

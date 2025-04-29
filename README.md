# 🧠 AI-Powered Resume schedular | FastAPI + ReactJS + NLP + Docker + Jenkins

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-ReactJS-blue)](https://reactjs.org/)
[![Docker](https://img.shields.io/badge/DevOps-Docker-informational)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/CI/CD-Jenkins-red)](https://www.jenkins.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack **AI-powered Resume Checker** that allows users to upload resumes, extracts keywords using **spaCy (NLP)**, matches them with job profiles, and provides real-time feedback—all managed under a **Dockerized CI/CD pipeline** using **Jenkins**.

---

## 🚀 Features

- 📄 **Resume Upload**: Simple upload via frontend for quick analysis.
- 🧠 **NLP-based Keyword Extraction**: Uses spaCy to extract relevant keywords.
- 🎯 **Job Matching**: Matches resume content with job descriptions.
- 👥 **Role-Based Login**: Separate views for Users and HR.
- 📊 **Resume Status Tracker**: Monitor application status: Submitted, Viewed, Selected, Rejected.
- 🐳 **Dockerized Setup**: Run the entire app in isolated containers via Docker Compose.
- 🔄 **CI/CD Integration**: Automate builds, testing, and deployment with Jenkins.

---

## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| **Frontend** | ReactJS           |
| **Backend**  | FastAPI (Python)  |
| **NLP**      | spaCy             |
| **Database** | PostgreSQL (SQLite for local) |
| **Containerization** | Docker, Docker Compose |
| **CI/CD**    | Jenkins           |

---

## 📁 Project Structure


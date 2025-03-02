import os
import streamlit as st
import csv
from PIL import Image

# Set Paths
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "CareerUpskillers")
pdf_path = os.path.join(downloads_folder, "pdf.pdf")
leads_csv = os.path.join(downloads_folder, "leads.csv")

# Ensure CareerUpskillers directory exists
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

# Ensure CSV file exists for lead storage
if not os.path.exists(leads_csv):
    with open(leads_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Phone", "Experience", "Domain", "Location", "Current Salary", 
                         "Expected Salary", "Upwork/Fiverr (Yes/No)", "AI Business Interest (Yes/No)"])

# Check Brochure Function
def check_brochure():
    if os.path.exists(pdf_path):
        st.success("Thank you! Your brochure will now download.")
        os.startfile(pdf_path)  # Open the PDF
    else:
        st.error("Brochure not found! Please add 'pdf.pdf' in CareerUpskillers folder.")

# Lead Collection Function
def submit_lead():
    name = st.session_state.name
    email = st.session_state.email
    phone = st.session_state.phone
    experience = st.session_state.experience
    domain = st.session_state.domain
    location = st.session_state.location
    current_salary = st.session_state.current_salary
    expected_salary = st.session_state.expected_salary
    upwork_fiverr = st.session_state.upwork_fiverr
    ai_business_interest = st.session_state.ai_business_interest

    if not email or len(phone) < 10:
        st.error("Valid Email & 10-digit Phone are required to download!")
        return

    with open(leads_csv, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, phone, experience, domain, location, current_salary, expected_salary,
                         upwork_fiverr, ai_business_interest])

    st.success("Thank you! Click 'Download Brochure' now.")
    st.session_state.download_enabled = True  # Enable download after submission

# Streamlit App
st.title("CareerUpskillers - We Help you grow")

# Load Logo
logo_path = "careerupskillers logo.jpg"
if os.path.exists(logo_path):
    logo = Image.open(logo_path).resize((150, 150), Image.LANCZOS)
    st.image(logo)

# Form Fields
st.text_input("Name", key="name")
st.text_input("Email", key="email")
st.text_input("Phone", key="phone")
st.text_input("Experience (Years)", key="experience")
st.text_input("Domain", key="domain")
st.text_input("Location", key="location")
st.text_input("Current Salary", key="current_salary")
st.text_input("Expected Salary", key="expected_salary")

# Upwork/Fiverr Question
upwork_fiverr = st.radio("Do you have Upwork or Fiverr?", ("Yes", "No"), key="upwork_fiverr")

# AI Business Interest Question
ai_business_interest = st.radio("Interested in building your own AI business agents?", ("Yes", "No"), key="ai_business_interest")

# Submit Button (Collects Leads)
if st.button("Submit & Unlock Brochure"):
    submit_lead()

# Download Button (Initially Disabled)
if st.session_state.get('download_enabled', False):
    if st.button("Download Brochure"):
        check_brochure()
else:
    st.button("Download Brochure", disabled=True)

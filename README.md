<div align="center">

# 🩸 Blood Donor Platform with Real-Time Donor Verification

</div>

<div align="center">

**Blood Donor Platform based on student database**

</div>

---

<div align="center">

## 🎯 Purpose

</div>

This platform solves a critical coordination problem in emergency healthcare:

- Hospitals submit urgent blood requests via a secure web form.
- The system matches requests with eligible donors from a MySQL database.
- Twilio voice calls verify which donors are immediately available.
- Hospitals receive a refined list of confirmed donors—ready to act.

---

<div align="center">

## 🏗️ Architecture Overview

</div>

| Layer                   | Description                                                                  |
|-------------------------|------------------------------------------------------------------------------|
| **Presentation Layer**  | HTML/CSS web form for hospital staff to submit blood requests                |
| **Application Layer**   | Flask backend that handles routing, donor matching, and Twilio integration   |
| **Database Layer**      | MySQL database storing donor, hospital, and request records                  |
| **Communication Layer** | Twilio voice API for real-time donor verification via IVR                    |

---

<div align="center">

## 🧱 Folder Structure

</div>

```
blood-donor-platform/
├── app.py
├── config.py
├── import_data.py
├── requirements.txt
├── .env.example
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   └── css/
│       └── style.css
├── Procfile
├── runtime.txt
├── README.md
└── .gitignore
```

---

<div align="center">

## ⚙️ Technologies Used

</div>

- **Backend**: Flask, SQLAlchemy, python-dotenv  
- **Database**: MySQL  
- **Frontend**: HTML, CSS, Bootstrap  
- **Communication**: Twilio Programmable Voice, TwiML  
- **Data Handling**: Pandas (for Excel import)  
- **Deployment**: Heroku / AWS  

---

<div align="center">

## 🔐 Environment Variables

</div>

Create a `.env` file based on `.env.example` with the following:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
```

---

<div align="center">

## 🚀 Deployment Instructions

</div>

**Step 1: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Run the Flask app locally**
```bash
python app.py
```

**Step 3: Expose local server for Twilio (optional)**
```bash
ngrok http 5000
```

**Step 4: Deploy to Heroku**
- Add `Procfile` and `runtime.txt`
- Set environment variables in Heroku dashboard
- Push code to Heroku Git remote

---

<div align="center">

## 📞 Twilio Call Flow

</div>

1. Flask triggers a Twilio call to the donor.
2. The donor hears: “Hospital X requires blood type A+. Press 1 if available.”
3. The donor presses a key.
4. Twilio sends the response to a Flask webhook.
5. The database updates the donor's availability in real-time.

---

<div align="center">

## 📊 Database Schema

</div>

- **Donors**: `id`, `name`, `phone_number`, `blood_group`, `last_donation_date`, `availability_status`
- **Hospitals**: `id`, `name`, `email`, `location`
- **Requests**: `id`, `hospital_id`, `blood_group_needed`, `request_time`, `status`

---

<div align="center">

## ✅ GitHub Engineering Workflow

</div>

- Use **feature branches** for each layer:
    - `feature/ui-form`
    - `feature/backend-core`
    - `feature/database-setup`
    - `feature/twilio-integration`
    - `feature/deployment-prep`
- Follow **conventional commits**:
    - `feat(ui): add hospital form`
    - `feat(db): define models`
    - `chore(deploy): add Procfile`
- Use **pull requests** to merge into `main`.

---

<div align="center">

## 📌 Status

</div>

- ✅ UI Form  
- ✅ Flask Routing  
- ✅ Donor Matching  
- ✅ Twilio Integration  
- 🔄 Deployment in Progress

---

<div align="center">

## 🤝 Contributors

</div>

Built and maintained by **Bharath**  
Inspired by real-world emergency coordination challenges.

# PawsitiveAdoptionHub

PawsitiveAdoptionHub is a comprehensive pet adoption platform designed to simplify the pet adoption process and connect pets in need with caring individuals or families.

## Features

- **Advanced Search Filters:** Refine pet searches based on species, age, size, and more.
- **Detailed Adoption Profiles:** View comprehensive pet profiles with photos and essential details.
- **Collaboration with Shelters:** Partnerships with local shelters to showcase available pets.
- **User Reviews:** Share adoption experiences and provide feedback for informed decisions.
- **Digital Pet Health Records:** Manage and access pet health records for adopted pets.
- **Step-by-Step Adoption Guidance:** Guidance and checklists for the adoption process.
- **Lost and Found Section:** Report and search for lost or found pets.
- **Pet Care Resources:** Access articles, guides, and FAQs on pet care.
- **Vet Directory and Services Locator:** Find vet services and pet-friendly locations.
- **Vibrant Pet Community Forum:** Engage with a community of pet enthusiasts for advice and experiences.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Additional Tools:** Git, GitHub

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shashaaankkkkk/PawsitiveAdoptionHub.git
    ```

2. Setup Python environment and install dependencies:

    ```bash
    cd PawsitiveAdoptionHub
    python -m venv venv
    source venv/bin/activate (For Windows: venv\Scripts\activate)
    pip install -r requirements.txt
    ```

3. Configure the database in settings.py:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. Apply migrations and start the server:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

5. Access the application at `http://127.0.0.1:8000/` in your browser.

## Contribution

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a pull request

## License

This project is licensed under the [MIT License](LICENSE).



# Screenshots
## Home Screen
![homescreen](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/5790b3c60fc7f7430f740b0e9a52eee611b77a16/static/Screenshot%202023-11-19%20at%206.22.42%E2%80%AFAM.png)

## Pet Search
![Pet_search](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/6693a6523d0c47c1f391f8127d48f549b2073a4c/static/Screenshot%202023-11-19%20at%206.22.46%E2%80%AFAM.png)
## Pet Profile
![Pet_profile](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/6693a6523d0c47c1f391f8127d48f549b2073a4c/static/Screenshot%202023-11-19%20at%206.22.52%E2%80%AFAM.png)

## Adoption appointment
![Appointment_pet](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/2855fccc5ce9be06fdc0e1d8dc3f2c784aaeddba/static/Screenshot%202023-11-19%20at%206.22.56%E2%80%AFAM.png)
## Community Forum 
![Forum](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/2855fccc5ce9be06fdc0e1d8dc3f2c784aaeddba/static/Screenshot%202023-11-19%20at%206.32.18%E2%80%AFAM.png)
## Vet Listing
![Vet_listing](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/2855fccc5ce9be06fdc0e1d8dc3f2c784aaeddba/static/Screenshot%202023-11-19%20at%206.33.42%E2%80%AFAM.png)
## Vet Profile
![Vet_profile](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/2855fccc5ce9be06fdc0e1d8dc3f2c784aaeddba/static/Screenshot%202023-11-19%20at%206.33.50%E2%80%AFAM.png)
## Vet Appointment 
![Appointment_vet](https://github.com/shashaaankkkkk/PawsitiveAdoptionHub/blob/2855fccc5ce9be06fdc0e1d8dc3f2c784aaeddba/static/Screenshot%202023-11-19%20at%206.33.59%E2%80%AFAM.png)

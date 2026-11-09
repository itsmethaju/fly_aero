#!/usr/bin/env python3
"""Apply Fly Aero Travel & Tourism content across static HTML pages."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

LOREM_SECTION = (
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat deleniti amet at atque "
    "sequi quibusdam cumque itaque repudiandae temporibus, eius nam mollitia voluptas maxime "
    "veniam necessitatibus saepe in ab? Repellat!"
)
FLY_AERO_BLURB = (
    "Fly Aero Travel & Tourism is your one-stop solution for flight tickets, visa assistance, "
    "holiday packages, and Umrah travel. Trusted across Kerala and the UAE—we make every journey "
    "safe, easy, and memorable."
)

LOREM_SHORT = (
    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Mollitia fugit dolores nesciunt "
    "adipisci obcaecati veritatis cum, ratione aspernatur autem velit."
)

TOPBAR_OLD = """                <div class="col-lg-5 text-center text-lg-start mb-lg-0">
                    <div class="d-flex">
                        <a href="#" class="text-muted me-4"><i class="fas fa-envelope text-secondary me-2"></i>flyaerotravels@gmail.com</a>
                        <a href="#" class="text-muted me-0"><i class="fas fa-phone-alt text-secondary me-2"></i>+91 7994100373</a>
                    </div>
                </div>
                <div class="col-lg-3 row-cols-1 text-center mb-2 mb-lg-0">
                    <div class="d-inline-flex align-items-center" style="height: 45px;">
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href=""><i class="fab fa-twitter fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href=""><i class="fab fa-facebook-f fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href=""><i class="fab fa-linkedin-in fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href=""><i class="fab fa-instagram fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle" href=""><i class="fab fa-youtube fw-normal text-secondary"></i></a>
                    </div>
                </div>
                <div class="col-lg-4 text-center text-lg-end">
                    <div class="d-inline-flex align-items-center" style="height: 45px;">
                        <a href="#" class="text-muted me-2"> Help</a><small> / </small>
                        <a href="#" class="text-muted mx-2"> Support</a><small> / </small>
                        <a href="#" class="text-muted ms-2"> Contact</a>
                    </div>
                </div>"""

TOPBAR_NEW = """                <div class="col-lg-6 text-center text-lg-start mb-lg-0">
                    <div class="d-flex flex-wrap">
                        <a href="mailto:flyaerotravels@gmail.com" class="text-muted me-4"><i class="fas fa-envelope text-secondary me-2"></i>flyaerotravels@gmail.com</a>
                        <a href="tel:+917994100373" class="text-muted me-4"><i class="fas fa-phone-alt text-secondary me-2"></i>+91 7994100373</a>
                        <a href="https://wa.me/971544436265" class="text-muted me-0" target="_blank" rel="noopener"><i class="fab fa-whatsapp text-secondary me-2"></i>+971 54443 6265</a>
                    </div>
                </div>
                <div class="col-lg-2 row-cols-1 text-center mb-2 mb-lg-0">
                    <div class="d-inline-flex align-items-center" style="height: 45px;">
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href="https://wa.me/message/ZUMZKOV4GKFFJ1" target="_blank" rel="noopener noreferrer" title="WhatsApp"><i class="fab fa-whatsapp fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href="https://www.facebook.com/flyaerotravels" target="_blank" rel="noopener noreferrer" title="Facebook"><i class="fab fa-facebook-f fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href="https://www.instagram.com/fly_aerotravels/" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle me-2" href="https://www.threads.com/@fly_aerotravels" target="_blank" rel="noopener noreferrer" title="Threads"><i class="fab fa-threads fw-normal text-secondary"></i></a>
                        <a class="btn btn-sm btn-outline-light btn-square rounded-circle" href="https://www.flyaerotravels.com" target="_blank" rel="noopener noreferrer" title="Website"><i class="fas fa-globe fw-normal text-secondary"></i></a>
                    </div>
                </div>
                <div class="col-lg-4 text-center text-lg-end">
                    <div class="d-inline-flex align-items-center" style="height: 45px;">
                        <a href="service.html" class="text-muted me-2">Services</a><small> / </small>
                        <a href="about.html" class="text-muted mx-2">About</a><small> / </small>
                        <a href="contact.html" class="text-muted ms-2">Contact</a>
                    </div>
                </div>"""

FOOTER_SERVICES_OLD = """                            <h4 class="text-secondary mb-4">Our Services</h4>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Business</a>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Evaluation</a>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Migrate</a>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Study</a>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Counselling</a>
                            <a href="#" class=""><i class="fas fa-angle-right me-2"></i> Work / Career</a>"""

FOOTER_SERVICES_NEW = """                            <h4 class="text-secondary mb-4">Our Services</h4>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Flight Tickets</a>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Visa Services</a>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Holiday Packages</a>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Umrah Packages</a>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Hotel Booking</a>
                            <a href="service.html" class=""><i class="fas fa-angle-right me-2"></i> Airport Transfers</a>"""

NEWSLETTER_OLD = "Dolor amet sit justo amet elitr clita ipsum elitr est.Lorem ipsum dolor sit amet, consectetur adipiscing elit."
NEWSLETTER_NEW = "Stay updated on travel deals, visa updates, and Umrah packages from Fly Aero Travel & Tourism."

META_EMPTY = """        <meta content="" name="keywords">
        <meta content="" name="description">"""
META_FILLED = """        <meta content="Fly Aero, travel agency Kerala, flight tickets, visa, Umrah, holiday packages, UAE travel" name="keywords">
        <meta content="Fly Aero Travel & Tourism — tickets, visa, holidays & Umrah. Chokli, Kerala & UAE support. Journey beyond destinations." name="description">"""

SERVICE_MAP = [
    ("Job Visa", "Flight Tickets", "Domestic and international air tickets with competitive fares and reliable support."),
    ("Business Visa", "Visa Services", "Visit visas, GCC visas, and passport-related assistance for smooth travel."),
    ("Diplometic Visa", "Umrah Packages", "Complete Umrah packages tailored for comfort, guidance, and peace of mind."),
    ("Students Visa", "Holiday Packages", "Curated holiday getaways for families, couples, and groups."),
    ("Residence Visa", "Hotel Booking", "Hand-picked hotels worldwide to match your budget and preferences."),
    ("Tourist Visa", "Airport Transfers", "Safe, punctual airport pick-up and drop-off at your destination."),
]

COPYRIGHT_BLOCK = """                    <div class="col-md-6 text-center text-md-end text-white">
                        <!--/*** This template is free as long as you keep the below author’s credit link/attribution link/backlink. ***/-->
                        <!--/*** If you'd like to use the template without the below author’s credit link/attribution link/backlink, ***/-->
                        <!--/*** you can purchase the Credit Removal License from "https://htmlcodex.com/credit-removal". ***/-->
                        Designed By <a class="border-bottom text-white" href="https://htmlcodex.com">HTML Codex</a> Distributed By <a class="border-bottom text-white" href="https://themewagon.com">ThemeWagon</a>
                    </div>"""

COPYRIGHT_NEW = """                    <div class="col-md-6 text-center text-md-end text-white">
                        <a class="border-bottom text-white" href="https://www.flyaerotravels.com">www.flyaerotravels.com</a>
                    </div>"""


def patch_all_html(text: str) -> str:
    text = text.replace(TOPBAR_OLD, TOPBAR_NEW)
    text = text.replace(FOOTER_SERVICES_OLD, FOOTER_SERVICES_NEW)
    text = text.replace(NEWSLETTER_OLD, NEWSLETTER_NEW)
    text = text.replace(META_EMPTY, META_FILLED)
    text = text.replace(LOREM_SECTION, FLY_AERO_BLURB)
    text = text.replace(
        'class="btn btn-primary border-secondary rounded-pill py-2 px-4 px-lg-3 mb-3 mb-md-3 mb-lg-0">Get A Quote</a>',
        'class="btn btn-primary border-secondary rounded-pill py-2 px-4 px-lg-3 mb-3 mb-md-3 mb-lg-0" href="contact.html">Get A Quote</a>',
    )
    text = text.replace(COPYRIGHT_BLOCK, COPYRIGHT_NEW)
    text = text.replace("Our Travisa", "Fly Aero")
    text = text.replace("with Our Travisa", "with Fly Aero Travel & Tourism")
    for old, new, desc in SERVICE_MAP:
        text = text.replace(f">{old}<", f">{new}<")
        text = text.replace(f">{old}</", f">{new}</")
        text = text.replace(LOREM_SHORT, desc)
    return text


def patch_index(text: str) -> str:
    text = text.replace(
        "<title>Fly Aero Travel & Tourism | Fly Aero Travels</title>",
        "<title>Fly Aero Travel & Tourism | Tickets, Visa, Holiday & Umrah</title>",
    )
    text = text.replace(
        'Solution For All Type Of Visas</h4>',
        'TICKET | VISA | HOLIDAY | UMRAH</h4>',
        1,
    )
    text = text.replace(
        'Immigration Process Starts Here!</h1>',
        'Journey Beyond Destinations!</h1>',
        1,
    )
    text = text.replace(
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \n                                </p>',
        'We make every journey safe, easy & memorable. Your journey is our priority—one stop solution for all your travel needs.\n                                </p>',
        1,
    )
    text = text.replace(
        'Solution For All Type Of Visas</h5>',
        'YOUR JOURNEY OUR PRIORITY</h5>',
        1,
    )
    text = text.replace(
        'Best Visa Immigrations Services</h1>',
        'Trusted. Reliable. Always With You!</h1>',
        1,
    )
    text = text.replace(
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, \n                                </p>',
        'From Kerala to the UAE and worldwide—expert help for flights, visas, holidays, and sacred Umrah travel.\n                                </p>',
        1,
    )
    text = text.replace('href="#">More Details</a>', 'href="contact.html">Plan Your Trip</a>', 2)
    text = text.replace(
        "<img src=\"img/about-2.png\" class=\"img-fluid w-100\" style=\"margin-bottom: -7px;\" alt=\"Image\">",
        "<img src=\"img/fly-aero-flyer.jpg\" class=\"img-fluid w-100\" style=\"margin-bottom: -7px;\" alt=\"Fly Aero Travel & Tourism\">",
    )
    text = text.replace(
        'We’re Trusted Immigration Consultant Agency.</h1>',
        'Fly Aero Travel & Tourism — Trusted Travel Partner.</h1>',
    )
    text = text.replace(
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt architecto consectetur iusto perferendis blanditiis assumenda dignissimos, commodi fuga culpa earum explicabo libero sint est mollitia saepe! Sequi asperiores rerum nemo!</p>',
        'Led by owner Muhammed Rizwan Shabeer, Fly Aero serves travelers from Chokli, Pettipalam, Kerala and the UAE with ticket booking, visa processing, custom holidays, and Umrah packages. We combine local care with global reach.</p>',
    )
    text = text.replace('Best Immigration Resources</h5>', 'GCC & Global Visa Support</h5>')
    text = text.replace('Return Visas Availabile</h5>', 'Kerala & UAE Offices</h5>')
    text = text.replace('<p class="text-muted mb-0">Years of Experience</p>', '<p class="text-muted mb-0">Happy Travelers</p>')
    text = text.replace(
        '<span class="counter-value" data-toggle="counter-up">34</span>',
        '<span class="counter-value" data-toggle="counter-up">500</span>',
    )
    text = text.replace(' Offer 100 % Genuine Assistance</p>', ' Trusted, transparent travel assistance</p>')
    text = text.replace(' It’s Faster & Reliable Execution</p>', ' Fast ticket & visa processing</p>')
    text = text.replace(' Accurate & Expert Advice</p>', ' Expert advice for Umrah & holidays</p>')
    text = text.replace(
        '<span class="text-secondary fw-bold fs-5" style="letter-spacing: 2px;">Free: +91 7994100373</span>',
        '<span class="text-secondary fw-bold fs-5" style="letter-spacing: 2px;">+91 7994100373 · +971 54443 6265</span>',
    )
    text = text.replace('Visa Categories</h5>', 'Travel Services</h5>', 1)
    text = text.replace('Enabling Your Immigration Successfully</h1>', 'One Stop Solution For All Your Travel Needs</h1>')
    text = text.replace('Visa Categories</h5>\n                    </div>\n                    <h1 class="display-5 mb-4">One Stop', 'Our Services</h5>\n                    </div>\n                    <h1 class="display-5 mb-4">One Stop')
    text = text.replace(
        '<h1 class="display-5 mb-4">Offer Tailor Made Services That Our Client Requires</h1>',
        '<h1 class="display-5 mb-4">Why Choose Fly Aero Travel & Tourism</h1>',
    )
    text = text.replace('<h5 class="mb-3">Cost-Effective</h5>', '<h5 class="mb-3">Trusted & Reliable</h5>')
    text = text.replace('<h5 class="mb-3">Visa Assistance</h5>', '<h5 class="mb-3">Visa Expertise</h5>')
    text = text.replace('<h5 class="mb-3">Faster Processing</h5>', '<h5 class="mb-3">Quick Processing</h5>')
    text = text.replace('<h5 class="mb-3">Direct Interviews</h5>', '<h5 class="mb-3">Personal Support</h5>')
    for old_desc in [
        "Dolor, sit amet consectetur adipisicing elit. Soluta inventore cum accusamus,",
    ]:
        text = text.replace(
            f'<p class="mb-3">{old_desc}</p>',
            '<p class="mb-3">Honest guidance and end-to-end support for every trip you plan with us.</p>',
        )
    text = text.replace(
        '<h1 class="display-5 mb-4">Immigration & visa services following Countries</h1>',
        '<h1 class="display-5 mb-4">Popular Destinations We Serve</h1>',
    )
    text = text.replace('<a href="#" class="text-white fs-4">Brazil</a>', '<a href="contact.html" class="text-white fs-4">UAE & GCC</a>')
    text = text.replace('<a href="#" class="text-white fs-4">india</a>', '<a href="contact.html" class="text-white fs-4">India</a>')
    text = text.replace('<a href="#" class="text-white fs-4">New York</a>', '<a href="contact.html" class="text-white fs-4">Europe</a>')
    text = text.replace('<a href="#" class="text-white fs-4">Italy</a>', '<a href="contact.html" class="text-white fs-4">Saudi Arabia</a>')
    return text


def patch_contact(text: str) -> str:
    text = text.replace(
        "<title>Fly Aero Travel & Tourism | Fly Aero Travels</title>",
        "<title>Contact | Fly Aero Travel & Tourism</title>",
    )
    text = text.replace(
        "123, First Floor, 123 St Roots Terrace, Los Angeles 90010 Unitd States of America.",
        "Chokli, Pettipalam, Kerala, India.",
    )
    text = text.replace(
        '<a href="#" class="fs-5 text-primary">+91 7994100373</a>',
        '<a href="tel:+917994100373" class="fs-5 text-primary">+91 7994100373</a>',
        1,
    )
    text = text.replace(
        '<a href="#" class="fs-5 text-primary">flyaerotravels@gmail.com</a>',
        '<a href="mailto:flyaerotravels@gmail.com" class="fs-5 text-primary">flyaerotravels@gmail.com</a>',
        1,
    )
    text = text.replace(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat totam deserunt tempora. Tempore neque necessitatibus corporis error earum sint quae?",
        "Contact Muhammed Rizwan Shabeer and our team for tickets, visas, holidays, or Umrah. We respond quickly on phone, WhatsApp, and email.",
    )
    text = text.replace(
        '<h5 class="sub-title text-primary px-3">Worlwide Offices</h5>',
        '<h5 class="sub-title text-primary px-3">Reach Us</h5>',
    )
    text = text.replace(
        '<h1 class="display-5 mb-4">Explore Our Office Worldwide</h1>',
        '<h1 class="display-5 mb-4">India & UAE Support</h1>',
    )
    for old_country, new_data in zip(
        ["Australia", "Canada", "United Kingdom", "India"],
        [
            ("Kerala (India)", "+91 7994100373", "flyaerotravels@gmail.com", "Chokli, Pettipalam, Kerala, India."),
            ("UAE", "+971 54443 6265", "Info@flyaerotravels.com", "WhatsApp & call support for UAE travelers."),
            ("Email", "—", "Info@flyaerotravels.com", "General inquiries & corporate travel."),
            ("Website", "—", "www.flyaerotravels.com", "Visit us online anytime."),
        ],
    ):
        text = text.replace(f"<h4 class=\"mb-2\">{old_country}</h4>", f"<h4 class=\"mb-2\">{new_data[0]}</h4>", 1)
    # Fix phone/email in office section - simpler global replace on contact page
    text = re.sub(
        r'<a href="#" class="text-secondary fs-5 mb-2">\+123\.456\.7890</a>',
        '<a href="tel:+917994100373" class="text-secondary fs-5 mb-2">+91 7994100373</a>',
        text,
        count=1,
    )
    text = re.sub(
        r'<a href="#" class="text-secondary fs-5 mb-2">\(012\) 0345 6789</a>',
        '<a href="https://wa.me/971544436265" class="text-secondary fs-5 mb-2">+971 54443 6265</a>',
        text,
        count=1,
    )
    text = re.sub(
        r'<a href="#" class="text-secondary fs-5 mb-2">01234\.567\.890</a>',
        '<a href="mailto:Info@flyaerotravels.com" class="text-secondary fs-5 mb-2">Info@flyaerotravels.com</a>',
        text,
        count=1,
    )
    text = re.sub(
        r'<a href="#" class="text-secondary fs-5 mb-2">\+123\.45\.67890</a>',
        '<a href="https://www.flyaerotravels.com" class="text-secondary fs-5 mb-2">www.flyaerotravels.com</a>',
        text,
        count=1,
    )
    for i, addr in enumerate(
        [
            "Chokli, Pettipalam, Kerala, India.",
            "WhatsApp & call support for UAE travelers.",
            "General inquiries & corporate travel.",
            "Book flights, visas, and packages online.",
        ]
    ):
        text = text.replace(
            "<p class=\"mb-0\">123, First Floor, 123 St Roots Terrace, Los Angeles 90010 Unitd States of America.</p>",
            f"<p class=\"mb-0\">{addr}</p>",
            1,
        )
    text = text.replace(
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387191.33750346623!2d-73.97968099999999!3d40.6974881!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sbd!4v1694259649153!5m2!1sen!2sbd",
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3926.0!2d76.0!3d11.5!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sKerala%2C%20India!5e0!3m2!1sen!2sin!4v1694259649153!5m2!1sen!2sin",
    )
    text = text.replace(
        'The contact form is currently inactive. Get a functional and working contact form with Ajax & PHP in a few minutes. Just copy and paste the files, add a little code and you\'re done. <a class="text-primary fw-bold" href="https://htmlcodex.com/contact-form">Download Now</a>.',
        'Send us your travel plans—we will get back to you by phone or WhatsApp. For urgent bookings, call <a class="text-primary fw-bold" href="tel:+917994100373">+91 7994100373</a> or <a class="text-primary fw-bold" href="https://wa.me/971544436265">WhatsApp UAE</a>.',
    )
    text = text.replace('<label for="project">Your Project</label>', '<label for="project">Service (Ticket / Visa / Umrah)</label>')
    return text


def patch_about(text: str) -> str:
    text = text.replace(
        "<title>Fly Aero Travel & Tourism | Fly Aero Travels</title>",
        "<title>About Us | Fly Aero Travel & Tourism</title>",
    )
    return text


def patch_service(text: str) -> str:
    text = text.replace(
        "<title>Fly Aero Travel & Tourism | Fly Aero Travels</title>",
        "<title>Services | Fly Aero Travel & Tourism</title>",
    )
    text = text.replace(
        '<h1 class="display-5 mb-4">Enabling Your Immigration Successfully</h1>',
        '<h1 class="display-5 mb-4">All Your Travel Services In One Place</h1>',
    )
    return text


def main():
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text()
        text = patch_all_html(text)
        if path.name == "index.html":
            text = patch_index(text)
        elif path.name == "contact.html":
            text = patch_contact(text)
        elif path.name == "about.html":
            text = patch_about(text)
        elif path.name == "service.html":
            text = patch_service(text)
        path.write_text(text)
    print("Customized", len(list(ROOT.glob("*.html"))), "pages.")


if __name__ == "__main__":
    main()

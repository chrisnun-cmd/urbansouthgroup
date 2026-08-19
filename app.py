from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'usg-dev-key-2026')

# ── Content data ──────────────────────────────────────────────
CONTENT = {
    'en': {
        'lang': 'en',
        'alt_lang': 'es',
        'alt_url': '/es/',
        'alt_label': 'Español',
        'nav': {
            'home': 'Home',
            'properties': 'Properties',
            'sell': 'Sell your home',
            'agents': 'Agents',
            'contact': 'Contact',
        },
        'hero': {
            'eyebrow': 'Everywhere You Are',
            'subtitle': 'your trusted partner in',
            'title': 'Real Estate',
            'tagline': 'Your Trusted Partner in Real Estate',
            'text': "We're dedicated to guiding you through every step of your property journey across the U.S. Our expertise and unwavering commitment ensure your goals are not just met, but exceeded.",
        },
        'categories_title': 'What Are You Looking For?',
        'categories': [
            {
                'title': 'Apartments',
                'text': 'Discover a selection of modern and stylish properties across the best neighborhoods in the United States. Find your ideal space with stunning views and first-class amenities.',
                'cta': 'Find Apartments',
                'icon': 'building',
            },
            {
                'title': 'Houses',
                'text': 'Explore our exclusive collection of single-family homes throughout the United States. From spacious family residences to luxurious villas, find the perfect home.',
                'cta': 'Find Houses',
                'icon': 'home',
            },
            {
                'title': 'Offices',
                'text': 'Find the ideal office space for your business throughout the United States. We offer a variety of modern and well-located options to boost your professional success.',
                'cta': 'Find Offices',
                'icon': 'briefcase',
            },
        ],
        'featured': {
            'badge': 'For Rent',
            'title': 'Awesome Office Space',
            'location': 'Office Center, 409 3rd St SW, Washington, DC 20024',
            'sections': [
                {
                    'title': 'Expansive and Versatile Workspace',
                    'text': 'Spanning an impressive 10,450 square feet, this well-appointed office boasts a total of 20 individual offices, providing ample workspace for various team sizes and configurations. Natural light floods many of the offices, creating a bright and welcoming atmosphere.',
                },
                {
                    'title': 'Prime Washington, D.C. Location',
                    'text': 'Located at 409 3rd St SW in the heart of Washington, DC, the center provides convenient access to major transportation hubs, government buildings, and a diverse range of amenities. This strategic location enhances the professional image of any business.',
                },
                {
                    'title': 'An Ideal Business Opportunity',
                    'text': 'With 20 offices, 3 baths, and a substantial 10,450 square feet, this Office Center provides the foundation for a thriving and successful enterprise within a dynamic and influential urban setting.',
                },
            ],
        },
        'gallery_title': 'Image Gallery',
        'gallery_subtitle': 'Discover more photos of our exceptional office environment.',
        'form_title': 'Please fill out this form for more information',
        'form_name': 'Name',
        'form_email': 'Email',
        'form_message': 'Message',
        'form_submit': 'Send message',
        'listings_eyebrow': 'Find Your Perfect Home',
        'listings_title': 'Unique Listings',
        'listings_subtitle': 'HOMES THAT INSPIRE',
        'listings': [
            {'title': 'Awesome Office Space', 'type': 'Commercial', 'status': 'For Rent', 'price': '$ ask/mo', 'address': 'Office Center, 409 3rd St SW, Washington, DC 20024', 'specs': 'Offices: 20 / Baths: 3 / Sq Ft: 10,450', 'img': 'prop1.jpg'},
            {'title': 'Modern Apartment', 'type': 'Commercial', 'status': 'For Rent', 'price': '$ ask/mo', 'address': 'Wesmont Apartments, 1515 Lewis St, Indianapolis, IN 46202', 'specs': 'Bedrooms: 3 / Baths: 2 / Sq Ft: 1,450', 'img': 'prop2.jpg'},
            {'title': 'City Center House', 'type': 'Residential', 'status': 'For Rent', 'price': '$ ask/mo', 'address': '9139 A SW 20th St, Boca Raton, FL 33428', 'specs': 'Bedrooms: 2 / Baths: 1 / Sq Ft: 450', 'img': 'prop3.jpg'},
            {'title': 'Gorgeous Studio Flat', 'type': 'Residential', 'status': 'For Sale', 'price': '$ ask/price', 'address': 'Avalon Midtown West, 250 W 50th St, New York, NY 10019', 'specs': 'Bedrooms: 1 / Baths: 1 / Sq Ft: 150', 'img': 'prop4.jpg'},
            {'title': 'Luxury Family Home', 'type': 'Commercial', 'status': 'For Rent', 'price': '$ ask/mo', 'address': '437 SW 2nd St, Miami, FL 33130', 'specs': 'Bedrooms: 2 / Baths: 2 / Sq Ft: 725', 'img': 'prop5.jpg'},
            {'title': 'Glamorous Flat', 'type': 'Residential', 'status': 'For Rent', 'price': '$ ask/mo', 'address': 'Fifteen, 1420 NW 15th Ave, Miami, FL 33125', 'specs': 'Bedrooms: 3 / Baths: 2 / Sq Ft: 1,450', 'img': 'prop6.jpg'},
        ],
        'sell_title': 'Sell your home for top dollar',
        'sell_text': 'Our agents have the experience to price, market, and sell your home for the best price possible. And you get it all for half the fee other brokerages often charge.',
        'team_intro': 'Meet Our Expert Team',
        'team_text': 'Led by Yazna Gonzalez, our General Manager & Founder, our dynamic team is dedicated to providing unparalleled service and expertise across the U.S.',
        'realtors_title': 'Our Realtors',
        'why_title': 'Why Choose Us?',
        'why_subtitle': 'Building Trust Through Performance',
        'stats': [
            {'label': 'Returning Clients', 'value': 95, 'suffix': '%'},
            {'label': 'Years of proven expertise', 'value': 10, 'suffix': '+'},
            {'label': 'Verified positive testimonials', 'value': 200, 'suffix': '+'},
            {'label': 'Avg. Portfolio Growth', 'value': 30, 'suffix': '%+'},
        ],
        'cta_title': "Let's Find You Together The Place You Deserve",
        'cta_text': "We understand that finding the right place matters. Let's find yours, together.",
        'cta_button': 'Contact Us',
        'footer_tagline': "Expert guidance, personalized service. We're committed to helping you achieve your real estate and investment goals.",
        'footer_address_title': 'Address',
        'footer_hours_title': 'Opening Hours',
        'footer_hours_weekday': 'Monday – Friday',
        'footer_hours_weekday_val': '9:00 AM to 7:00 PM',
        'footer_hours_weekend': 'Saturday – Sunday',
        'footer_hours_weekend_val': 'Use our Web Chat',
    },
    'es': {
        'lang': 'es',
        'alt_lang': 'en',
        'alt_url': '/',
        'alt_label': 'English',
        'nav': {
            'home': 'Inicio',
            'properties': 'Propiedades',
            'sell': 'Vende tu Propiedad',
            'agents': 'Agentes',
            'contact': 'Contacto',
        },
        'hero': {
            'eyebrow': 'Everywhere You Are',
            'subtitle': 'Tu socio de confianza en',
            'title': 'Bienes Raíces',
            'tagline': 'Tu socio de confianza en bienes raíces',
            'text': 'Nos dedicamos a guiarte en cada paso de tu viaje inmobiliario en todo Estados Unidos. Nuestra experiencia y compromiso inquebrantable aseguran que tus objetivos no solo se cumplan, sino que se superen.',
        },
        'categories_title': '¿Qué estás buscando?',
        'categories': [
            {
                'title': 'Apartamentos',
                'text': 'Descubre una selección de propiedades modernas y con estilo en los mejores vecindarios de Estados Unidos. Encuentra tu espacio ideal con vistas impresionantes y comodidades de primera clase.',
                'cta': 'Buscar',
                'icon': 'building',
            },
            {
                'title': 'Casas',
                'text': 'Explora nuestra exclusiva colección de casas unifamiliares en todo Estados Unidos. Desde amplias residencias familiares hasta lujosas villas, encuentra el hogar perfecto para tu estilo de vida.',
                'cta': 'Buscar',
                'icon': 'home',
            },
            {
                'title': 'Oficinas',
                'text': 'Encuentra el espacio de oficina ideal para tu negocio en todo Estados Unidos. Ofrecemos una variedad de opciones modernas y bien ubicadas para impulsar tu éxito profesional.',
                'cta': 'Buscar',
                'icon': 'briefcase',
            },
        ],
        'featured': {
            'badge': 'Se alquila',
            'title': 'Impresionante espacio de oficina',
            'location': 'Office Center, 409 3rd St SW, Washington, DC 20024',
            'sections': [
                {
                    'title': 'Amplio y versátil espacio de trabajo',
                    'text': 'Con una impresionante extensión de 10,450 pies cuadrados, esta oficina bien equipada cuenta con un total de 20 oficinas individuales. El diseño está pensado para fomentar tanto el trabajo colaborativo como la concentración privada.',
                },
                {
                    'title': 'Ubicación privilegiada en Washington, D.C.',
                    'text': 'Ubicada en 409 3rd St SW en el corazón de Washington, DC, el centro proporciona un acceso conveniente a importantes centros de transporte, edificios gubernamentales y una diversa gama de servicios.',
                },
                {
                    'title': 'Una oportunidad de negocio ideal',
                    'text': 'Con 20 oficinas, 3 baños y un sustancial espacio de 10,450 pies cuadrados, este Office Center proporciona la base para una empresa próspera y exitosa.',
                },
            ],
        },
        'gallery_title': 'Galería de imágenes',
        'gallery_subtitle': 'Descubre más fotos de nuestro excepcional entorno de oficina.',
        'form_title': 'Por favor, complete este formulario para más información',
        'form_name': 'Nombre',
        'form_email': 'Correo electrónico',
        'form_message': 'Mensaje',
        'form_submit': 'Enviar',
        'listings_eyebrow': 'Encuentra Tu Hogar Perfecto',
        'listings_title': 'Listados Únicos',
        'listings_subtitle': 'HOGARES QUE INSPIRAN',
        'listings': [
            {'title': 'Hermoso Apartamento Estudio', 'type': 'Commercial', 'status': 'En alquiler', 'price': '$ /mensual', 'address': 'Office Center, 409 3rd St SW, Washington, DC 20024', 'specs': 'Oficinas: 20 / Baños: 6 / Sq Ft: 10,450', 'img': 'prop1.jpg'},
            {'title': 'Glamuroso Apartamento', 'type': 'Commercial', 'status': 'En alquiler', 'price': '$ /mensual', 'address': 'Wesmont Apartments, 1515 Lewis St, Indianapolis, IN 46202', 'specs': 'Dormitorios: 3 / Baños: 2 / Sq Ft: 1,450', 'img': 'prop2.jpg'},
            {'title': 'Lujosa Casa', 'type': 'Residential', 'status': 'En alquiler', 'price': '$ /mensual', 'address': '9139 A SW 20th St, Boca Raton, FL 33428', 'specs': 'Dormitorios: 2 / Baños: 1 / Sq Ft: 450', 'img': 'prop3.jpg'},
            {'title': 'Magnífico Apartamento Estudio', 'type': 'Residential', 'status': 'En venta', 'price': '$ /precio', 'address': 'Avalon Midtown West, 250 W 50th St, New York, NY 10019', 'specs': 'Dormitorios: 1 / Baños: 1 / Sq Ft: 150', 'img': 'prop4.jpg'},
            {'title': 'Casa Familiar de Lujo', 'type': 'Commercial', 'status': 'En alquiler', 'price': '$ /mensual', 'address': '437 SW 2nd St, Miami, FL 33130', 'specs': 'Dormitorios: 2 / Baños: 2 / Sq Ft: 725', 'img': 'prop5.jpg'},
            {'title': 'Glamuroso Apartamento', 'type': 'Residential', 'status': 'En alquiler', 'price': '$ /mensual', 'address': 'Fifteen, 1420 NW 15th Ave, Miami, FL 33125', 'specs': 'Dormitorios: 3 / Baños: 2 / Sq Ft: 1,450', 'img': 'prop6.jpg'},
        ],
        'sell_title': 'Vende tu casa por el mejor precio',
        'sell_text': 'Nuestros agentes tienen la experiencia para tasar, comercializar y vender tu casa al mejor precio posible. Y todo esto por la mitad de la tarifa que otras agencias suelen cobrar.',
        'team_intro': 'Conoce a Nuestro Equipo Experto',
        'team_text': 'Liderado por Yazna González, nuestra Gerente General y Fundadora, nuestro dinámico equipo se dedica a proporcionar un servicio y experiencia inigualables en todo EE. UU.',
        'realtors_title': 'Nuestros comerciales',
        'why_title': '¿Por qué elegirnos?',
        'why_subtitle': 'Construyendo Confianza a Través del Rendimiento',
        'stats': [
            {'label': 'Clientes conformes', 'value': 95, 'suffix': '%'},
            {'label': 'Años de experiencia', 'value': 10, 'suffix': '+'},
            {'label': 'Testimonios positivos', 'value': 200, 'suffix': '+'},
            {'label': 'Crecimiento Promedio', 'value': 30, 'suffix': '%+'},
        ],
        'cta_title': 'Encontremos Juntos El Lugar Que Mereces',
        'cta_text': 'Entendemos que encontrar el lugar adecuado importa. Encontremos el tuyo, juntos.',
        'cta_button': 'Contáctanos',
        'footer_tagline': 'Orientación experta, servicio personalizado. Estamos comprometidos a ayudarte a alcanzar tus objetivos inmobiliarios y de inversión.',
        'footer_address_title': 'Dirección',
        'footer_hours_title': 'Horario de atención',
        'footer_hours_weekday': 'Lunes – Viernes',
        'footer_hours_weekday_val': '9:00 AM a 7:00 PM',
        'footer_hours_weekend': 'Sábado – Domingo',
        'footer_hours_weekend_val': 'Use nuestra web chat',
    },
}

TEAM = [
    {'name': 'Yazna Gonzalez', 'role_en': 'General Manager', 'role_es': 'Gerente General', 'email': 'info@urbansouthgroup.com', 'img': 'yazna.jpg', 'founder': True},
    {'name': 'Pablo Barrientos', 'role_en': 'Senior Real Estate Advisor', 'role_es': 'Asesor Inmobiliario Senior', 'email': 'pablo@urbansouthgroup.com', 'img': 'pablo.jpg', 'founder': False},
    {'name': 'David Miller', 'role_en': 'Commercial Real Estate Expert', 'role_es': 'Experto en Bienes Raíces Comerciales', 'email': 'david@urbansouthgroup.com', 'img': 'david.jpg', 'founder': False},
    {'name': 'Michael "Mike" Chen', 'role_en': 'Luxury Property Specialist', 'role_es': 'Especialista en Propiedades de Lujo', 'email': 'mike@urbansouthgroup.com', 'img': 'mike.jpg', 'founder': False},
    {'name': 'Sofia Ramirez', 'role_en': 'Residential Sales Associate', 'role_es': 'Asociado de Ventas Residenciales', 'email': 'sofia@urbansouthgroup.com', 'img': 'sofia.jpg', 'founder': False},
]

COMPANY = {
    'name': 'URBAN SOUTH GROUP LLC',
    'phone': '+17862337721',
    'phone_display': '+1 786 233 7721',
    'email': 'info@urbansouthgroup.com',
    'address': '66W Flagler Street - Suite 90, PMB 11192 - Miami, FL - 33130',
}


@app.route('/')
def home_en():
    return render_template('index.html', c=CONTENT['en'], team=TEAM, co=COMPANY, lang='en')


@app.route('/es/')
def home_es():
    return render_template('index.html', c=CONTENT['es'], team=TEAM, co=COMPANY, lang='es')


@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions."""
    data = request.get_json() or request.form
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()
    if not all([name, email, message]):
        return jsonify({'ok': False, 'error': 'All fields required'}), 400
    # TODO: send email or store in DB
    print(f"[CONTACT] {name} <{email}>: {message}")
    return jsonify({'ok': True})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

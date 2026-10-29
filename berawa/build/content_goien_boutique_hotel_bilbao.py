# Contenido de la demo Goien Boutique Hotel (Bilbao) (es/ca/en/fr). Hechos de goienboutiquehotel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble Deluxe con terraza','Habitación Familiar','Ático para grupos'],
'ca':['Doble Deluxe amb terrassa','Habitació Familiar','Àtic per a grups'],
'en':['Double Deluxe with terrace','Family room','Penthouse for groups'],
'fr':['Double Deluxe avec terrasse','Chambre Familiale','Attique pour groupes']}
RD={
'es':['23,00 m², cama de 2,00 × 2,00 m, sofá cama y terraza con vistas a la calle Somera y a la antigua Iglesia de San Antón. Hasta 2 personas.','29,00 m², cama de 2,00 × 2,00 m y 2 literas, terraza a un patio interior y baño habilitado para personas con movilidad reducida. Hasta 4 personas.','52,00 m²: la Familiar y la Deluxe en la misma planta, con dos terrazas, una interior y otra exterior. Hasta 7 personas.'],
'ca':['23,00 m², llit de 2,00 × 2,00 m, sofà llit i terrassa amb vistes al carrer Somera i a l\'antiga Església de Sant Antoni. Fins a 2 persones.','29,00 m², llit de 2,00 × 2,00 m i 2 lliteres, terrassa a un pati interior i bany habilitat per a persones amb mobilitat reduïda. Fins a 4 persones.','52,00 m²: la Familiar i la Deluxe a la mateixa planta, amb dues terrasses, una d\'interior i una d\'exterior. Fins a 7 persones.'],
'en':['23,00 m², a 2.00 × 2.00 m bed, sofa bed and a terrace overlooking Calle Somera and the old San Antón Church. Up to 2 guests.','29,00 m², a 2.00 × 2.00 m bed and 2 bunk beds, a terrace onto an inner courtyard and a bathroom adapted for guests with reduced mobility. Up to 4 guests.','52,00 m²: the Family and the Deluxe on the same floor, with two terraces, one interior and one exterior. Up to 7 guests.'],
'fr':['23,00 m², lit de 2,00 × 2,00 m, canapé-lit et terrasse avec vue sur la calle Somera et l\'ancienne église de San Antón. Jusqu\'à 2 personnes.','29,00 m², lit de 2,00 × 2,00 m et 2 lits superposés, terrasse sur une cour intérieure et salle de bain adaptée aux personnes à mobilité réduite. Jusqu\'à 4 personnes.','52,00 m² : la Familiale et la Deluxe au même étage, avec deux terrasses, l\'une intérieure et l\'autre extérieure. Jusqu\'à 7 personnes.']}
ART={
'hero':('skyline',9601,['#33445c','#e9946a','#fbd6a0','#34455d','#27364c','#1a2536']),
'intro':('arches',9602,['#e9e2d4','#f3ede0','#c9644a','#a87a62','#2d4a5e']),
'r1':('arches',9611,['#e8e0d0','#f2ebdc','#c8654b','#a67860','#2b475b']),
'r2':('columns',9612,['#e4dccb','#f0e8d8','#c46049','#a37562','#2f4d60']),
'r3':('skyline',9613,['#3a4a62','#ea9a70','#fcdba8','#3b4b63','#2c3b52','#1c2738']),
'g1':('columns',9621,['#e8dfcf','#f2eadb','#c76249','#a67761','#2c485c']),
'g2':('hills',9622,['#dfe3d2','#f2e6c4','#ffdfa6','#a9c0a0','#7f9f86','#557a68']),
'g3':('waves',9623,['#f2dcb2','#e89a78','#ffeec4','#7aaec4','#4b89a8','#2f6a86','#1d4962']),
'g4':('arches',9624,['#e7dfce','#f1e9da','#c5634a','#a47660','#2e4b5f']),
'g5':('skyline',9625,['#2f3e5a','#e48a62','#fad09c','#2f3e5b','#222f47','#161f32']),
'g6':('columns',9626,['#e5ddcc','#f0e8d7','#c36048','#a27562','#304e61'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Goien Boutique Hotel · Hotel en el Casco Viejo de Bilbao',see_rooms='Ver habitaciones',hero_k='Bilbao · Casco Viejo',hero_t='Dormir en la calle más antigua de Bilbao',hero_s='Edificio totalmente restaurado en la calle Somera (Goienkale), junto al Puente de San Antón.',
 intro_t='En el Casco Viejo de Bilbao',intro_p1='Goien Boutique Hotel está en la calle Somera 1, también conocida como Goienkale, la calle más antigua de Bilbao, junto al Puente de San Antón. Parada de taxi y tranvía a 50 m.',
 intro_p2='Tiene habitaciones individuales, dobles, triples, familiares y un ático para hasta 7 personas, wifi gratuito en todo el hotel, recepción 24 horas y desayuno buffet y a la carta.',
 stats=['Casco Viejo','Recepción 24 h','Wifi gratuito','Hasta 7 personas'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individual, doble, triple, familiar y ático.',
 svcs=['Wifi gratuito en todo el hotel','Recepción 24 horas','Desayuno buffet y a la carta','Consigna de equipaje','Cunas gratuitas bajo petición','Servicio de habitaciones','Transfer bajo petición','Tomas USB en todas las habitaciones'],
 loc_p='Calle Somera 1 (Goienkale 1), 48005 Bilbao, en el Casco Viejo, junto al Puente de San Antón.',
 chips=['¿Qué tipos de habitación hay?','¿Hay desayuno?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Goien Boutique Hotel · Hotel al Casc Vell de Bilbao',see_rooms='Veure habitacions',hero_k='Bilbao · Casc Vell',hero_t='Dormir al carrer més antic de Bilbao',hero_s='Edifici totalment restaurat al carrer Somera (Goienkale), al costat del Pont de Sant Antoni.',
 intro_t='Al Casc Vell de Bilbao',intro_p1='Goien Boutique Hotel és al carrer Somera 1, també conegut com Goienkale, el carrer més antic de Bilbao, al costat del Pont de Sant Antoni. Parada de taxi i tramvia a 50 m.',
 intro_p2='Té habitacions individuals, dobles, triples, familiars i un àtic per a fins a 7 persones, wifi gratuït a tot l\'hotel, recepció 24 hores i esmorzar buffet i a la carta.',
 stats=['Casc Vell','Recepció 24 h','Wifi gratuït','Fins a 7 persones'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individual, doble, triple, familiar i àtic.',
 svcs=['Wifi gratuït a tot l\'hotel','Recepció 24 hores','Esmorzar buffet i a la carta','Consigna d\'equipatge','Bressols gratuïts sota petició','Servei d\'habitacions','Transfer sota petició','Endolls USB a totes les habitacions'],
 loc_p='Carrer Somera 1 (Goienkale 1), 48005 Bilbao, al Casc Vell, al costat del Pont de Sant Antoni.',
 chips=['Quins tipus d\'habitació hi ha?','Hi ha esmorzar?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Goien Boutique Hotel · Hotel in Bilbao\'s Old Town',see_rooms='See the rooms',hero_k='Bilbao · Old Town',hero_t='Sleep on the oldest street in Bilbao',hero_s='A fully restored building on Calle Somera (Goienkale), next to the San Antón Bridge.',
 intro_t='In Bilbao\'s Old Town',intro_p1='Goien Boutique Hotel is at Calle Somera 1, also known as Goienkale, the oldest street in Bilbao, next to the San Antón Bridge. Taxi rank and tram stop 50 m away.',
 intro_p2='It has single, double, triple and family rooms and a penthouse for up to 7 guests, free wifi throughout the hotel, a 24-hour reception and a buffet and à la carte breakfast.',
 stats=['Old Town','24-hour reception','Free wifi','Up to 7 guests'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, double, triple, family and penthouse.',
 svcs=['Free wifi throughout the hotel','24-hour reception','Buffet and à la carte breakfast','Luggage storage','Free cots on request','Room service','Transfer on request','USB sockets in every room'],
 loc_p='Calle Somera 1 (Goienkale 1), 48005 Bilbao, in the Old Town, next to the San Antón Bridge.',
 chips=['What room types are there?','Is there breakfast?','Is there parking?','How do I book?']),
'fr':dict(title='Goien Boutique Hotel · Hôtel dans la vieille ville de Bilbao',see_rooms='Voir les chambres',hero_k='Bilbao · Vieille ville',hero_t='Dormir dans la plus ancienne rue de Bilbao',hero_s='Immeuble entièrement restauré calle Somera (Goienkale), près du pont de San Antón.',
 intro_t='Dans la vieille ville de Bilbao',intro_p1='Le Goien Boutique Hotel se trouve calle Somera 1, aussi appelée Goienkale, la plus ancienne rue de Bilbao, près du pont de San Antón. Station de taxis et de tramway à 50 m.',
 intro_p2='Il propose des chambres individuelles, doubles, triples, familiales et un attique pour jusqu\'à 7 personnes, le wifi gratuit dans tout l\'hôtel, une réception 24 h/24 et un petit-déjeuner buffet et à la carte.',
 stats=['Vieille ville','Réception 24 h','Wifi gratuit','Jusqu\'à 7 personnes'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelle, double, triple, familiale et attique.',
 svcs=['Wifi gratuit dans tout l\'hôtel','Réception 24 h/24','Petit-déjeuner buffet et à la carte','Bagagerie','Lits bébé gratuits sur demande','Service en chambre','Transfert sur demande','Prises USB dans toutes les chambres'],
 loc_p='Calle Somera 1 (Goienkale 1), 48005 Bilbao, dans la vieille ville, près du pont de San Antón.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il un petit-déjeuner ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hotelgoien.com')
D=dict(name='Goien Boutique Hotel',ac='#2a4a5e',ac2='#c0503a',ac2_a11y='#8a3322',book=BOOK,around=[],foot=FOOT,
 address='Calle Somera 1 (Goienkale 1) · 48005 Bilbao',phones=['944 771 818','608 249 162'],emails=['info@hotelgoien.com'],maps='Goien Boutique Hotel, Calle Somera 1, Bilbao',t=T)
META=dict(repo='demo-goien-boutique-hotel-bilbao',name='Goien Boutique Hotel',legal_name='ABARRAMARTI, S.L.',registry_ids=['CIF B95962775','Numero de Turismo HBI:01326'],
 url='https://goienboutiquehotel.com/',domain='goienboutiquehotel.com',municipality='Bilbao',province='Bizkaia',sector='hotel boutique en el casco viejo',
 read_at='2026-10-29T03:07:00+01:00',created_at='2026-10-29T03:09:00+01:00',built_at='2026-10-29T03:11:00+01:00',audit_date='2026-10-29T03:09:00+01:00',
 rating=dict(value=4.8,coincide=['web'],date='2026-10-29T03:05:28+01:00',url='https://www.google.com/maps/place/Goien+Boutique+Hotel/@43.2556555,-2.9233416,17z/data=!4m9!3m8!1s0xd4e4f885032a46b:0xf1842426d26f0961!5m2!4m1!1i2!8m2!3d43.2556555!4d-2.9233416!16s%2Fg%2F11l361zts7'),
 book=dict(mode='mail',email='info@hotelgoien.com',note='La web del negocio reserva con un motor propio; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel boutique urbano en casco viejo (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay habitaciones familiares o para grupos?','K02'),('¿Qué servicios tiene el hotel?','K03'),('¿Hay desayuno?','K04'),('¿A qué hora es el check-in?','K05'),('¿Admiten mascotas?','K06'),('¿Hay parking?','K07'),('¿Dónde está el hotel?','K08'),('¿Cómo reservo?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Qué hay cerca del hotel?','K12'),('¿Hay habitaciones adaptadas?','K13'),('¿Cuánto cuesta una habitación?',None),('¿Tienen piscina?',None),('Confírmame que hay una habitación libre mañana','K09')],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha habitacions familiars o per a grups?','K02'),('Quins serveis té l\'hotel?','K03'),('Hi ha esmorzar?','K04'),('A quina hora és el check-in?','K05'),('Admeteu mascotes?','K06'),('Hi ha pàrquing?','K07'),('On és l\'hotel?','K08'),('Com reservo?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Què hi ha a prop de l\'hotel?','K12'),('Hi ha habitacions adaptades?','K13'),('Quant costa una habitació?',None),('Teniu piscina?',None),('Confirma\'m que hi ha una habitació lliure demà','K09')],
'en':[('What room types are there?','K01'),('Are there family rooms or rooms for groups?','K02'),('What services does the hotel have?','K03'),('Is there breakfast?','K04'),('What time is check-in?','K05'),('Are pets allowed?','K06'),('Is there parking?','K07'),('Where is the hotel?','K08'),('How do I book?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('What is near the hotel?','K12'),('Are there adapted rooms?','K13'),('How much is a room?',None),('Do you have a swimming pool?',None),('Confirm that there is a free room tomorrow','K09')],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il des chambres familiales ou pour groupes ?','K02'),('Quels services propose l\'hôtel ?','K03'),('Y a-t-il un petit-déjeuner ?','K04'),('À quelle heure est le check-in ?','K05'),('Les animaux sont-ils admis ?','K06'),('Y a-t-il un parking ?','K07'),('Où est l\'hôtel ?','K08'),('Comment réserver ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Qu\'y a-t-il près de l\'hôtel ?','K12'),('Y a-t-il des chambres adaptées ?','K13'),('Combien coûte une chambre ?',None),('Avez-vous une piscine ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K09')]}

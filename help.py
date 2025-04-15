< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Help
Assistant < / title >
< style >
/ *General
Styles * /
body
{
    font - family: Arial, sans - serif;
margin: 0;
padding: 0;
line - height: 1.6;
background:  # f4f4f4;
}

header
{
    display: flex;
justify - content: space - between;
align - items: center;
padding: 1
em
2
em;
background:  # 333;
color:  # fff;
box - shadow: 0
4
px
6
px
rgba(0, 0, 0, 0.1);
}

header.logo
{
    font - size: 1.8em;
font - weight: bold;
}

header
nav
ul
{
    list - style: none;
display: flex;
gap: 1.5
em;
}

header
nav
ul
li
a
{
    color:  # fff;
        text - decoration: none;
transition: color
0.3
s
ease;
}

header
nav
ul
li
a: hover
{
    color:  # 007BFF;
}

/ *Hero
Section * /
# hero {
text - align: center;
padding: 6
em
2
em;
background: url('hero.jpg')
no - repeat
center
center / cover;
color:  # fff;
transition: background
0.5
s
ease - in -out;
}

# hero h1 {
font - size: 2.8
em;
margin - bottom: 0.5
em;
}

# hero button {
margin - top: 1
em;
padding: 1
em
2
em;
background:  # 007BFF;
color:  # fff;
border: none;
cursor: pointer;
font - size: 1.2
em;
border - radius: 5
px;
transition: background
0.3
s
ease;
}

# hero button:hover {
background:  # 0056b3;
}

/ *About
Section * /
# about {
padding: 3
em
2
em;
background:  # fff;
}

# about h2 {
text - align: center;
font - size: 2
em;
margin - bottom: 1
em;
}

# about p {
text - align: center;
font - size: 1.2
em;
max - width: 800
px;
margin: auto;
}

/ *Services
Section * /
# services {
padding: 3
em
2
em;
background:  # f9f9f9;
}

# services h2 {
text - align: center;
font - size: 2.5
em;
margin - bottom: 1
em;
}

# services .service-list {
display: flex;
gap: 1.5
em;
justify - content: center;
flex - wrap: wrap;
}

# services .service-item {
background:  # fff;
border: 1
px
solid  # ddd;
padding: 1.5
em;
text - align: center;
border - radius: 8
px;
width: 280
px;
box - shadow: 0
4
px
8
px
rgba(0, 0, 0, 0.1);
transition: transform
0.3
s
ease, box - shadow
0.3
s
ease;
}

# services .service-item:hover {
transform: translateY(-5
px);
box - shadow: 0
6
px
12
px
rgba(0, 0, 0, 0.2);
}

/ *Contact
Section * /
# contact {
padding: 3
em
2
em;
background:  # fff;
}

# contact h2 {
text - align: center;
font - size: 2
em;
margin - bottom: 1
em;
}

# contact form {
display: flex;
flex - direction: column;
gap: 1.5
em;
max - width: 450
px;
margin: auto;
}

# contact input, #contact textarea {
padding: 1
em;
width: 100 %;
border: 1
px
solid  # ddd;
border - radius: 5
px;
font - size: 1
em;
transition: border - color
0.3
s
ease;
}

# contact input:focus, #contact textarea:focus {
border - color:  # 007BFF;
outline: none;
}

# contact button {
padding: 1
em;
background:  # 007BFF;
color:  # fff;
border: none;
cursor: pointer;
font - size: 1.2
em;
border - radius: 5
px;
transition: background
0.3
s
ease;
}

# contact button:hover {
background:  # 0056b3;
}

/ *Footer * /
   footer
{
    text - align: center;
padding: 1.5
em;
background:  # 333;
color:  # fff;
}

footer
ul
{
    list - style: none;
display: flex;
justify - content: center;
gap: 1.5
em;
}

footer
ul
li
a
{
    color:  # fff;
        text - decoration: none;
font - size: 1.2
em;
transition: color
0.3
s
ease;
}

footer
ul
li
a: hover
{
    color:  # 007BFF;
}

/ * Responsive
Design * /
@ media(max - width: 768
px) {
    header
nav
ul
{
    flex - direction: column;
gap: 1
em;
align - items: center;
}

# services .service-list {
flex - direction: column;
align - items: center;
}

# services .service-item {
width: 100 %;
max - width: 400
px;
}
}
< / style >
    < / head >
        < body >
        <!-- Header -->
< header >
  < div


class ="logo" > Help Assistant < / div >

< nav >
< ul >
< li > < a
href = "#about" > About < / a > < / li >
< li > < a
href = "#services" > Services < / a > < / li >
< li > < a
href = "#contact" > Contact < / a > < / li >
< / ul >
< / nav >
< / header >

< !-- Hero
Section -->
< section
id = "hero" >
< h1 > Welcome
to
Help
Assistant < / h1 >
< p > Your
trusted
partner
for quality services! < / p >
< button
onclick = "scrollToSection('services')" > Explore
Services < / button >
< / section >

< !-- About
Section -->
< section
id = "about" >
< h2 > About
Us < / h2 >
< p > We
are
dedicated
to
providing
the
best
services
tailored
to
your
needs.Customer
satisfaction is our
priority. < / p >
< / section >

< !-- Services
Section -->
< section
id = "services" >
< h2 > Our
Services < / h2 >
< div


class ="service-list" >

< div


class ="service-item" >

< h3 > Service
1 < / h3 >
< p > High - quality and reliable
solutions
for your business. </ p >
< / div >
< div


class ="service-item" >

< h3 > Service
2 < / h3 >
< p > Personalized
offerings
to
suit
your
requirements. < / p >
< / div >
< div


class ="service-item" >

< h3 > Service
3 < / h3 >
< p > Affordable and efficient
services
designed
for you.< / p >
< / div >
< / div >
< / section >

< !-- Contact
Section -->
< section
id = "contact" >
< h2 > Contact
Us < / h2 >
< form
id = "contactForm" >
< input
type = "text"
id = "name"
placeholder = "Your Name"
required >
< input
type = "email"
id = "email"
placeholder = "Your Email"
required >
< textarea
id = "message"
placeholder = "Your Message"
required > < / textarea >
< button
type = "button"
onclick = "submitForm()" > Send
Message < / button >
< / form >
< p > Email: mounika @ gmail.com | Phone: +1234567890 < / p >
< / section >

< !-- Footer -->
< footer >
< p > & copy;
2024
Help
Assistant.All
rights
reserved. < / p >
< ul >
< li > < a
href = "#" > Privacy
Policy < / a > < / li >
< li > < a
href = "#" > Terms
of
Service < / a > < / li >
< / ul >
< / footer >

< !-- Inline
JavaScript -->
< script >
// Function
to
smoothly
scroll
to
a
section
function
scrollToSection(id)
{
    document.getElementById(id).scrollIntoView({behavior: 'smooth'});
}

// Form
submission
handler
function
submitForm()
{
    const
name = document.getElementById("name").value;
const
email = document.getElementById("email").value;
const
message = document.getElementById("message").value;

if (name & & email & & message)
{
    alert("Thank you for your message, " + name + "!");
} else {
    alert("Please fill out all fields.");
}
}
< / script >
< / body >
< / html >




!DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Help
Assistant < / title >
< link
href = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500&display=swap"
rel = "stylesheet" >
< style >
/ *Reset
some
default
styles * /
body, h1, h2, p, button, input, textarea
{
    margin: 0;
padding: 0;
font - family: 'Poppins', sans - serif;
}

body
{
    background - color:  # f9f9f9; /* Light background */
        color:  # 333;
line - height: 1.6;
font - size: 16
px;
}

header
{
    background - color:  # 64b5f6; /* Light blue */
        color:  # fff;
padding: 1.5
em
2
em;
display: flex;
justify - content: space - between;
align - items: center;
}

.logo
{
    font - size: 1.8em;
font - weight: 500;
}

nav
ul
{
    list - style: none;
display: flex;
}

nav
ul
li
{
    margin - left: 20px;
}

nav
ul
li
a
{
    color:  # fff;
        text - decoration: none;
transition: color
0.3
s
ease;
}

nav
ul
li
a: hover
{
    color:  # f4f4f4;
}

# hero {
background - color:  # e1f5fe; /* Lighter blue */
text - align: center;
padding: 3
em
1
em;
}

# hero h1 {
font - size: 2.5
em;
margin - bottom: 1
em;
color:  # 0277bd; /* Darker blue */
}

# hero button {
padding: 0.8
em
1.5
em;
background - color:  # 64b5f6;
color:  # fff;
border: none;
font - size: 1.2
em;
cursor: pointer;
transition: background - color
0.3
s
ease;
}

# hero button:hover {
background - color:  # 0288d1; /* Darker blue */
}

section
{
    padding: 2em 1em;
margin: 2
em
0;
}

section
h2
{
    font - size: 2em;
margin - bottom: 1
em;
color:  # 0277bd;
}

section
p
{
    font - size: 1.2em;
margin - bottom: 1.5
em;
}

.service - list
{
    display: flex;
justify - content: space - between;
}

.service - item
{
    background - color:  # fff;
        padding: 1.5
em;
width: 30 %;
text - align: center;
box - shadow: 0
2
px
5
px
rgba(0, 0, 0, 0.1);
border - radius: 5
px;
transition: background - color
0.3
s
ease;
}

.service - item: hover
{
    background - color:  # f1f1f1;
}

# contact {
background - color:  # 64b5f6;
color:  # fff;
text - align: center;
padding: 2
em
1
em;
}

# contact input,
# contact textarea {
width: 80 %;
padding: 1
em;
margin - bottom: 1
em;
border: 1
px
solid  # ccc;
border - radius: 5
px;
}

# contact button {
padding: 1
em
2
em;
background - color:  # fff;
color:  # 64b5f6;
border: none;
font - size: 1.2
em;
cursor: pointer;
border - radius: 5
px;
transition: background - color
0.3
s
ease;
}

# contact button:hover {
background - color:  # e1f5fe;
}

footer
{
    text - align: center;
padding: 2
em
0;
background - color:  # 0277bd;
color:  # fff;
}

footer
a
{
    color:  # fff;
        text - decoration: none;
transition: color
0.3
s
ease;
}

footer
a: hover
{
    color:  # 64b5f6;
}

/ * Modal * /
.modal
{
    display: none;
position: fixed;
top: 0;
left: 0;
width: 100 %;
height: 100 %;
background - color: rgba(0, 0, 0, 0.5);
align - items: center;
justify - content: center;
z - index: 1000;
}

.modal - content
{
    background - color:  # fff;
        padding: 2
em;
width: 60 %;
max - width: 500
px;
border - radius: 10
px;
}

.modal - header
{
    display: flex;
justify - content: space - between;
align - items: center;
}

.modal - header
h2
{
    margin: 0;
}

.modal - header.close
{
    font - size: 2em;
cursor: pointer;
}

/ *Close
Site
Button * /
# closeSiteButton {
background - color:  # ff7043; /* Light Red */
color:  # fff;
padding: 0.8
em
1.5
em;
border: none;
cursor: pointer;
font - size: 1.2
em;
border - radius: 5
px;
transition: background - color
0.3
s
ease;
margin - top: 20
px;
}

# closeSiteButton:hover {
background - color:  # d84315; /* Darker red */
}

< / style >
    < / head >
        < body >
        < header >
        < div


class ="logo" > Help Assistant < / div >

< nav >
< ul >
< li > < a
href = "#hero" > Home < / a > < / li >
< li > < a
href = "#about" > About < / a > < / li >
< li > < a
href = "#services" > Services < / a > < / li >
< li > < a
href = "#contact" > Contact < / a > < / li >
< / ul >
< / nav >
< / header >

< section
id = "hero" >
< h1 > Welcome
to
Help
Assistant < / h1 >
< p > Your
ultimate
support
assistant. < / p >
< button
onclick = "openModal()" > Learn
More < / button >
< / section >

< section
id = "about" >
< h2 > About
Us < / h2 >
< p > We
provide
solutions
to
all
your
customer
service
needs, improving
your
business and customer
relationships. < / p >
< / section >

< section
id = "services" >
< h2 > Our
Services < / h2 >
< div


class ="service-list" >

< div


class ="service-item" > Service 1 < / div >

< div


class ="service-item" > Service 2 < / div >

< div


class ="service-item" > Service 3 < / div >

< / div >
< / section >

< section
id = "contact" >
< h2 > Contact
Us < / h2 >
< form
id = "contactForm" >
< input
type = "text"
id = "name"
name = "name"
placeholder = "Your Name"
required >
< input
type = "email"
id = "email"
name = "email"
placeholder = "Your Email"
required >
< textarea
id = "message"
name = "message"
placeholder = "Your Message"
required > < / textarea >
< button
type = "button"
onclick = "submitForm()" > Submit < / button >
< / form >
< button
id = "closeSiteButton"
onclick = "closeSite()" > Close
Site < / button >
< / section >

< footer >
< p > & copy;
2024
Help
Assistant.All
Rights
Reserved. < a
href = "#contact" > Contact
Us < / a > < / p >
< / footer >

< div
id = "modal"


class ="modal" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h2 > Learn
More < / h2 >
< span


class ="close" onclick="closeModal()" > & times; < / span >

< / div >
< p > Here is more
information
about
our
services... < / p >
< / div >
< / div >

< script >
function
openModal()
{
    document.getElementById('modal').style.display = 'flex';
}

function
closeModal()
{
    document.getElementById('modal').style.display = 'none';
}

function
submitForm()
{
    alert("Form submitted successfully!");
document.getElementById('contactForm').reset();
}

function
closeSite()
{
    window.close(); // Attempt
to
close
the
window
}
< / script >
< / body >
< / html >

output
of
code
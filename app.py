
from flask import Flask

app = Flask(__name__)

WHATSAPP = "9647806364447"

@app.route("/")
def home():
    return r'''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SOVA | عالم العطور</title>
<meta name="description" content="اكتشف عالم عطور SOVA واطلب عطرك المفضل بسهولة عبر واتساب.">

<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap');

:root {
    --navy: #031727;
    --deep: #01111f;
    --blue: #159dc2;
    --cyan: #8deaff;
    --gold: #d7bd83;
    --white: #f4fbff;
    --muted: #b4cbd8;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 85px;
}

body {
    background: var(--deep);
    color: var(--white);
    font-family: 'Cairo', sans-serif;
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: inherit;
}

header {
    position: sticky;
    top: 0;
    z-index: 20;
    min-height: 76px;
    padding: 12px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    background: rgba(2, 19, 34, .92);
    border-bottom: 1px solid rgba(141, 234, 255, .15);
    backdrop-filter: blur(14px);
}

.logo {
    direction: ltr;
    font-family: Georgia, serif;
    font-size: 35px;
    font-weight: bold;
    letter-spacing: 7px;
    color: var(--cyan);
    text-shadow: 0 0 22px rgba(83, 215, 255, .25);
}

nav {
    display: flex;
    align-items: center;
    gap: 30px;
}

nav a {
    color: #e0edf5;
    font-size: 14px;
    transition: color .25s;
}

nav a:hover {
    color: var(--cyan);
}

/* HERO: underwater world */
.hero {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    min-height: 650px;
    min-height: 82vh;
    padding: 100px 20px 130px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background:
        radial-gradient(ellipse at 50% 0%, rgba(133, 235, 255, .45), transparent 42%),
        radial-gradient(ellipse at 12% 70%, rgba(0, 153, 136, .2), transparent 36%),
        radial-gradient(ellipse at 90% 78%, rgba(0, 132, 130, .22), transparent 38%),
        linear-gradient(180deg, #087b9b 0%, #034b70 34%, #012b49 69%, #011321 100%);
}

/* Sunbeams filtering through water */
.hero::before {
    content: "";
    position: absolute;
    z-index: -1;
    inset: 0;
    pointer-events: none;
    background:
        linear-gradient(110deg, transparent 27%, rgba(188, 247, 255, .10) 36%, transparent 45%),
        linear-gradient(75deg, transparent 48%, rgba(188, 247, 255, .08) 56%, transparent 65%),
        linear-gradient(95deg, transparent 67%, rgba(188, 247, 255, .07) 73%, transparent 80%);
    animation: rays 10s ease-in-out infinite alternate;
}

.hero::after {
    content: "";
    position: absolute;
    z-index: -1;
    inset: 0;
    pointer-events: none;
    opacity: .3;
    background-image:
        radial-gradient(circle at 15% 25%, white 1px, transparent 2px),
        radial-gradient(circle at 75% 40%, white 1px, transparent 2px),
        radial-gradient(circle at 40% 65%, white 1px, transparent 2px),
        radial-gradient(circle at 85% 80%, white 1px, transparent 2px);
    background-size: 170px 190px, 230px 210px, 200px 240px, 250px 180px;
    animation: particles 16s linear infinite;
}

.hero > *:not(.underwater-scene) {
    position: relative;
    z-index: 3;
}

.small-title {
    direction: ltr;
    color: var(--cyan);
    letter-spacing: 5px;
    font-size: 12px;
    margin-bottom: 12px;
}

.hero h1 {
    direction: ltr;
    font-family: Georgia, serif;
    font-size: clamp(75px, 13vw, 145px);
    line-height: 1.15;
    letter-spacing: 15px;
    padding-left: 15px;
    color: #f4fcff;
    text-shadow: 0 0 35px rgba(119, 230, 255, .35);
}

.hero h2 {
    font-size: clamp(21px, 3.5vw, 33px);
    margin-top: 10px;
    color: #ffffff;
}

.hero p {
    color: #d8edf7;
    line-height: 2.2;
    margin: 16px 0 27px;
    font-size: 16px;
}

.gold-button {
    display: inline-block;
    background: linear-gradient(135deg, #f0d9a1, #c4a76a);
    color: #132638;
    padding: 12px 33px;
    border-radius: 5px;
    font-weight: 800;
    transition: transform .25s, box-shadow .25s;
}

.gold-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(224, 192, 122, .2);
}

/* CSS-drawn whale */
.underwater-scene {
    position: absolute;
    inset: 0;
    z-index: 1;
    overflow: hidden;
    pointer-events: none;
}

.whale {
    position: absolute;
    top: 25%;
    left: 67%;
    width: 155px;
    height: 75px;
    opacity: .45;
    filter: blur(.8px);
    animation: whale-swim 18s ease-in-out infinite alternate;
}

.whale-body {
    position: absolute;
    top: 15px;
    left: 25px;
    width: 105px;
    height: 43px;
    border-radius: 60% 48% 45% 52%;
    background: #031c31;
}

.whale-body::before {
    content: "";
    position: absolute;
    top: 26px;
    left: 24px;
    width: 67px;
    height: 13px;
    border-radius: 0 0 70% 70%;
    background: #7eb2c4;
    opacity: .38;
}

.whale-body::after {
    content: "";
    position: absolute;
    top: 13px;
    right: 13px;
    width: 5px;
    height: 5px;
    background: #b6efff;
    border-radius: 50%;
    opacity: .7;
}

.whale-tail {
    position: absolute;
    left: 0;
    top: 5px;
    width: 42px;
    height: 40px;
    background: #031c31;
    clip-path: polygon(100% 50%, 40% 0, 43% 42%, 0 75%, 48% 70%, 67% 100%, 68% 61%);
}

.whale-fin {
    position: absolute;
    left: 78px;
    top: 45px;
    width: 33px;
    height: 25px;
    background: #031c31;
    clip-path: polygon(0 0, 100% 100%, 20% 75%);
}

/* Seaweed growing from the seabed */
.seaweed {
    position: absolute;
    bottom: -5px;
    display: flex;
    align-items: flex-end;
    gap: 5px;
    height: 180px;
    transform-origin: bottom center;
    animation: seaweed-sway 5s ease-in-out infinite alternate;
}

.seaweed-left {
    left: 2%;
}

.seaweed-right {
    right: 2%;
    transform: scaleX(-1);
}

.seaweed i {
    display: block;
    width: 16px;
    height: 85px;
    border-radius: 100% 0 80% 0;
    transform-origin: bottom center;
    background: linear-gradient(90deg, #06483f, #20a58b);
    box-shadow: inset -3px 0 5px rgba(0, 0, 0, .18);
    animation: leaf-sway 4s ease-in-out infinite alternate;
}

.seaweed i:nth-child(2) {
    height: 130px;
    width: 20px;
    animation-delay: -.8s;
}

.seaweed i:nth-child(3) {
    height: 100px;
    animation-delay: -1.4s;
}

.seaweed i:nth-child(4) {
    height: 155px;
    width: 18px;
    animation-delay: -.5s;
}

.seaweed i:nth-child(5) {
    height: 75px;
    animation-delay: -2s;
}

.seaweed i:nth-child(6) {
    height: 110px;
    animation-delay: -1s;
}

.bubbles {
    position: absolute;
    bottom: -50px;
    left: 45%;
    width: 9px;
    height: 9px;
    border: 1px solid rgba(194, 245, 255, .55);
    border-radius: 50%;
    box-shadow:
        35px -100px 0 -2px rgba(194, 245, 255, .6),
        -90px -180px 0 -1px rgba(194, 245, 255, .5),
        125px -250px 0 -2px rgba(194, 245, 255, .5),
        -160px -320px 0 -1px rgba(194, 245, 255, .4);
    animation: bubbles-rise 12s linear infinite;
}

@keyframes rays {
    from { transform: translateX(-10px); opacity: .6; }
    to { transform: translateX(12px); opacity: 1; }
}

@keyframes particles {
    from { background-position: 0 0, 0 0, 0 0, 0 0; }
    to { background-position: 0 -180px, 0 -210px, 0 -240px, 0 -180px; }
}

@keyframes whale-swim {
    from { transform: translateX(-28px) translateY(0) scale(.9); }
    to { transform: translateX(32px) translateY(-15px) scale(1); }
}

@keyframes seaweed-sway {
    from { rotate: -3deg; }
    to { rotate: 3deg; }
}

@keyframes leaf-sway {
    from { rotate: -8deg; }
    to { rotate: 9deg; }
}

@keyframes bubbles-rise {
    from { transform: translateY(0); }
    to { transform: translateY(-700px); }
}

/* About */
.about {
    position: relative;
    text-align: center;
    padding: 90px 22px;
    background:
        radial-gradient(ellipse at 50% 0%, rgba(13, 104, 137, .18), transparent 65%),
        #031727;
}

.section-label {
    direction: ltr;
    color: var(--cyan);
    font-size: 11px;
    letter-spacing: 4px;
    margin-bottom: 14px;
}

.about h2,
.collection h2 {
    font-size: clamp(25px, 4vw, 36px);
    margin-bottom: 18px;
}

.about p {
    max-width: 650px;
    margin: auto;
    color: var(--muted);
    line-height: 2.2;
}

/* Products */
.collection {
    padding: 80px 7% 100px;
    text-align: center;
    background:
        radial-gradient(ellipse at 50% 0%, rgba(5, 70, 103, .2), transparent 60%),
        #021321;
}

.products {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 22px;
    margin-top: 42px;
    text-align: center;
}

.product-box {
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 17px 23px;
    border-radius: 12px;
    background: linear-gradient(160deg, #0b2c43, #061b2c 80%);
    border: 1px solid rgba(104, 208, 239, .19);
    box-shadow: 0 12px 35px rgba(0, 0, 0, .16);
    transition: transform .25s, border-color .25s;
}

.product-box:hover {
    transform: translateY(-6px);
    border-color: rgba(141, 234, 255, .55);
}

.product-box img {
    width: 100%;
    height: 210px;
    object-fit: contain;
    margin-bottom: 17px;
    border-radius: 5px;
}

.product-box h3 {
    direction: ltr;
    font-size: 17px;
    margin-bottom: 9px;
    color: #ffffff;
}

.product-box p {
    min-height: 55px;
    color: #b7cedb;
    font-size: 13px;
    line-height: 1.9;
}

.price {
    margin: 13px 0 17px;
    color: var(--gold);
    font-size: 14px;
    font-weight: 700;
}

.order-button {
    display: block;
    width: 100%;
    margin-top: auto;
    padding: 11px 8px;
    background: #087e76;
    color: white;
    border: 1px solid rgba(120, 255, 224, .18);
    border-radius: 5px;
    font-weight: 700;
    font-size: 14px;
    transition: background .2s;
}

.order-button:hover {
    background: #0b9d8b;
}

footer {
    text-align: center;
    padding: 30px 20px;
    background: #010c15;
    border-top: 1px solid rgba(141, 234, 255, .12);
    color: #8faab9;
    font-size: 12px;
    line-height: 2;
}

footer strong {
    direction: ltr;
    display: inline-block;
    color: var(--cyan);
    letter-spacing: 3px;
}

@media (max-width: 1000px) {
    .products {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 600px) {
    header {
        padding: 12px 5%;
        min-height: 68px;
    }

    .logo {
        font-size: 27px;
        letter-spacing: 4px;
    }

    nav {
        gap: 13px;
    }

    nav a {
        font-size: 12px;
    }

    .hero {
        min-height: 620px;
        padding: 90px 18px 115px;
    }

    .hero h1 {
        letter-spacing: 8px;
        padding-left: 8px;
    }

    .hero p {
        font-size: 14px;
    }

    .whale {
        left: 48%;
        top: 22%;
        transform: scale(.75);
    }

    .seaweed {
        transform: scale(.7);
    }

    .seaweed-right {
        transform: scaleX(-1) scale(.7);
    }

    .about {
        padding: 65px 22px;
    }

    .collection {
        padding: 65px 5% 75px;
    }

    .products {
        gap: 12px;
    }

    .product-box {
        padding: 12px 10px 15px;
    }

    .product-box img {
        height: 150px;
    }

    .product-box h3 {
        font-size: 14px;
    }

    .product-box p {
        font-size: 12px;
    }

    .price {
        font-size: 12px;
    }

    .order-button {
        font-size: 12px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">SOVA</div>
  <nav>
    <a href="#home">الرئيسية</a>
    <a href="#about">من نحن</a>
    <a href="#collection">عطورنا</a>
    <a href="#cart" id="cart-link">🛒 السلة (<span id="cart-count">0</span>)</a>
</nav>
</header>

<section class="hero" id="home">

    <div class="underwater-scene" aria-hidden="true">
        <div class="whale">
            <div class="whale-body"></div>
            <div class="whale-tail"></div>
            <div class="whale-fin"></div>
        </div>

        <div class="seaweed seaweed-left">
            <i></i><i></i><i></i><i></i><i></i><i></i>
        </div>

        <div class="seaweed seaweed-right">
            <i></i><i></i><i></i><i></i><i></i><i></i>
        </div>

        <div class="bubbles"></div>
    </div>

    <div class="small-title">THE ART OF PERFUMERY</div>
    <h1>SOVA</h1>
    <h2>مو مجرد عطر، هذا حضور</h2>

    <p>
        اكتشف عالم الروائح المميزة<br>
        وخلي عطرك يحچي عن شخصيتك
    </p>

    <a href="#collection" class="gold-button">اكتشف عطورنا</a>
</section>

<section class="about" id="about">
    <div class="section-label">OUR PHILOSOPHY</div>
    <h2>الفخامة تبدأ من التفاصيل</h2>
    <p>
        في SOVA نختار عطور تجمع بين الأناقة والحضور،
        حتى نساعدك تلقى الرائحة اللي تناسب شخصيتك.
    </p>
</section>


<section class="collection" id="collection">
    <div class="section-label">OUR COLLECTION</div>
    <h2>عطور SOVA</h2>

    <div class="products">

        <div class="product-box">
            <img src="/static/images/afnan.jpg"
                 alt="Afnan 9 PM"
                 onerror="this.style.display='none';">
            <h3>Afnan 9 PM</h3>
            <p>عطر مميز لمحبي الروائح الجذابة والحضور القوي</p>
            <div class="price">65,000 دينار عراقي</div>

            <button class="order-button" type="button"
                    onclick="addToCart('Afnan 9 PM', 65000)">
                🛒 أضف إلى السلة
            </button>

            <a class="order-button"
               href="https://wa.me/9647806364447?text=السلام%20عليكم،%20أريد%20أطلب%20عطر%20Afnan%209%20PM%20بسعر%2065000%20دينار"
               target="_blank" rel="noopener">اطلب الآن</a>
        </div>

        <div class="product-box">
            <img src="/static/images/asad.jpg"
                 alt="Lattafa Asad"
                 onerror="this.style.display='none';">
            <h3>Lattafa Asad</h3>
            <p>عطر رجالي بطابع دافئ وجذاب</p>
            <div class="price">45,000 دينار عراقي</div>

            <button class="order-button" type="button"
                    onclick="addToCart('Lattafa Asad', 45000)">
                🛒 أضف إلى السلة
            </button>

            <a class="order-button"
               href="https://wa.me/9647806364447?text=السلام%20عليكم،%20أريد%20أطلب%20عطر%20Lattafa%20Asad%20بسعر%2045000%20دينار"
               target="_blank" rel="noopener">اطلب الآن</a>
        </div>

        <div class="product-box">
            <img src="/static/images/FREEZE%20RIIFFS.jpg"
                 alt="FREEZE RIIFFS"
                 onerror="this.style.display='none';">
            <h3>FREEZE RIIFFS</h3>
            <p>عطر فريز بطابع مميز وجذاب</p>
            <div class="price">50,000 دينار عراقي</div>

            <button class="order-button" type="button"
                    onclick="addToCart('FREEZE RIIFFS', 50000)">
                🛒 أضف إلى السلة
            </button>

            <a class="order-button"
               href="https://wa.me/9647806364447?text=السلام%20عليكم،%20أريد%20أطلب%20عطر%20FREEZE%20RIIFFS%20بسعر%2050000%20دينار"
               target="_blank" rel="noopener">اطلب الآن</a>
        </div>

        <div class="product-box">
            <img src="/static/images/FREEZE%20IN%20FLAMES%20RIIFFS.jpg"
                 alt="FREEZE IN FLAMES RIIFFS"
                 onerror="this.style.display='none';">
            <h3>FREEZE IN FLAMES RIIFFS</h3>
            <p>عطر فريز برائحة مميزة</p>
            <div class="price">50,000 دينار عراقي</div>

            <button class="order-button" type="button"
                    onclick="addToCart('FREEZE IN FLAMES RIIFFS', 50000)">
                🛒 أضف إلى السلة
            </button>

            <a class="order-button"
               href="https://wa.me/9647806364447?text=السلام%20عليكم،%20أريد%20أطلب%20عطر%20FREEZE%20IN%20FLAMES%20RIIFFS%20بسعر%2050000%20دينار"
               target="_blank" rel="noopener">اطلب الآن</a>
        </div>

    </div>
</section>

<section class="collection" id="cart">
    <div class="section-label">YOUR SHOPPING CART</div>
    <h2>سلة مشترياتك 🛒</h2>

    <div id="cart-items">
        <p>جاري تحميل السلة...</p>
    </div>

    <div class="price" style="margin-top: 20px;">
        المجموع: <span id="cart-total">0</span> دينار عراقي
    </div>

    <button class="order-button"
            type="button"
            onclick="renderCart()">
        تحديث السلة
    </button>
</section>

<footer>
    <strong>SOVA</strong>
    <p>عطرك جزء من حضورك</p>
    <p>للطلب والاستفسار تواصل ويانا عبر واتساب</p>
</footer>


<script>
const CART_KEY = "sova_cart";

function getCart() {
    return JSON.parse(localStorage.getItem(CART_KEY) || "[]");
}

function addToCart(name, price) {
    const cart = getCart();
    const item = cart.find(product => product.name === name);

    if (item) {
        item.quantity += 1;
    } else {
        cart.push({ name: name, price: price, quantity: 1 });
    }

    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartCount();
    renderCart();
    alert("تمت إضافة " + name + " إلى سلة SOVA 🛒");
}

function updateCartCount() {
    const count = getCart().reduce(
        (total, item) => total + item.quantity, 0
    );

    const counter = document.getElementById("cart-count");
    if (counter) counter.textContent = count;
}

function renderCart() {
    const cart = getCart();
    const container = document.getElementById("cart-items");
    const totalElement = document.getElementById("cart-total");

    if (!container || !totalElement) return;

    container.replaceChildren();
    let total = 0;

    if (cart.length === 0) {
        container.textContent = "سلتك فارغة حالياً 🛒";
        totalElement.textContent = "0";
        return;
    }

    cart.forEach((item, index) => {
        total += item.price * item.quantity;

        const row = document.createElement("div");
        row.className = "product-box";

        const name = document.createElement("h3");
        name.textContent = item.name;

        const details = document.createElement("p");
        details.textContent =
            "السعر: " + item.price.toLocaleString("en-US") +
            " دينار | الكمية: " + item.quantity;

        const minus = document.createElement("button");
        minus.className = "order-button";
        minus.textContent = "−";
        minus.onclick = () => changeQuantity(index, -1);

        const plus = document.createElement("button");
        plus.className = "order-button";
        plus.textContent = "+";
        plus.onclick = () => changeQuantity(index, 1);

        const remove = document.createElement("button");
        remove.className = "order-button";
        remove.textContent = "حذف العطر";
        remove.onclick = () => removeFromCart(index);

        row.append(name, details, minus, plus, remove);
        container.appendChild(row);
    });

    totalElement.textContent = total.toLocaleString("en-US");
}

function changeQuantity(index, amount) {
    const cart = getCart();
    if (!cart[index]) return;

    cart[index].quantity += amount;

    if (cart[index].quantity <= 0) {
        cart.splice(index, 1);
    }

    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartCount();
    renderCart();
}

function removeFromCart(index) {
    const cart = getCart();
    cart.splice(index, 1);
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartCount();
    renderCart();
}

document.addEventListener("DOMContentLoaded", () => {
    updateCartCount();
    renderCart();
});
</script>

</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)
